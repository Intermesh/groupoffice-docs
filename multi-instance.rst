Multi Instance
==============

It's possible to host multiple instances of Group Office on one server. After
installing Group Office via the Debian packages or Docker you do the following
to enable it:

1. Make sure the main install database user has permissions to create databases
   by running the folowing SQL:
   
   .. code:: sql

      GRANT ALL PRIVILEGES ON *.* TO 'groupoffice'@'%' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
   
2. Create "multi_instance" config folder (Skip this when using Docker)::

      mkdir /etc/groupoffice/multi_instance && chown www-data:www-data /etc/groupoffice/multi_instance
	 

3. Create "multi_instance" data folder (Skip this when using Docker)::
   
      mkdir /var/lib/groupoffice/multi_instance && chown www-data:www-data /var/lib/groupoffice/multi_instance
   
4. Login as administrator into the main Group Office instance that will manage the
   other instances and install the "Multi Instance" module from the "Community" package.

