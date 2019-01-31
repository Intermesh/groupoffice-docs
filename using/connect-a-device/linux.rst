Linux
=====

- Files
- Calendar
- Contacts
- E-mail

Thunderbird
-----------

You can use Thunerbird with the lightning extention to synchronize e-mail, contacts and
calendars with IMAP, CardDAV and CalDAV.

Walkthrough guide coming soon...

Files
-----

With the Group Office assistant you can edit files directly in Group Office. When 
you launch a file by double clicking it will automatically mount the webdav drive
and launch the default application on your computer.

   .. figure:: /_static/linux-assistant/1-groupoffice-assistant.png


On Debian based distributions you can install the Group Office Assistant.

1. First add our APT repository::

      echo "deb http://repo.group-office.com/ one main" | sudo tee /etc/apt/sources.list.d/groupoffice-assistant.list

2. Add our public key::

      gpg --keyserver pool.sks-keyservers.net --recv-keys 0758838B
      gpg --export --armor 0758838B | sudo apt-key add -

3. Update APT::

     sudo apt-get update

4. Then install Group Office Assistant by running::

     sudo apt-get install groupoffice-assistant

5. Now double click a file in Group Office and it can be edited on your desktop 
   instantly.
   


.. note: Due to a bug in Ubuntu you'll get this ignorable error:

   Error in file "/usr/share/applications/org.gnome.font-viewer.desktop": "font/ttf" is an invalid MIME type ("font" is an unregistered media type)


