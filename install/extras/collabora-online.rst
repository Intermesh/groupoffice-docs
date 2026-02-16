.. _collabora-online-install:

Collabora Online
================

.. figure:: /_static/using/files/collabora-online.png
   :alt: Collabora Online

With Collabora Online you can co-edit office documents in your browser. You need a working
Collabora Online server. You can find more info on https://www.collaboraonline.com/.

Install the **Office Online** module from the Business package at :ref:`System Settings -> Modules <modules>`.

.. figure:: /_static/using/files/install-office-online.png
   :alt: Install Office Online
   :width: 400px

Reload Group-Office and go to System Settings -> Office Online.

Then add your Collabora Online Service. The default port for Collabora Online is **9980**. But with the reverse proxy setup
above we're using the standard SSL port so it's not necessary to specify it.

.. figure:: /_static/using/files/add-collabora-code-service.png
   :alt: Add Collabora Online Service
   :width: 400px

Now you can open a document in the files module with **Collabora Online** by right clicking on a file and
choose :ref:`'Open with...' <files-open-with>`.

.. figure:: /_static/using/files/open-with-collabora-online.png
   :alt: Use Collabora Online Service
   :width: 400px


.. note:: If you get a 404 error when editing because /wopi is not found then you probably are missing the alias in your
   webserver configuration. The Group-Office Debian and Docker packages automatically create this but with the tarball
   package you have to do this manually.
   :ref:`Example configuration can be found here. <webserver-aliases>`
