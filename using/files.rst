.. _files:

Files
=====

In the "Files" tab you can manage your personal files and share folders with other users. The files module is
integrated in most other modules as well. So you can add files to Contacts, Projects, Tasks, Appointments etc.

.. figure:: /_static/using/files/files.png
      :alt: Files module
      :width: 100%

      Home folder

The files module supports:

- :ref:`links`
- :ref:`custom-fields`
- :ref:`comments`
- :ref:`sharing`
- :ref:`files`


Share folders
-------------
It's easy to share folders in Group-Office. Any user can do it. If you want to create a shared folder for the whole
organization it's recommended to do this as the "admin" user. Take the following steps:

1. Right click on the folder that you want to share and click 'Properties'

   .. figure:: /_static/using/files/share-folder-1.png
      :alt: Share folder 1
      :width: 50%

2. Check 'Activate sharing'

   .. figure:: /_static/using/files/share-folder-2.png
      :alt: Share folder 2
      :width: 50%

3. Add the right user groups in the 'Permissions' tab.

   .. figure:: /_static/using/files/share-folder-3.png
      :alt: Share folder 3
      :width: 50%

The folder will show up under shared for other users. Not for the user that shared it.

.. figure:: /_static/using/files/share-folder-4.png
   :alt: Share folder 4
   :width: 50%

.. note:: Visibility of files is solely dependent on the permissions defined for its containing folder. There is no way to hide individual files except to move them in a private folder.

.. _files-open-with:

Opening files
-------------
Opening files is as easy as a double click on the file of course. But you can also change the default
action. For example you might want to edit text documents with :ref:`Only Office <onlyoffice>`,
:ref:`Microsoft Office Online <officeonline>` or your :ref:`own desktop application <assistant>`.
You can view images in the online viewer or in a browser tab. To change this
right click on a file and choose "Open with...". Check the box "Remember my decision for this file type"
to make it the default. Then choose your preferred action.

.. figure:: /_static/using/files/open-with-dialog.png
  :alt: Change default open file action
  :width: 100%

Integrations
------------

.. _assistant:

Assistant
~~~~~~~~~

The Group-Office Assistant is a small program that you can install on your Windows, MacOS or
Linux computer. It will automatically download files opened from Group-Office and monitor
it for changes. When the file is saved it automatically uploads it back to Group-Office.

It also assists in mounting a network drive.

Download it for:

- :ref:`Windows <assistant-for-windows>`
- :ref:`MacOS <assistant-for-macos>`
- :ref:`Linux <assistant-for-linux>`

.. _officeonline:

Microsoft Office Online
~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/using/files/microsoft-office-online.png
   :alt: Mirosoft Office Online

By becoming a Microsoft partner, we can offer Microsoft Office Online to everyone.
You need an Office 365 for business subscription.

In our cloud version it's already configured by default. Right click on a file and
open with "Office Online" and make it the default if you desire.

n our cloud version it's already configured by default. Now you can open a document in the files module
with Office 365 by right clicking on a file and choose :ref:`'Open with...' <files-open-with>`.

You can also host Office Online yourself and integrate it with Group-Office. Read more about that here:

https://docs.microsoft.com/en-us/officeonlineserver/office-online-server

LibreOffice Online
~~~~~~~~~~~~~~~~~~

.. figure:: /_static/using/files/collabora-online.png
   :alt: LibreOffice Online

   LibreOffice Online

With LibreOffice Online you can edit office documents in your browser. You need a working
LibreOffice Online server. More info on https://www.libreoffice.org/download/libreoffice-online/

For installing read the :ref:`LibreOffice online installation page. <libreoffice-online>`

.. _onlyoffice:

OnlyOffice
~~~~~~~~~~

.. figure:: /_static/using/files/onlyoffice.png
   :alt: OnlyOffice

   OnlyOffice

Run your private office with Group-Office and `OnlyOffice <https://www.onlyoffice.com>`__.

Designed to make collaboration easy. A complete productivity suite to run your entire business with.

Edit Text Documents, Spreadsheets and Presentations online in your browser.

For installing read the :ref:`OnlyOffice installation page. <onlyoffice-install>`

WebDAV
~~~~~~

You mount Group-Office as a network drive on your workstation.

For more information read the page: :ref:`connect-a-device`.
