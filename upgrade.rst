Upgrade Group-Office
====================

General
-------
You can upgrade any version from Group-Office. For some versions it's necessary
to do it in steps:

- 2.18 can upgrade to 3.7.55
- 3.7.55 can upgrade to 6.2
- 6.2 can upgrade to 6.3

Needless to say, but always make a **backup** before upgrading.

Upgrading on Debian / Ubuntu
----------------------------

When running 6.3.x or higher simply do:

.. code:: bash

   apt-get install groupoffice

From older versions than 6.3
````````````````````````````

- `First checkout the blog post about this release <http://groupoffice.blogspot.com/2018/07/group-office-63-released.html>`_
- 6.3 offers quite a lot of changes. It's strongly recommended to upgrade in a test environment first.
- After the upgrade you should consider replacing the "gota" module with the new
  "assistant" module for better file editing on the desktop.
- Typically the Custom CSS module was used to replace the logo. To take advanage of 
  the new System Settings -> Appearance features you should remove this CSS code.
- If you customized language then you should convert this to the new language :ref:`customize-language` system.

Steps
^^^^^

1. Make sure you're on the latest 6.2 version.
2. Make sure you've installed the "customfields" and "search" modules as they 
   will become part of the Group-Office core.
3. Uninstall the old "groupoffice-com" package but do **NOT** deconfigure the database:

   .. code:: bash
   
      apt-get remove groupoffice-com
      
4. If you made manual changes inside /usr/share/groupoffice (Like installing z-push for example). The the package manager will leave these folders intact. To avoid problems move /usr/share/groupoffice away before installing::
   
      mv /usr/share/groupoffice /root/groupofficebak

5. Edit /etc/apt/sources.list and remove:

   .. code:: bash
   
      deb http://repos.groupoffice.eu/ sixtwo main

6. Now do a fresh install of the Debian package. But note:

   - When the installer asks to install a database choose "NO".
   - When the installer asks to replace /etc/groupoffice/config.php, choose 
     "Keep the local version currently installed".

Continue at :ref:`install-debian`.


Upgrading the Docker images
---------------------------

Please follow the instructions on our docker-groupoffice github repository:

https://github.com/Intermesh/docker-groupoffice

Or if you've used our developer environment then visit:

https://github.com/Intermesh/docker-groupoffice-development


Manual upgrade from the Tarball
-------------------------------

We strongly recommend that you use our Debian packages or Docker instead of the
tarball. But if you really want use it then follow these steps:

1. Make sure your system meets the :ref:`system-requirements`.
2. Make sure you're on the latest 6.2 version.
3. Make sure you've installed the "customfields" and "search" modules as they 
   will become part of the Group-Office core.
4. Move away your old source files. Important! Do not copy the new files over 
   the existing.
5. Put the new files at the right location.
6. If exists copy your old config.php or config.ini and license file to the new 
   files. It is good practice to keep these files one directory higher then the 
   Group-Office source so you have a complete clean code base.
7. Visit http://yourdomain/install/ and follow instructions.
8. Check if you have the right cron job in place:

      .. code:: bash

      * * * * * www-data php <YOURDOCUMENTROOT>/cron.php
