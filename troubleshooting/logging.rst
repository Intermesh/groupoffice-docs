Logging
=======

Errors on the Group-Office server will be logged trough PHP. Normally you can find errors in the webserver error log.
When using apache this is::

   /var/log/apache2/error.log
   
ActiveSync is implemented with the Z-push library. This will log errors to::

   <file_storage_path>/log/z-push-error.log
   
Debugging
---------

When $config['debug'] = true; is set in :ref:`config.php <configuration>`. Then debug info will be logged into::

   <file_storage_path>/log/debug.log
   
Z-Push / Microsoft ActiveSync
-----------------------------
   
Either when $config['debug'] = true; or $config['zpush2_loglevel'] = 32; is set in :ref:`config.php <configuration>`. Then additional
ActiveSync information will be logged into::

   <file_storage_path>/log/z-push.log

If you want to debug specific users you can set::

   $config['zpush2_special_log_users'] = ['username1', 'username2'];

Command Line tools
``````````````````

You can also monitor resources with the top tool::

    php ./modules/z-push/z-push-top.php

You can also manage devices with the admin tool::

    php ./modules/z-push/z-push-admin.php


.. note:: In  a multi instance environment you can set the HTTP_HOST environment variable to switch
    between instances::

        export HTTP_HOST=myinstance.example.com