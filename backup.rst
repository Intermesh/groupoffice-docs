Backup
======

You need to backup the following items:

1. The configuration file :ref:`config.php <configuration>`. Can be found in /etc/groupoffice or in
   the source directory.

2. The MySQL / MariaDB database. You can find the connection parameters in :ref:`config.php <configuration>`.

3. The data folder. You can find the "file_storage_path" in the :ref:`config.php <configuration>` file.

4. If you use the Group-Office mailserver, then also backup the e-mail that's 
   located in /var/mail/vhosts.


Recovery
--------

To recover a backup simply replace the folders you've backed up using the information above and restore the database.

Oops, I accidentally deleted something...
`````````````````````````````````````````

Mistakes happen. Sometimes you've accidentally deleted something from Group-Office. You could then restore all missing
items from a backup by merging. Please be aware that everthing that was deleted will be restored. Also the items that
you deleted intentionally.

Steps:

1. Load the backup database in a temporary database called "groupoffice_temp" in this example::

      mysql -u root -p -e 'create database groupoffice_temp;'
      mysql -u root -p groupoffice_temp < backup.sql
      mysqldump --no-create-info --insert-ignore --complete-insert -u root -p groupoffice_temp > merge-data.sql

2. Your file merge-data.sql will contain the command to insert in the database and ignore the insert if the record already
   exists. Now load this into your live database called "groupoffice_live" in this example::

      mysql -u root -p groupoffice_live < merge-data.sql

3. Now all records should be back in the database. To reset the Group-Office cache and sync states run the upgrade procdure in the browser::

    https://groupoffice.example.com/install/upgrade.php

4. If you also need to restore missing files the use the command line utility rsync to restore the data.
