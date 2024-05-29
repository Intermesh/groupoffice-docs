Upgrading on Debian / Ubuntu
============================

Core system
-----------

Running 6.3 or higher
`````````````````````

To upgrade minor releases run:

.. code:: bash

   apt-get update
   apt-get install groupoffice

This will install the new software and upgrades the database.
When Group-Office open Group-Office now they will get a message that the service is unavailable at this time because an
upgrade is being installed.

.. note:: If for any reason you see a maintenance screen when launching Group-Office. Then launch /install to upgrade the database or run it on the command line::

     sudo -u www-data /usr/share/groupoffice/cli.php core/System/upgrade -c=/etc/groupoffice/config.php

Major release upgrade
~~~~~~~~~~~~~~~~~~~~~
When the second digit increases in the version number we call this a major release. For example when upgrading to 6.4 from 6.3.
When upgrading to the next major release follow these steps prior to the above:

1. Run the above command first to upgrade to the latest 6.x
   **Note**: if you're on version 6.2 please read section below first.

2. Then open your browser to update the database.

4. Make sure to install the latest license key from our website if you run the professional version.

5. Major release upgrades can't be skipped so you need to do them step by step.
   Adjust the repository to the next major release in '/etc/apt/sources.list.d/groupoffice.list':

    - For 6.8 change it to::

         deb http://repo.group-office.com/ sixeight main

      .. note:: In 6.8 we switched from Ioncube to SourceGuardian. Please make sure SourceGuardian is installed.
         See point 7. at :ref:`install-debian`. If you're not using Ioncube for something else then you can uninstall it.

    - For 6.7 change it to::

        deb http://repo.group-office.com/ sixseven main

    - For 6.6 change it to::

         deb http://repo.group-office.com/ sixsix main

      .. note:: In 6.6 we changed the dependency from "mariadb-server" or "mysql-server" into a recommendation for the "default-mysql-server". On Ubuntu server this leads to the situation where "mariadb-server" is suggested to be auto removed. To solve this you can install it manually with "apt install mariadb-server".

      
    - For 6.5 change it to::
   
         deb http://repo.group-office.com/ sixfive main

    - For 6.4 change it to::

         deb http://repo.group-office.com/ 64-php-71 main

      Or when running PHP 7.0::

         deb http://repo.group-office.com/ 64-php-70 main


From older versions than 6.3
````````````````````````````

- `First checkout the blog post about this release <http://groupoffice.blogspot.com/2018/07/group-office-63-released.html>`_
- 6.3 offers quite a lot of changes. It's strongly recommended to upgrade in a test environment first.
- After the upgrade you should consider replacing the "gota" module with the new
  "assistant" module for better file editing on the desktop.
- Typically the Custom CSS module was used to replace the logo. To take advanage of 
  the new System Settings -> Appearance features you should remove this CSS code.
- If you customized language then you should convert this to the new language :ref:`customize-language` system.
- If your system is older than 6.2 your system probably depends on mcrypt. If you 
  migrate to a new server and you run into email password problems you might need 
  to install https://pecl.php.net/package/mcrypt to decrypt email passwords. 
  If you have plain MD5 hashes in your pa_mailboxes database table run this SQL query::

     update `pa_mailboxes` set `password` = concat("{PLAIN-MD5}", `password`) WHERE `password` NOT LIKE '{%' AND `password` NOT LIKE '$%';

Steps
~~~~~

1. Make sure you're on the latest 6.2 version.
2. Make sure you've installed the "customfields" and "search" modules as they 
   will become part of the Group-Office core.
3. If you are coming from version 5.0 or lower. Then you must install the projects2 module in 6.2 to migrate your existing data. This can't be done in a later version!
4. Uninstall the old "groupoffice-com" package but do **NOT** deconfigure the database:

   .. code:: bash
   
      apt-get remove groupoffice-com
      
5. If you made manual changes inside /usr/share/groupoffice (Like installing z-push for example). The the package manager will leave these folders intact. To avoid problems move /usr/share/groupoffice away before installing::
   
      mv /usr/share/groupoffice /root/groupofficebak

6. Edit /etc/apt/sources.list and remove:

   .. code:: bash
   
      deb http://repos.groupoffice.eu/ sixtwo main

7. Now do a fresh install of the **6.3** Debian package. But note:

   - When the installer asks to install a database choose "NO".
   - When the installer asks to replace /etc/groupoffice/config.php, choose 
     "Keep the local version currently installed".
   - Use the following APT repository in /etc/apt/sources.list.d/groupoffice.list::

         deb http://repo.group-office.com/ 63-php-71 main
      
     Or when running PHP 7.0::

         deb http://repo.group-office.com/ 63-php-70 main


Mailserver
----------

If you're upgrading from a previous 6.3.x or higher version simply run::

   apt-get install groupoffice-mailserver

Or if you also installed the anti spam and virus package:

   apt-get install groupoffice-mailserver groupoffice-mailserver-antispam

Upgrading from 6.2
``````````````````

1. To upgrade from 6.2 you must start with a clean system by removing all previous
software and configuration. **Make a backup!**::

      apt-get purge groupoffice-mailserver dovecot* postfix* clamav* spamassassin amavisd-new

2. Then install the new package::

      apt-get install groupoffice-mailserver

3. Move the mail to the new location::

      mv /home/vmail/* /var/mail/vhosts
      rmdir /home/vmail

4. Remove no longer required packages::
      
      apt-get autoremove
