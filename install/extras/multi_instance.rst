.. _multi-instance:

Multi Instance
--------------

It's possible to host multiple instances of Group Office on one server. They all have their own
database and optionally a license for additional modules.
When pointing the DNS of a domain with a wildcard to the server, you can create a new instance
with a few mouse clicks or via an API.

Installation
````````````

After installing Group Office via the Debian packages or Docker you'll need to do the following
to enable it:

1. Make sure the main install database user has permissions to create databases
   by running the following SQL:

   .. code:: sql

      GRANT ALL PRIVILEGES ON *.* TO 'groupoffice'@'%' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

2. Create "multi_instance" config folder (Skip this when using Docker)::

      mkdir /etc/groupoffice/multi_instance && chown www-data:www-data /etc/groupoffice/multi_instance

3. Create "multi_instance" data folder (Skip this when using Docker)::

      mkdir /var/lib/groupoffice/multi_instance && chown www-data:www-data /var/lib/groupoffice/multi_instance

4. If you're using the professional version and the studio module is allowed in /etc/groupoffice/globalconfig.inc.php
   (see default settings below), then a package folder will be created for each instance in
   /usr/share/groupoffice/go/modules. So you have to make that folder writable for the webserver::

      chown www-data:www-data /usr/share/groupoffice/go/modules

5. Login as administrator into the main Group Office instance that will manage the
   other instances and install the "Multi Instance" module from the "Community" package.

6. Make sure the instances DNS records (we recommend using a wildcard domain) are pointing to the server and is picked
   up by the apache configuration.

Creating an instance
````````````````````
In the "Multi instance" tab you can click the add button. Enter the full hostname of the instance and click "Save".
After that you can select which modules it's allowed to use.
Via the more menu in the grid you can login to this instance.

Deleting and restoring instances
````````````````````````````````

When you delete an instance it's stored in the trash folder. You can restore an instance with this command::

    ./cli.php community/multi_instance/Instance/restore --name=test.example.com

When you have deleted the same name for a second time the folder might be named with a suffix. You can specify the trash path in that case::

    ./cli.php community/multi_instance/Instance/restore --name=test.example.com --trashPath=-trashPath=/var/lib/groupoffice/multi_instance/_trash_/test.example.com-606050820f3d


Default settings
````````````````

You can control the default allowed modules via /etc/groupoffice/globalconfig.inc.php this file supports the same
properties as :ref:`config.php <configuration>` but applies to all instances if not overriden in the instance config
file.

New portals will also copy the system settings of the main portal.