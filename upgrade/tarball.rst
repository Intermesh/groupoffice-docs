Manual upgrade from the Tarball
-------------------------------

We strongly recommend that you use our Debian packages or Docker instead of the
tarball. But if you really want use it then follow these steps:

1. Grab the version to install from https://sourceforge.net/projects/group-office/files
2. Make sure your system meets the :ref:`system-requirements`.
3. Make sure you're on the latest minor release of your current version (For example 6.2.112 or 6.3.76).
4. When running 6.2 make sure you've installed the "customfields" and "search" modules as they 
   will become part of the Group-Office core.
5. Move away your old source files to a backup location.
   
   .. warning:: Do not copy the new files over the existing. This will result in a broken system.
      
6. Put the new files at the right location.
7. If exists copy your old config.php or config.ini and license file to the new 
   files. It is good practice to keep these files one directory higher then the 
   Group-Office source so you have a complete clean code base.
8. Visit http://yourdomain/install/ and follow instructions.
9. Check if you have the right cron job in place::

      * * * * * www-data php <YOURDOCUMENTROOT>/cron.php

.. warning:: If you're upgrading from 6.2 to 6.3 or higher and you are running the CGI version of PHP then you need to add a reqrite rule to add the "Authorization" header. Read more at :ref:`cgi-authorization`.
