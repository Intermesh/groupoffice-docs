Upgrading on Debian / Ubuntu
============================

Core system
-----------

When running 6.3.x or higher simply do:

.. code:: bash

   apt-get install groupoffice

From older versions than 6.3
````````````````````````````

*Note:* 6.3 offers quite a lot of changes. It's strongly recommended to upgrade in a test environment first.

1. Make sure you're on the latest 6.2 version.
2. Make sure you've installed the "customfields" and "search" modules as they 
   will become part of the Group-Office core.
3. Uninstall the old "groupoffice-com" package but do **NOT** deconfigure the database:

   .. code:: bash
   
      apt-get remove groupoffice-com

4. Edit /etc/apt/sources.list and remove:

   .. code:: bash
   
      deb http://repos.groupoffice.eu/ sixtwo main

5. Now do a fresh install of the Debian package. But note:

   - When the installer asks to install a database choose "NO".
   - When the installer asks to replace /etc/groupoffice/config.php, choose 
     "Keep the local version currently installed".

Continue at :ref:`install-debian`.


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