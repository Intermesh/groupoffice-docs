Migrate
=======

To migrate Group-Office to another server you need to backup all data files and 
the database.

.. note:: The filesystem paths shown here might be different in your environment.

Create the backup
-----------------

1. Determine where the data files are stored (You can also just open :ref:`config.php <configuration>` and
   lookup the value instead of using 'cat' and 'grep' on linux)::

      cat /etc/groupoffice/config.php | grep file_storage_path

   This outputs::

      $config['file_storage_path']='/var/lib/groupoffice/';   
   
2. You might want to disable Group-Office so nobody can work in it anymore by adding or changing this value to the :ref:`config.php <configuration>`::

      $config['enabled'] = false;
   
3. This command outputs the database parameters (You can also just open :ref:`config.php <configuration>`
   and lookup the values instead of using 'cat' and 'grep' on linux)::

      cat config.php | grep db
 

  This outputs::

     $config['db_type']='mysql';
     $config['db_host']='localhost';
     $config['db_name']='groupoffice';
     $config['db_user']='groupoffice';
     $config['db_pass']='password';

4. Now create a dump of the database (replace '/var/lib/groupoffice/' with your actual path found in step 1)::

      mysqldump groupoffice -u groupoffice -p > /var/lib/groupoffice/groupoffice-20190101.sql
      
5. Now you can either:

      a. create an archive of this folder::
      
         tar czf groupoffice-backup.tar.gz /var/lib/groupoffice
      
      b. or transfer it directly with 'rsync' to the new server::
      
         rsync -av /var/lib/groupoffice user@newserver.com:/var/lib

Installing the backup on the new server
---------------------------------------

1. Install a clean :ref:`install` following this manual. You can install a newer version. Pick a version that can upgrade your current version. Please refer to the upgrade page.
2. If you created the archive then copy it to the new server in /tmp
   a. Replace the file folder with the groupoffice-backup.tar.gz contents. For example::

      # change to /tmp
      cd /tmp
      
      # unpack archive
      tar -zxf groupoffice-backup.tar.gz
      
      #backup the existing folder (should be empty but to be safe)
      mv /var/lib/groupoffice /var/lib/groupofficebak
      
      # move unpacked folder to /var/lib
      mv groupoffice /var/lib/
      
      # replace www-data with your web server user in the following command
      chown -R www-data:www-data /var/lib/groupoffice 
      
      
4. Replace the database with the mysqldump created in the backup. For example::
      
      # Import dump file to mysql
      mysql groupoffice -u groupoffice -p < /var/lib/groupoffice/groupoffice-20190101.sql
      
5. Run /install/ to finish.


.. note:: If you run into this error when importing the database dump file::

      ERROR 1118 (42000) at line x: Row size too large (> 8126). Changing some columns to TEXT or BLOB may help. In current row format, BLOB prefix of 0 bytes is stored inline

   Then try to add this line on top of the dump file::

      set innodb_strict_mode=0;

   and retry.

----------------

.. toctree::
   :maxdepth: 1
   :caption: Mailserver

   mail-server
