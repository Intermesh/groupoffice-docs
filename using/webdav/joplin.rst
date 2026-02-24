.. _joplin:

Synchronizing Joplin Note Books
===============================

According to `its own website <https://joplinapp.org>`_, Joplin is an open source note-taking app. One powerful feature
of Joplin is the ability to synchronize to any remote service, like WebDAV.

.. note:: Joplin can not be used as a drop-in replacement for our notes module. If you want to edit notes from within GroupOffice itself, you should simply use the :ref:`notes<notes>` module.

Preparing GroupOffice
``````````````````````

First and foremost, please make sure that WebDAV is up and running. If you used our Debian or Docker installation methods,
WebDAV works out of the box. Otherwise, you will have to :ref:`set it up manually<webserver-aliases>`:


It is recommended that you create a folder in your GroupOffice user folder. For the sake of this tutorial, it is simply
called 'joplin' and it is a direct subdirectory of your home directory.

Setting up Joplin
`````````````````

If you haven't already, it is advisable to `set up End-to-End Encryption <https://joplinapp.org/help/apps/sync/e2ee#enabling-e2ee>`_
first. Having done that, open the Options screen from the main menu. Select the tab labeled 'Synchornization' and set
the following options:

.. table:: Joplin setup
   :widths: auto

   ======================  ============================================================================================================================================
   Parameter               Description
   ======================  ============================================================================================================================================
   Synchronization target  WebDAV
   WedDAV URL              The full URL to your WebDAV endpoint, appended with your username and folder name, e.g. `https://group-office.example.com/webdav/you/joplin`
   WebDAV username         Your GroupOffice username
   WebDAV password         Your GroupOffice password
   ======================  ============================================================================================================================================

You can test the connection by clicking the button labeled 'Check synchronization configuration'. If all is well, save
the settings and you are set.

