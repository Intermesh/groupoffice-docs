Docker
======

Core System
-----------

It's very easy to install Group-Office with docker. Please follow the instructions
on our docker-groupoffice github repository:

https://github.com/Intermesh/docker-groupoffice

If you'd like to setup a developer environment then you should use:

https://github.com/Intermesh/docker-groupoffice-development

Multi Instance
--------------

It's possible to host multiple instances of Group Office on one server. After
installing Group Office via the Debian packages or Docker you do the following
to enable it:

1. Make sure the main install database user has permissions to create databases
   by running the following SQL:
   
   .. code:: sql

      GRANT ALL PRIVILEGES ON *.* TO 'groupoffice'@'%' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
   
2. Login as administrator into the main Group Office instance that will manage the
   other instances and install the "Multi Instance" module from the "Community" package.

