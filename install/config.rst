Configuration file
==================

The configuration file can be found in:

- /etc/groupoffice/config.php
- /etc/groupoffice/multi_instance/<DOMAINNAME>/config.php
- The root of the Group-Office installation

Here's a list of config options:

.. table:: Config options
   :widths: auto

   ====================  ======  ===========
   Name                  Type    Description
   ====================  ======  ===========
   db_name               string  Database name
   db_host               string  Database server hostname
   db_port               string  Database server port
   db_user               string  Database username
   db_pass               string  Database password
   file_storage_path     string  Where the files on disk are stored
   tmpdir                string  Temporary files directory
   sseEnabled            bool    Enable Server Sent Events for live push updates. Some servers don't support two connections!
   quota                 int     Max storage in bytes this installation may use
   max_users             int     Max number of users this system may have
   allowed_modules       string  Comma separated string of modules the system may use
   product_name          string  For branding the system to another name
   debug                 bool    Enable debugging for developers. Can also be temporarilty enabled with CTRL + F7 or Cmd + F7 in the browser.
   debugLog              bool    Disable debug log when debug = true.
   servermanager         bool    Set by multi_instance module. This will copy system settings and create welcome message on install.
   zpush2_loglevel       int     Set to 32 to generate debugging info in log/z-push.log
   ====================  ======  ===========

Recommended PHP settings
------------------------

For optimal Group-Office perfomance we recommend these settings. This will allow users to upload files up to 1GB:

.. table:: PHP settings
   :widths: auto

   ====================  ===========
   Name                  Value
   ====================  ===========
   memory_limit          256M
   post_max_size         1000M
   max_upload_size       1000M
   ====================  ===========
