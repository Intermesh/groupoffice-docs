.. _libreoffice-online:

LibreOffice Online
==================

.. figure:: /_static/using/files/collabora-online.png
   :alt: Collabora Online

With LibreOffice Online you can edit office documents in your browser. You need a working
LibreOffice Online server. More info on https://www.libreoffice.org/download/libreoffice-online/

For LibreOffice Online to work you need to setup SSL and allow your Group-Office URL to use it.

Docker
------

We found the easiest way to set it up is using Docker with Docker compose and Nginx or Apache as reverse proxy. If you
run it on the same server as Group-Office you should setup with Apache as the package comes with Apache.

Replace "docs.example.com" everywhere below with your hostname that you'll use to access LibreOffice Online.

Docker compose
~~~~~~~~~~~~~~

Create a file "docs.example.com/docker-compose.yml"::

    version: "3.6"
    services:
      libreoffice:
        image: libreoffice/online:master
        environment:
          domain: (.*\.example\.com|host\.docker\.internal)
          username: admin
          password: secret
          extra_params: --o:ssl.enable=false --o:ssl.termination=true
          DONT_GEN_SSL_CERT: 1
        volumes:
          - lo_config_volume:/etc/loolwsd
        cap_add:
          - MKNOD
        ports:
                - "127.0.0.1:9980:9980"
        restart:
          unless-stopped
    volumes:
      lo_config_volume:


Replace the domain part with a regular expression that allows the Group-Office hosts. For a single domain you can replace this
with just "groupoffice.example.com".

Start docker with the command in the directory "docs.example.com"::

    docker-compose up -d

Nginx
~~~~~
You can use either Nginx or Apache. If you already have Apache installed then skip this section and proceed with Apache.
Setup the virtual host in a new text file: /etc/nginx/sites-enabled/docs.example.com::

    # HTTPS Server
    server {
        listen 443 ssl;
        server_name docs.example.com;

        error_log /var/log/nginx/docs_error.log;

        # We use let's encrypt for SSL
        ssl_certificate /etc/letsencrypt/live/docs.example.com/fullchain.pem;
        ssl_trusted_certificate /etc/letsencrypt/live/docs.example.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/docs.example.com/privkey.pem;

        include /etc/letsencrypt/options-ssl-nginx.conf;

        # static files
        location ^~ /loleaflet {
            proxy_pass http://localhost:9980;
            proxy_set_header Host $http_host;
        }

        # WOPI discovery URL
        location ^~ /hosting/discovery {
            proxy_pass http://localhost:9980;
            proxy_set_header Host $http_host;
        }

        # Capabilities
        location ^~ /hosting/capabilities {
            proxy_pass http://localhost:9980;
            proxy_set_header Host $http_host;
        }

        # main websocket
        location ~ ^/lool/(.*)/ws$ {
            proxy_pass http://localhost:9980;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "Upgrade";
            proxy_set_header Host $http_host;
            proxy_read_timeout 36000s;
        }

        # download, presentation and image upload
        location ~ ^/lool {
            proxy_pass http://localhost:9980;
            proxy_set_header Host $http_host;
        }

        # Admin Console websocket
        location ^~ /lool/adminws {
            proxy_pass http://localhost:9980;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "Upgrade";
            proxy_set_header Host $http_host;
            proxy_read_timeout 36000s;
        }
    }

Check the nginx syntax with::

    nginx -t

It it's OK then reload nginx::

    systemctl reload nginx

Now that Libre Office online is running you can skip to the Group-Office section below to connect it.

Apache
~~~~~~

Create this virtual host in the text file /etc/apache2/sites-enabled::

    <VirtualHost *:443>
      ServerName docs.example.com:443
      Options -Indexes

      # SSL configuration, you may want to take the easy route instead and use Lets Encrypt!
      SSLEngine on
      SSLCertificateFile /path/to/signed_certificate
      SSLCertificateChainFile /path/to/intermediate_certificate
      SSLCertificateKeyFile /path/to/private/key
      SSLProtocol             all -SSLv2 -SSLv3
      SSLCipherSuite ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:ECDHE-ECDSA-DES-CBC3-SHA:ECDHE-RSA-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA:!DSS
      SSLHonorCipherOrder     on

      # Encoded slashes need to be allowed
      AllowEncodedSlashes NoDecode

      # Container uses a unique non-signed certificate
      SSLProxyEngine On
      SSLProxyVerify None
      SSLProxyCheckPeerCN Off
      SSLProxyCheckPeerName Off

      # keep the host
      ProxyPreserveHost On

      # static html, js, images, etc. served from loolwsd
      # loleaflet is the client part of LibreOffice Online
      ProxyPass           /loleaflet http://127.0.0.1:9980/loleaflet retry=0
      ProxyPassReverse    /loleaflet http://127.0.0.1:9980/loleaflet

      # WOPI discovery URL
      ProxyPass           /hosting/discovery http://127.0.0.1:9980/hosting/discovery retry=0
      ProxyPassReverse    /hosting/discovery http://127.0.0.1:9980/hosting/discovery

      # Capabilities
      ProxyPass           /hosting/capabilities http://127.0.0.1:9980/hosting/capabilities retry=0
      ProxyPassReverse    /hosting/capabilities http://127.0.0.1:9980/hosting/capabilities

      # Main websocket
      ProxyPassMatch "/lool/(.*)/ws$" ws://127.0.0.1:9980/lool/$1/ws nocanon

      # Admin Console websocket
      ProxyPass   /lool/adminws ws://127.0.0.1:9980/lool/adminws

      # Download as, Fullscreen presentation and Image upload operations
      ProxyPass           /lool http://127.0.0.1:9980/lool
      ProxyPassReverse    /lool http://127.0.0.1:9980/lool
    </VirtualHost>

Now that Libre Office online is running you can skip to the Group-Office section below to connect it.


Verify LibreOffice install
--------------------------

You can verify that the install worked by visiting the URL below in your browser:

https://docs.example.com/hosting/discovery

You should see an XML document. If not then look at the log files::

	docker-compose logs


Debian packages
---------------

SSL
~~~

We've used the Debian packages and setup SSL with Letsencrypt. Then we've added this SSL
configuration to /etc/loolwsd/loolwsd.xml::

    <ssl desc="SSL settings">
        <enable type="bool" desc="Controls whether SSL encryption is enable (do not disable for production deployment). If default is false, must first be compiled with SSL support to enable." default="true">true</enable>
        <termination desc="Connection via proxy where loolwsd acts as working via https, but actually uses http." type="bool" default="true">false</termination>
        <cert_file_path desc="Path to the cert file" relative="false">/etc/letsencrypt/live/groupoffice.co/cert.pem</cert_file_path>
        <key_file_path desc="Path to the key file" relative="false">/etc/letsencrypt/live/groupoffice.co/privkey.pem</key_file_path>
        <ca_file_path desc="Path to the ca file" relative="false">/etc/letsencrypt/live/groupoffice.co/fullchain.pem</ca_file_path>
        <cipher_list desc="List of OpenSSL ciphers to accept" default="ALL:!ADH:!LOW:!EXP:!MD5:@STRENGTH"></cipher_list>
        <hpkp desc="Enable HTTP Public key pinning" enable="false" report_only="false">
            <max_age desc="HPKP's max-age directive - time in seconds browser should remember the pins" enable="true">1000</max_age>
            <report_uri desc="HPKP's report-uri directive - pin validation failure are reported at this URL" enable="false"></report_uri>
            <pins desc="Base64 encoded SPKI fingerprints of keys to be pinned">
            <pin></pin>
            </pins>
        </hpkp>
    </ssl>

Network
~~~~~~~

Change network settings to allow posting from your Group-Office URL.
We've used a wildcard for all subdomains *.*\.example\.com* for example::

   <net desc="Network settings">
      <proto type="string" default="all" desc="Protocol to use IPv4, IPv6 or all for both">all</proto>
      <listen type="string" default="any" desc="Listen address that loolwsd binds to. Can be 'any' or 'loopback'.">any</listen>
      <service_root type="path" default="" desc="Prefix all the pages, websockets, etc. with this path."></service_root>
      <post_allow desc="Allow/deny client IP address for POST(REST)." allow="true">
        <host desc="The IPv4 private 192.168 block as plain IPv4 dotted decimal addresses.">192\.168\.[0-9]{1,3}\.[0-9]{1,3}</host>
        <host desc="Ditto, but as IPv4-mapped IPv6 addresses">::ffff:192\.168\.[0-9]{1,3}\.[0-9]{1,3}</host>
        <host desc="The IPv4 loopback (localhost) address.">127\.0\.0\.1</host>
        <host desc="Ditto, but as IPv4-mapped IPv6 address">::ffff:127\.0\.0\.1</host>
	    <host desc="The IPv6 loopback (localhost) address.">::1</host>
	    <host desc="wildcard" allow="true">.*\.example\.com</host>
      </post_allow>
      <frame_ancestors desc="Specify who is allowed to embed the LO Online iframe (loolwsd and WOPI host are always allowed). Separate multiple hosts by space."></frame_ancestors>
    </net>

Storage
~~~~~~~

Change the backend storage to allow your Group-Office URL::

    <storage desc="Backend storage">
        <filesystem allow="false" />
	    <wopi desc="Allow/deny wopi storage. Mutually exclusive with webdav." allow="true">
            <host desc="wildcard" allow="true">.*\.example\.com</host>
	        <host desc="Regex pattern of hostname to allow or deny." allow="true">localhost</host>
            <host desc="Regex pattern of hostname to allow or deny." allow="true">10\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}</host>
            <host desc="Regex pattern of hostname to allow or deny." allow="true">172\.1[6789]\.[0-9]{1,3}\.[0-9]{1,3}</host>
            <host desc="Regex pattern of hostname to allow or deny." allow="true">172\.2[0-9]\.[0-9]{1,3}\.[0-9]{1,3}</host>
            <host desc="Regex pattern of hostname to allow or deny." allow="true">172\.3[01]\.[0-9]{1,3}\.[0-9]{1,3}</host>
            <host desc="Regex pattern of hostname to allow or deny." allow="true">192\.168\.[0-9]{1,3}\.[0-9]{1,3}</host>
            <host desc="Regex pattern of hostname to allow or deny." allow="false">192\.168\.1\.1</host>
            <max_file_size desc="Maximum document size in bytes to load. 0 for unlimited." type="uint">0</max_file_size>
        </wopi>
        <webdav desc="Allow/deny webdav storage. Mutually exclusive with wopi." allow="false">
            <host desc="Hostname to allow" allow="false">localhost</host>
        </webdav>
    </storage>

After making these changes restart loolwsd::

    sudo systemctl restart loolwsd

Check the status::

    sudo systemctl status loolwsd

If anything is wrong view the logs::

    sudo journalctl -u loolwsd


Group-Office connection
-----------------------

When LibreOffice Online is running you can setup Group-Office to use it. Install the Office Online module from the Business package.

.. figure:: /_static/using/files/install-office-online.png
   :alt: Install Office Online
   :width: 400px

Reload Group-Office and go to System Settings -> Office Online

Then add your Collabora Code Service. The default port for LibreOffice online is 9980. BUt with the reverse proxy setup
above we're using the standard SSL port so it's not necessary to specify it.

.. figure:: /_static/using/files/add-collabora-code-service.png
   :alt: Add LibreOffice Online Service
   :width: 400px

Now every user can go to the files module and use it. Just right click a file and choose "Open with...".

.. figure:: /_static/using/files/open-with-collabora-online.png
   :alt: Use LibreOffice Online Service
   :width: 400px


.. note:: If you get a 404 error when editing because /wopi is not found then you probably are missing the alias in your
   webserver configuration. The Group-Office Debian package automatically does this but with the tarball package you have
   to do this manually.
   :ref:`Example configuration can be found here. <webserver-aliases>`
