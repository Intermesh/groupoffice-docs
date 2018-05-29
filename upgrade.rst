Upgrade Group-Office
====================

General
-------
You can upgrade any version from Group-Office. For some versions it's necessary
to do it in steps:

- 2.18 can upgrade to 3.7.55
- 3.7.55 can upgrade to 6.2
- 6.2 can upgrade to 6.3

Needless to say, but always make a **backup** before upgrading.

Upgrading on Debian / Ubuntu
----------------------------

When running 6.3.x or higher simply do:

.. code:: bash

   apt-get install groupoffice

From older versions than 6.3
````````````````````````````

1. Make sure you're on the latest 6.2 version.

2. Create a dump of the "groupofficecom" database (Lookup password in /etc/groupoffice/config.php):

   .. code:: bash
   
      mysqldump -u groupoffice-com -p groupofficecom > ~/groupoffice-com.sql

3. Then uninstall the old "groupoffice-com" package:

   .. code:: bash
   
      apt-get remove groupoffice-com

4. Edit /etc/apt/sources.list and remove:

   .. code:: bash
   
      deb http://repos.groupoffice.eu/ sixtwo main

5. Now do a fresh install of the Debian package. But don't run the web installer. See :ref:`install-debian`.

6. Now import your database (Lookup new password in /etc/groupoffice/config.ini)

   .. code:: bash
   
      mysql -u groupoffice -p groupoffice < ~/groupoffice-com.sql

7. Remove fresh data folder:

   .. code:: bash
   
      rmdir /var/lib/groupoffice 

8.  move Group-Office data folder to the new location:

   .. code:: bash

      mv /home/groupoffice /var/lib/groupoffice

9. Upgrade the database by visiting http://yourdomain/install/upgrade.php

You're all done!


Upgrading the Docker images
---------------------------

Please follow the instructions on our docker-groupoffice github repository:

https://github.com/Intermesh/docker-groupoffice

Or if you've used our developer environment then visit:

https://github.com/Intermesh/docker-groupoffice-development


Manual upgrade from the Tarball
-------------------------------

We strongly recommend that you use our Debian packages or Docker instead of the
tarball. But if you really want use it then follow these steps:

1. Make sure your system meets the :ref:`system-requirements`.
2. Move away your old source files. Important! Do not copy the new files over the existing.
3. Put the new files at the right location.
4. If exists copy your old config.php or config.ini and license file to the new files. It is good practice to keep these files one directory higher then the Group-Office source so you have a complete clean code base.
5. Visit http://yourdomain/install/upgrade.php to perform the database upgrade.
