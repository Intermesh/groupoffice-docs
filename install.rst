Installation
============

We recommend installing using the Debian packages or Docker. These methods will
install all dependencies automatically and will be the easiest for you.

.. _install-debian:

Install on Debian / Ubuntu
----------------------------

Our preferred way of installing is using our Debian packages:

1. On Debian login as the root server and on Ubuntu become root by running::

      sudo -s

2. First add our repository to the package management system. 

   If you run PHP 7.0 (Debian 9) run::
   
      echo  "deb http://repo.group-office.com/ 63-php-70 main" | tee -a /etc/apt/sources.list

   If you run PHP 7.1 or greater (Ubuntu 18.04+) add::

      echo  "deb http://repo.group-office.com/ 63-php-71 main" | tee -a /etc/apt/sources.list

3. Add our public key::

      apt-key adv --recv-keys --keyserver pool.sks-keyservers.net 0758838B

4. Update APT::

      apt-get update

5. Then install Group-Office by running::

      apt-get install groupoffice

6. Then visit http://yourserver/groupoffice and the installer should appear:

   .. figure:: _static/installer.png
      :alt: The Group-Office installer

      The Group-Office installer

7. Follow the instructions on screen and enjoy Group-Office!

Install with Docker
-------------------

It's very easy to install Group-Office with docker. Please follow the instructions
on our docker-groupoffice github repository:

https://github.com/Intermesh/docker-groupoffice

If you'd like to setup a developer environment then you should use:

https://github.com/Intermesh/docker-groupoffice-development

Install with the Tarball download
---------------------------------

We strongly recommend that you use our Debian packages or Docker over this method.
But if you really want to use the Tarball source then here is how.

.. _system-requirements:

System requirements
^^^^^^^^^^^^^^^^^^^

You need a Linux server with:

.. table:: Software
   :widths: auto

   ====================  ===========
   Type                  Requirement
   ====================  ===========
   Operating System      Linux / Docker
   Webserver             Apache 2+
   Database              MySQL 5.3+
   Programming language	 PHP 7.0+
   ====================  ===========

Required PHP Extensions
+++++++++++++++++++++++

- pcre       
- mbstring
- ctype
- date
- iconv
- curl
- zip
- soap
- gd
- pdo
- pdo_mysql
- calendar

1. Grab the source from:

   https://sourceforge.net/projects/group-office/files/6.3/

2. Put the unpacked source in apache's document root.

3. Make sure to make some aliases in the Apache configuration:

   .. code:: bash
   
   	 Alias /public <YOURDOCUMENTROOT>/public.php
   
   	 Alias /Microsoft-Server-ActiveSync <YOURDOCUMENTROOT>/modules/z-push/index.php
   
   	 #For CalDAV support
   	 Alias /caldav <YOURDOCUMENTROOT>/modules/caldav/calendar.php
   
   	 #For CardDAV support
   	 Alias /carddav <YOURDOCUMENTROOT>/modules/carddav/addressbook.php
   
   	 #For WebDAV support
   	 Alias /webdav <YOURDOCUMENTROOT>/modules/dav/files.php
   
   
   	 #DAV Service discovery. At least required for iOS7 support
   	 Redirect 301 /.well-known/carddav /carddav
     Redirect 301 /.well-known/caldav /caldav

4. Open it in the web browser. Then follow the installer's instructions.

5. Create a cron job:

   .. code:: bash

      * * * * * www-data php <YOURDOCUMENTROOT>/cron.php
