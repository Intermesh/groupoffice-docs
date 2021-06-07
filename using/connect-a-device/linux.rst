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

Thunderbird doesn't auto detect the CardDAV and CalDAV links automatically. You have to enter the complete URL's.

You can find those by using your browser and go to /carddav/addressbooks/<ADDRESSBOOK> or /caldav/calendars/<CALENDAR>

.. _assistant-for-linux:

Files
-----

The Group-Office Assistant is a small program that you can install on your Windows, MacOS or
Linux computer. It will automatically download files opened from Group-Office and monitor
it for changes. When the file is saved it automatically uploads it back to Group-Office.

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

.. note:: For Chrome users. You might be annoyed by the popup dialog everytime you open a file. Here's a solution for
   that: https://superuser.com/questions/1481851/disable-chrome-to-ask-for-confirmation-to-open-external-application-everytime
