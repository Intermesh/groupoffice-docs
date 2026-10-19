.. _http-proxy:

HTTP Proxy
==========

Sometimes it's handy to use a http proxy like nginx or apache to forward requests to an internal server or Docker container running GroupOffice. If you do this then you need to set these headers to make GroupOffice operate properly:

- X-Forwarded-Proto : http or https. This is the protocol the proxy server uses.
- X-Forwarded-Host : The hostname of the proxy server.

See for more information:

- nginx: https://linuxize.com/post/nginx-reverse-proxy/
- Apache: https://httpd.apache.org/docs/2.4/mod/mod_proxy.html#x-headers


.. _http-proxy-client-ip:

Client IP address
-----------------

GroupOffice uses the IP address of the client to throttle failed login attempts, for the IP address restrictions of
user groups and in the audit logs.

By default this is the address of the connection to the server. Headers like ``X-Forwarded-For`` or ``Client-IP`` are
**ignored**, because a client can set them to anything. An attacker could otherwise use a different fake address for each
login attempt to get around the throttling, or pretend to be on a trusted network.

When there is a reverse proxy or load balancer in front of GroupOffice, all connections come from that proxy. Then you
have two options.

**Option 1: configure the trusted proxies in GroupOffice**

Add the IP address or the CIDR range of your proxy to :ref:`config.php <configuration>`:

.. code-block:: php

   $config['trustedProxies'] = ['10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16'];

For connections from these addresses GroupOffice reads the client address from the ``X-Forwarded-For`` header. It
walks through the header from right to left and uses the first address that is not a trusted proxy. Everything before
that is supplied by the client and is not used. IPv4 and IPv6 are supported.

Your proxy must add the address it received the request from to ``X-Forwarded-For``, like the nginx example below does
with ``$proxy_add_x_forwarded_for``. Other headers such as ``X-Real-IP`` and ``Forwarded`` are not used.

.. note:: With Docker the proxy often connects from the address of the Docker network gateway. This is usually in
   the 172.16.0.0/12 range, but check with ``docker network inspect``.

**Option 2: let the web server set the real IP**

The web server that passes requests to PHP can replace the connection address with the one in the header, but only for
your own proxies. GroupOffice then needs no configuration.

For nginx, using the `realip module <https://nginx.org/en/docs/http/ngx_http_realip_module.html>`_:

.. code-block::

    set_real_ip_from 172.16.0.0/12;
    real_ip_header X-Forwarded-For;
    real_ip_recursive on;

For Apache, enable ``mod_remoteip`` (``a2enmod remoteip``) and use:

.. code-block::

    RemoteIPHeader X-Forwarded-For
    RemoteIPInternalProxy 172.16.0.0/12

.. important:: If you upgrade from a version that trusted the ``X-Forwarded-For`` header from everyone and you use a
   reverse proxy, then you must configure one of the options above. Otherwise every user appears to come from the IP
   address of the proxy. Failed logins of one user then count against everybody, and IP address restrictions
   of groups no longer match.

   Without a proxy in front of the web server (for example nginx or Apache with PHP-FPM that clients connect to
   directly) nothing needs to be done.


504 Gateway Time-out
--------------------

Some requests to GroupOffice live for a long time:

- sse.php: Used for server sent events to update changes with a push notification. It lives for 120s
- Microsoft-Server-ActiveSync, For synchronising mobile devices. It may live up to 3600s.

In your Apache Proxy configuration you could use::

    ProxyTimeout 1800


Nginx with Docker example
-------------------------

Here's an example for nginx with docker.

.. code-block::

    server {
        listen 443 ssl;
        server_name groupoffice.example.com;

        ssl_certificate /etc/letsencrypt/live/groupoffice.example.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/groupoffice.example.com/privkey.pem;

        # for large file uploads
        client_max_body_size 5G;

         location / {
             proxy_pass http://localhost:9090;
             proxy_set_header Host $host;
             proxy_set_header X-Real-IP $remote_addr;
             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header X-Forwarded-Proto https;
         }
    }


Apache2 with PHP FPM example
----------------------------


.. code-block::

    <VirtualHost *:443>

   	<Directory /usr/share/groupoffice/www>
       Options -Indexes +FollowSymLinks
       AllowOverride None

       #Enable for apache 2.4
       Require all granted
     </Directory>

    ServerName groupoffice.example.com
    DocumentRoot /usr/share/groupoffice

    ErrorLog /var/log/apache2/groupoffice_error.log
    CustomLog /var/log/apache2/groupoffice_access.log combined

    SSLEngine On
   	SSLCertificateKeyFile /etc/letsencrypt/live/groupoffice.example.com/privkey.pem
   	SSLCertificateFile /etc/letsencrypt/live/groupoffice.example.com/fullchain.pem

    Alias /Microsoft-Server-ActiveSync /usr/share/groupoffice/www/modules/z-push/index.php
    Alias /caldav /usr/share/groupoffice/www/modules/caldav/calendar.php
    Alias /carddav /usr/share/groupoffice/www/modules/carddav/addressbook.php
    Alias /webdav /usr/share/groupoffice/www/modules/dav/files.php
    Alias /wopi /usr/share/groupoffice/www/go/modules/business/wopi/wopi.php
    Alias /onlyoffice /usr/share/groupoffice/www/go/modules/business/onlyoffice/connector.php

    #autoconfig
    Alias /mail/config-v1.1.xml /usr/share/groupoffice/go/modules/community/autoconfig/autoconfig.php
    Alias /v1.1/mail/config-v1.1.xml /usr/share/groupoffice/go/modules/community/autoconfig/autoconfig.php
    Alias /.well-known/autoconfig/mail/config-v1.1.xml /usr/share/groupoffice/go/modules/community/autoconfig/autoconfig.php

    #autodiscover
    #  Alias /autodiscover/autodiscover.json /usr/share/groupoffice/go/modules/community/autoconfig/autodiscover-json.php
    Alias /Autodiscover/Autodiscover.xml /usr/share/groupoffice/go/modules/community/autoconfig/autodiscover.php
    Alias /autodiscover/autodiscover.xml /usr/share/groupoffice/go/modules/community/autoconfig/autodiscover.php

    #openID service discovery
    Alias /.well-known/openid-configuration /usr/share/groupoffice/api/oauth.php/.well-known/openid-configuration


    #PHP-FPM proxy config

    # Increased timeout for long running requests (sse, activesync)
    ProxyTimeout 1800

    # flushpackets is required for SSE to work
    ProxyPassMatch "^/sse.php.*$" "fcgi://localhost" flushpackets=on

    #Pass authorization header
    SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1

    # For apache2 + php-fpm. This is required to make PUT request with chunked transfer encoding work. MacOS Finder
    # uses this to upload with WebDAV.
    SetEnv proxy-sendcl 1

    <FilesMatch \.php$>
        # For Apache version 2.4.10 and above, use SetHandler to run PHP as a fastCGI process server
        SetHandler "proxy:unix:/run/php/php8.4-fpm.sock|fcgi://localhost"
    </FilesMatch>

    #End PHP-FPM proxy config
    </VirtualHost>