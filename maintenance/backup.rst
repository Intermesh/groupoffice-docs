Backup
======

You need to backup the following items:

1. The configuration file :ref:`config.php <configuration>`. Can be found in ``/etc/groupoffice`` or in
   the source directory.

2. The MySQL / MariaDB database. You can find the connection parameters in :ref:`config.php <configuration>`.

3. The data folder. You can find the "file_storage_path" in the :ref:`config.php <configuration>` file.

4. If you use the GroupOffice mailserver, then also backup the e-mail that's
   located in ``/var/mail/vhosts``.


Recovery
--------

To recover a backup simply replace the folders you've backed up using the information above and restore the database.

Oops, I accidentally deleted something...
`````````````````````````````````````````

Mistakes happen. Sometimes you've accidentally deleted something from GroupOffice. You could then restore all missing
items from a backup by merging. Please be aware that everthing that was deleted will be restored. Also the items that
you deleted intentionally.

Steps:

1. Load the backup database in a temporary database called "groupoffice_temp" in this example::

      mysql -e 'create database groupoffice_temp;'
      mysql groupoffice_temp < backup.sql
      
      
2. Export the data with insert ignore statements so it will only import missing records::

      mysqldump --no-create-info --insert-ignore --complete-insert groupoffice_temp > merge-data.sql
      
  Or if you'd like to restore just some tables (be careful you need to know the database very well)::

     mysqldump --no-create-info --insert-ignore --complete-insert groupoffice_temp "core_pdf_block" "core_pdf_template" "core_email_template" "core_email_template_attachment" > merge-data.sql
     
  If you would like to overwrite existing data you can use the --replace flag instead of --insert-ignore. Be careful!

3. Your file merge-data.sql will contain the command to insert in the database and ignore the insert if the record already
   exists. Now load this into your live database called "groupoffice_live" in this example::

      mysql groupoffice_live < merge-data.sql

4. Now all records should be back in the database. To reset the GroupOffice cache and sync states run the upgrade procdure in the browser::

    https://groupoffice.example.com/install/upgrade.php

5. If you also need to restore missing files the use the command line utility rsync to restore the data.
