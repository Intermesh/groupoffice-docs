Troubleshooting
===============

Upgrading
---------

In recent 6.6 versions and up, the upgrade script is not being automatically anymore after updating the package. You will
see this message in the screen:


.. figure:: /_static/troubleshooting/service_unavailable.png
   :width: 80%


This is perfectly normal! If you are the server administrator, you will need to run the upgrade script manually, thus
finishing the upgrade process. If not, notify the administrator that they should finish the upgrade process.

Troubleshooting errors
----------------------

The code base of Group Office has roughly two parts: a Javascript part that runs code in the browser and a server side API.


Client-side errors
``````````````````
If something unexpected happens (or does not happen unexpectedly!), first check the Javascript console for error messages.
You can normally open the Javascript developer console by pressing Ctrl+Shift+i or F12, depending on the browser. Errors,
warnings and informational messages can be found in the tab 'Console'.

.. note:: If you enable debugging, your client side error messages will be more verbose. Add or edit the line ``$config["debug"] = true;`` in your Group Office configuration file (normally ``/etc/groupoffice/config.php``


Server-side errors
``````````````````

In the Networking tab of your developer toolbox, you can view the individual requests to the API or server, as well as
a response code. These HTTP response codes are pretty easy to read and helpful when checking whether the problem is on the
server.

- 2XX : the request was successful. In some cases, the script was successful, but there feedback from the API, like form validation errors. In those cases, a helpful message is returned.
- 4XX: the script or file unavailable to the current user. That is either because the user does not have the proper permission or the file does not exist.
- 5XX: there is an actual error in a script.

Log entries can normally be found in the log files of the web server. The exact location of the error log depends on your
configuration, but ``/var/log/apache2`` is the default location for apache in many Linux distributions.

ActiveSync
``````````
When you're having issues with synchronisation there are some additional log files you can inspect. Read more about that `here <https://groupoffice.readthedocs.io/en/latest/logging.html#z-push>`__.

Also check if https://yourhostname.com/Microsoft-Server-ActiveSync is presenting a login dialog and is not displaying errors.

Asking support
--------------

Here's a few helpful hints that will help us troubleshoot Group Office if needed. When using our ticketing system (when
you have access to our ticketing system, you know) or
`Github <https://github.com/Intermesh/groupoffice/issues?page=2&q=is%3Aissue+is%3Aopen>`_, it may be helpful to provide
the following information:

- Describe your problem as thoroughly as possible.
   - What was your expected result?
   - What was the actual result?
   - What were the steps to reproduce this error?
- What is the current GO version that you are using?
- In some cases, server details may be relevant like PHP version, MySQL / MariaDB version of even version of the operating system.

