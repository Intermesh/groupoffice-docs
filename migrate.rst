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

   tar -czf groupoffice-database.tar.gz groupoffice-20190101.sql

Now we've packed up all necessary files in archives:

- groupoffice-files.tar.gz
- groupoffice-database.tar.gz

Installing the backup on the new server
---------------------------------------

1. Install a clean :ref:`install` following this manual. You can install a newer version. Pick a version that can upgrade your current version. Please refer to the upgrade page.
2. Copy the archives created to the new server in /tmp
3. Replace the file folder with the groupoffice-files.tar.gz contents. For example::

      # change to /tmp
      cd /tmp
      
      # unpack archive
      tar -zxf groupoffice-files.tar.gz
      
      #backup the existing folder (should be empty but to be safe)
      mv /var/lib/groupoffice /var/lib/groupofficebak
      
      # move unpacked folder to /var/lib
      mv groupoffice /var/lib/
      
      # replace www-data with your web server user in the following command
      chown -R www-data:www-data /var/lib/groupoffice 
      
      
4. Replace the database with the mysqldump created in the backup. For example::
      
      # change to /tmp
      cd /tmp
      
      # unpack archive
      tar -zxf groupoffice-database.tar.gz
      
      # Import dump file to mysql
      mysql groupoffice -u groupoffice -p < groupoffice-20190101.sql
      
5. Run /install/ to finish.


.. note:: If you run into this error when importing the database dump file::

      ERROR 1118 (42000) at line x: Row size too large (> 8126). Changing some columns to TEXT or BLOB may help. In current row format, BLOB prefix of 0 bytes is stored inline

   Then try to add this line on top of the dump file::

      set innodb_strict_mode=0;

   and retry.
