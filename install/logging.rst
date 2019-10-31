Logging
=======

Errors on the Group-Office server will be logged trough PHP. Normally you can find errors in the webserver error log. When using apache this is::

   /var/log/apache2/error.log
   
ActiveSync is implemented with the Z-push library. This will log errors to::

   <file_storage_path>/log/z-push-error.log
   
Debugging
---------

When $config['debug'] = true; is set in config.php. Then debug info will be logged into::

   <file_storage_path>/log/debug.log
   
When $config['zpush2_loglevel'] = 32; is set in config.php. Then additional ActiveSync information will be logged into:

   <file_storage_path>/log/z-push.log
