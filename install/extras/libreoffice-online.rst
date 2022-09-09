.. _libreoffice-online:

LibreOffice Online
==================

.. figure:: /_static/using/files/collabora-online.png
   :alt: Collabora Online

With LibreOffice Online you can edit office documents in your browser. You need a working
LibreOffice Online server. More info on https://www.libreoffice.org/download/libreoffice-online/

For LibreOffice Online to work you need to setup SSL and allow your Group-Office URL to use it.
In case you need some guidance on how to set it up we wrote a blog post on how to setup
LibreOffice Online here:

http://groupoffice.blogspot.com/2021/03/installing-libreoffce-online.html

Install the Office Online module from the Business package at :ref:`System Settings -> Modules <modules>`.

.. figure:: /_static/using/files/install-office-online.png
   :alt: Install Office Online
   :width: 400px

Reload Group-Office and go to System Settings -> Office Online.

Then add your LibreOffice Online Service. The default port for LibreOffice online is 9980. BUt with the reverse proxy setup
above we're using the standard SSL port so it's not necessary to specify it.

.. figure:: /_static/using/files/add-collabora-code-service.png
   :alt: Add LibreOffice Online Service
   :width: 400px

Now you can open a document in the files module with LibreOffice by right clicking on a file and
choose :ref:`'Open with...' <files-open-with>`.

.. figure:: /_static/using/files/open-with-collabora-online.png
   :alt: Use LibreOffice Online Service
   :width: 400px


.. note:: If you get a 404 error when editing because /wopi is not found then you probably are missing the alias in your
   webserver configuration. The Group-Office Debian and Docker packages automatically create this but with the tarball
   package you have to do this manually.
   :ref:`Example configuration can be found here. <webserver-aliases>`
