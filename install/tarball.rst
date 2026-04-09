Manual from Tarball 
-------------------

We strongly recommend that you use our Debian packages or Docker over this method.
But if you really want to use the Tarball source then here is how.

Instructions
^^^^^^^^^^^^

1. Grab the source from:

   https://github.com/Intermesh/groupoffice/releases

2. Put the unpacked source in apache's document root.

.. _webserver-aliases:

3. Make sure to make some aliases in the Apache configuration::
   
      Alias /public <YOURDOCUMENTROOT>/public.php

      Alias /Microsoft-Server-ActiveSync <YOURDOCUMENTROOT>/modules/z-push/index.php

      #For CalDAV support
      Alias /caldav <YOURDOCUMENTROOT>/modules/caldav/calendar.php

      #For CardDAV support
      Alias /carddav <YOURDOCUMENTROOT>/modules/carddav/addressbook.php

      #For WebDAV support
      Alias /webdav <YOURDOCUMENTROOT>/modules/dav/files.php
      
      #For WOPI support (Collabora Online and Office Online)
      Alias /wopi <YOURDOCUMENTROOT>/go/modules/business/wopi/wopi.php

      #For OnlyOffice support
      Alias /onlyoffice <YOURDOCUMENTROOT>/go/modules/business/onlyoffice/connector.php

      #For OpenID service discovery
      Alias /.well-known/openid-configuration <YOURDOCUMENTROOT>/api/oauth.php/.well-known/openid-configuration

      #DAV Service discovery. At least required for iOS7 support
      Redirect 301 /.well-known/carddav /carddav
      Redirect 301 /.well-known/caldav /caldav
       
   Or if you're not able to add these aliases you could create a .htaccess file and use mod_rewrite rules. These
   aliases must work in the root of your domain so don't put this in a subdirectory. In example groupoffice.example.com/webdav and not
   www.example.com/groupoffice/webdav::

      # Enable rewriting
      RewriteEngine On

      # Set the base to slash as it may already have been set to something else in the main configuration.
      RewriteBase /
      
      # The following two lines are only necessary when using PHP in CGI mode and not an apache module
      RewriteCond %{HTTP:Authorization} ^(.*)
      RewriteRule .* - [e=HTTP_AUTHORIZATION:%1]
      
      # Configure /webdav, /caldav etc. on your domain
      RewriteRule ^webdav(.*)$ /modules/dav/files.php
      RewriteRule ^caldav(.*)$ /modules/caldav/calendar.php
      RewriteRule ^carddav(.*)$ /modules/carddav/addressbook.php
      RewriteRule ^wopi(.*)$ /go/modules/business/wopi/wopi.php/$1 [L]
      RewriteRule ^Microsoft-Server-ActiveSync(.*)$ /modules/z-push/index.php
      RewriteRule ^onlyoffice(.*)$ /go/modules/business/onlyoffice/connector.php/$1 [L]
      RewriteRule "^/\.well-known/openid-configuration"  "/api/oauth.php/.well-known/openid-configuration" [PT]


4. If you purchased GroupOffice Professional licenses then make sure the
   `SourceGuardian loader <https://www.sourceguardian.com/loaders.html>`_ is installed.

5. Then visit http://yourserver/ and the installer should appear:

   .. figure:: /_static/installer.png
      :alt: The GroupOffice installer

      The GroupOffice installer

6. Follow the instructions on screen.

7. Finally, create a cron job for the scheduled tasks. For example in the file /etc/cron.d/groupoffice::

      * * * * * www-data php <YOURDOCUMENTROOT>/cron.php
      
   Optionally you can add the config file location::
   
      * * * * * www-data php <YOURDOCUMENTROOT>/cron.php /etc/groupoffice/myoffice/config.php
   
      
.. _cgi-authorization:

Authentication with CGI or FastCGI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When using PHP through CGI the "Authorization" header might not be passed by default.
You can enable this header by setting the Authorization as environment variable in
your VirtualHost section or .htacess file::

    SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1

Alternatively you could use these "mod_rewrite" rules::

    RewriteEngine On
    RewriteCond %{HTTP:Authorization} ^(.*)
    RewriteRule .* - [e=HTTP_AUTHORIZATION:%1]


