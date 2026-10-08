Tools
=====

Under tools you can execute various maintenance tasks.

System check
------------
Checks if your server meets all requirements

Database check
--------------
Checks your database for errors and fixes them if possible.

You can also run this on the command line::

   sudo -u www-data /usr/share/groupoffice/groupofficecli.php -r=maintenance/checkDatabase

Update search index
-------------------

Checks the search index for missing entries and adds them.
You can also run this on the command line::

   sudo -u www-data /usr/share/groupoffice/groupofficecli.php -r=maintenance/buildSearchCache

For a specific module::

   sudo -u www-data /usr/share/groupoffice/groupofficecli.php -r=maintenance/buildSearchCache --module=projects2

Update search index (Complete rebuild)
--------------------------------------
The same as above but it first removes all cached entries.

.. warning:: During the process search results and links will not appear until they are reindexed.

On the command line::

   sudo -u www-data /usr/share/groupoffice/groupofficecli.php -r=maintenance/buildSearchCache --reset=1

Remove duplicate contacts and events
------------------------------------

Checks for duplicates and you can delete them if you confirm.

Sync filesystem
---------------

Checks if the filesystem is in sync with the database. Adds and removes missing files.

You can run it on the command line too::

   sudo -u www-data /usr/share/groupoffice/groupofficecli.php -r=files/folder/syncFilesystem
   
Or specify a path::

   sudo -u www-data /usr/share/groupoffice/groupofficecli.php -r=files/folder/syncFilesystem --path=projects2


Delete folder
-------------

Be careful! Since version 26.0.36, You can delete a folder by path on the CLI with this command::

    sudo -u www-data /usr/share/groupoffice/groupofficecli.php -r=files/folder/deleteByPath --path=tmp


Update file search index
------------------------

Indexes the filesearch module if installed.

You can run it on the command line too::

   sudo -u www-data /usr/share/groupoffice/groupofficecli.php -r=filesearch/filesearch/sync


Clear calendar holiday cache
----------------------------

Recalculates holidays in the calendar.


Reset JMAP sync state
---------------------

It's recommended to use the JMAP API but when making changes to the database directly it could be
useful to make clients resynchronize an entity::

    sudo -u www-data /usr/share/groupoffice/cli.php core/System/resetSyncState --entity=Contact

or to resynchronize everything::

    sudo -u www-data /usr/share/groupoffice/cli.php core/System/resetSyncState


Blob usage report
-----------------

This command prints  blob usage count per table and size on disk::

    sudo -u www-data /usr/share/groupoffice/cli.php core/System/blobReport


Server Side Events
------------------

Server Side Events (SSE for short) is a mechanism that notifies the various clients when entities are updated on the server
side layer. Entity stores are saved in the browser and as far as the client is concerned, it is a single source of truth.

By default, as an administrator, you do not have to do anything to make SSE work. It is on by default and has defaults are
sane. However, you can set a custom polling interval by setting the `sseCheckInterval` option. Alternatively, you can
disable SSE entirely by setting the `sseEnabled` option to `false`.