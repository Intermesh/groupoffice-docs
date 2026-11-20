.. _incremental-upgrades-on-debian:

Incremental Upgrades on Debian
==============================

Use Case
--------

This guide is meant for all system administrators who wish to migrate a very old GroupOffice version to a new server and
then upgrading to the latest version. Alternatively, the upgrades are on the server itself, although upgrading the
server itself is outside of this scope.

For the sake of this document, we upgrade from GroupOffice 5.0 to 26.0 and move the entire installation to a new server.
The OS for this server has either a modern Debian or Ubuntu Server version.

Preparation
-----------

On the new server, during the upgrade process, you will have to switch PHP versions at least once. By default, both
Debian and Ubuntu come with only one PHP version, which is normally a recent version. Therefore, we add an external
repository:

.. code::  bash

    sudo apt update
    sudo apt install -y apt-transport-https lsb-release ca-certificates curl
    sudo curl -sSLo /tmp/debsuryorg-archive-keyring.deb https://packages.sury.org/debsuryorg-archive-keyring.deb
    sudo dpkg -i /tmp/debsuryorg-archive-keyring.deb
    sudo apt update

Then, we install the latest GroupOffice using this guide: :ref:`install-debian`.

Moving the Backups
------------------

- From the old server, copy the database dump to the new server and import it directly into the groupoffice database.
- From the old server, copy the data directory, e.g. as a tarball and extract in into a new folder, e.g. `groupoffice-bacup-files`.
- Delete the current data directory: `rmdir /var/lib/groupoffice`
- `mv groupoffice-backup-files /var/lib/groupoffice`
- Write down the credentials for the GroupOffice database, copy the ``config.php`` file from the old server, copy it over the current ``config.php`` file in ``/etc/groupoffice/`` and update the database credentials for the new database.

PHP 7.4 and Ioncube
-------------------

The first upgrade is to the latest 6.2 version (assuming we move from an earlier version that is). Install PHP7.4 and ioncube

.. code:: bash

    apt install php7.4-cli php7.4-mbstring php7.4-mysql php7.4-xml php7.4-curl php7.4-gd php7.4-intl php7.4-xsl php7.4-apcu

Also, download and run our inocube installation script here: https://github.com/Intermesh/groupoffice/blob/master/scripts/install-ioncube.sh

Upgrade to the Latest 6.2 Version
---------------------------------

.. note:: If you already run 6.2.134 or up, you may skip this section

Update the `config.php` file with two lines:

.. code:: php

    $config['file_storage_path'] = '/var/lib/groupoffice/';
    $config['allowed_modules'] = "";

It is important to keep the trailing slash, as 6.2 required this in order for the upgrade to work. The `allowed_modules`
setting needs to be empty to avoid problems with upgrading refactored modules.

Create a temporary subdirectory for GO, download and extract the GroupOffice 6.2 tarball into said directory:

.. code:: bash

    mkdir -p /var/www/go
    cd /var/www/go
    wget https://sourceforge.net/projects/group-office/files/6.2/groupoffice-com-6.2.134-php-7.1.tar.gz/download
    tar zxf download
    rm download

If you have any licenses, make sure that they are installed in the newly unpacked root directory for Group-Office.

Now run the initial upgrade of 6.2:

.. code:: bash

    sudo -u www-data php7.4 ./groupoffice-com-6.2.134-php-7.1/groupofficecli.php -r=maintenance/upgrade`

If all is well, restore the `file_storage_path` option to its original value, i.e. remove the trailing slash. Make a
database backup of the 6.2 database.

.. code:: bash

    mysqldump groupoffice > go62.sql`

Make sure that the search and customfields modules are installed:

.. code:: bash

    mysql groupoffice -e 'set @aclId := (select acl_id from go_modules where id="users");insert ignore into go_modules values ("search",0,0,0,@aclId,1);'
    mysql groupoffice -e "select id from go_modules"

If the customfields module was not installed before, run these commands as well. If It already was, please skip these steps!

.. code:: bash

    mysql groupoffice -e 'set @aclId := (select acl_id from go_modules where id="users");insert into go_modules values ("customfields",0,0,0,@aclId,1);';
    mysql groupoffice < groupoffice-com-6.2.134-php-7.1/modules/customfields/install/install.sql

Finally, make sure that the projects2 module is installed when the original projects module was installed earlier.

Upgrade Each Release up to 6.7
------------------------------

.. note:: Before running each upgrade, make sure that the proper license file is copied to the root directory of each interim GO version, e.g. ``/var/www/go/groupoffice-6.3.99-php71/``.

.. tip:: After each upgrade, you may want to create a backup of the upgraded database. When an upgrade fails, you can restore the previous version instead of having to start all over.

Run the upgrade script for each version up to version 6.7. There is an optional command line parameter ``-c`` that will
allow you to upgrade a non-standard configuration file, which may come in handy if you run multiple instances on your server. If
you don't, it is safe to omit this parameter.

.. code:: bash

    wget https://sourceforge.net/projects/group-office/files/6.3/groupoffice-6.3.99-php-71.tar.gz/download
    tar zxf download
    rm download
    sudo -u www-data php7.4 ./groupoffice-6.3.99-php-71/install/upgrade.php [-c=/etc/groupoffice/multi_instance/customer.group-office.com/config.php]
    wget https://sourceforge.net/projects/group-office/files/6.4/groupoffice-6.4.247-php-71.tar.gz/download
    tar zxf download
    rm download

Please note that the upgrade to 6.4 will probably take very long, as the migration to the JMAP addressbook module is a
huge operation. This is expected behavior and no cause for alarm.

.. code:: bash

    sudo -u www-data php7.4 ./groupoffice-6.4.247-php-71/cli.php core/System/upgrade [-c=/etc/groupoffice/multi_instance/customer.group-office.com/config.php]
    wget https://github.com/Intermesh/groupoffice/releases/download/v6.5.113/groupoffice-6.5.113.tar.gz
    tar zxf groupoffice-6.5.113.tar.gz


As of GroupOffice 6.5, a license key is set in the database. We set it now:

.. code:: bash

    sudo -u www-data php7.4 ./groupoffice-6.5.113/cli.php core/System/setLicense --key=YOURKEY [-c=/etc/groupoffice/multi_instance/customer.group-office.com/config.php]

... and we move on, up to version 6.7, which is the last version that needs Ioncube.

.. code:: bash

    sudo -u www-data php7.4 ./groupoffice-6.5.113/cli.php core/System/upgrade [-c=/etc/groupoffice/multi_instance/customer.group-office.com/config.php]
    wget https://github.com/Intermesh/groupoffice/releases/download/v6.6.177/groupoffice-6.6.177.tar.gz
    tar zxf groupoffice-6.6.177.tar.gz
    sudo -u www-data php7.4 ./groupoffice-6.6.177/cli.php core/System/upgrade [-c=/etc/groupoffice/multi_instance/customer.group-office.com/config.php]
    wget https://github.com/Intermesh/groupoffice/releases/download/v6.7.54/groupoffice-6.7.54.tar.gz
    tar zxf groupoffice-6.7.54.tar.gz
    sudo -u www-data php7.4 ./groupoffice-6.7.54/cli.php core/System/upgrade [-c=/etc/groupoffice/multi_instance/customer.group-office.com/config.php]

Upgrade to 6.8 and Further
--------------------------

As with the previous section: make sure that after each upgrade, you make a new backup of the database. Also, with each
upgrade, only use the ``-c`` parameter if you need it.

The first step is to install PHP 8.2. Also, make sure that SourceGuardian is configured as a module for 8.2:

.. code:: bash

    apt install php8.2-cli php8.2-mbstring php8.2-mysql php8.2-xml php8.2-curl php8.2-gd php8.2-intl php8.2-xsl php8.2-apcu
    php8.2 -M

This will list all the installed and configured modules in the PHP CLI version. The configuration for this module is
shared with the Apache2 or FPM version as well. Now we perform the upgrades up to version 25:

.. code:: bash

    wget https://github.com/Intermesh/groupoffice/releases/download/v6.8.172/groupoffice-6.8.172.tar.gz
    tar zxf groupoffice-6.8.172.tar.gz
    sudo -u www-data php8.2 ./groupoffice-6.8.172/cli.php core/System/upgrade [-c=/etc/groupoffice/multi_instance/customer.group-office.com/config.php]
    wget https://github.com/Intermesh/groupoffice/releases/download/v25.0.108/groupoffice-25.0.108.tar.gz
    sudo -u www-data php8.2 ./groupoffice-25.0.108/cli.php core/System/upgrade [-c=/etc/groupoffice/multi_instance/customer.group-office.com/config.php]

Upgrade to Version 26.0
-----------------------

As you installed GroupOffice 26 from the repository in the first step, we now switch to the most modern PHP version we
support, which would be PHP8.5. Then we perform the final upgrade:

.. code:: bash

    apt install php8.5-cli php8.5-mbstring php8.5-mysql php8.5-xml php8.5-curl php8.5-gd php8.5-intl php8.5-xsl php8.5-apcu
    php8.5 -M # check whether SourceGuardian is still available
    sudo -u www-data /usr/share/groupoffice/cli.php core/System/upgrade [-c=/etc/groupoffice/multi_instance/customer.group-office.com/config.php]

Clean up some stuff and repopulate some the search cache:

.. code:: bash

    sudo -u www-data /usr/share/groupoffice/groupofficecli.php -r=maintenance/checkDatabase [-c=/etc/groupoffice/multi_instance/customer.group-office.com/config.php]
    sudo -u www-data /usr/share/groupoffice/groupofficecli.php -r=maintenance/buildSearchCache [-c=/etc/groupoffice/multi_instance/customer.group-office.com/config.php]

In case you encounter problems with linked e-mails, rebuild the search cache for these from scratch:

.. code:: bash

    sudo -u www-data /usr/share/groupoffice/groupofficecli.php -r=maintenance/buildSearchCache -c=/etc/groupoffice/config.php --reset=1 --modelName=GO\\Savemailas\\Model\\LinkedEmail

Congratulations! You are now fully up to date!

Optional Aftercare
------------------

- Remove the ``/var/www/go`` subdirectory.
- Remove old PHP versions: ``apt remove php7.4* php8.2*``
- If you feel particularly courageous, give the database some :ref:`spring cleaning<cleanup_database>`. **Do this at your own risk**.