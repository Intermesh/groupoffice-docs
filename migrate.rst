Migrate
=======

To migrate Group-Office to another server you need to backup all data files and 
the database.

.. note:: The filesystem paths shown here might be different in your environment.

Backup
------

Determine where the data files are stored (You can also just open :ref:`config.php <configuration>` and
lookup the value instead of using 'cat' and 'grep' on linux)::

   cat /etc/groupoffice/config.php | grep file_storage_path

This outputs::

   $config['file_storage_path']='/var/lib/groupoffice/';

Now create an archive of this path::

   tar czf groupoffice-files.tar.gz /var/lib/groupoffice

This command outputs the database parameters (You can also just open :ref:`config.php <configuration>`
and lookup the values instead of using 'cat' and 'grep' on linux)::

   cat config.php | grep db

This outputs::

   $config['db_type']='mysql';
   $config['db_host']='localhost';
   $config['db_name']='groupoffice';
   $config['db_user']='groupoffice';
   $config['db_pass']='password';
   
you might want to disable Group-Office so nobody can work in it anymore by adding this to :ref:`config.php <configuration>`::

   $config['enabled'] = false;

Now create a dump of the database::

   mysqldump groupoffice -u groupoffice -p > groupoffice-20190101.sql

You might want to compress this file to save bandwidth::

   tar czf groupoffice-database.tar.gz groupoffice-20190101.sql

Now we've packed up all necessary files in archives:

- groupoffice-files.tar.gz
- groupoffice-database.tar.gz

Installing the backup on the new server
---------------------------------------

1. Install a clean :ref:`install` following this manual
2. Replace the file folder with the groupoffice-file.tar.gz contents.
3. Replace the database with the mysqldump created in the backup.
4. Run /install/ to finish.


.. note:: If you run into this error when importing the database dump file::

      ERROR 1118 (42000) at line x: Row size too large (> 8126). Changing some columns to TEXT or BLOB may help. In current row format, BLOB prefix of 0 bytes is stored inline

   Then try to add this line on top of the dump file::

      set innodb_strict_mode=0;

   and retry.
