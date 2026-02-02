.. _connect-to-linux:


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

Files - Group-Office Assistant
------------------------------

The Group-Office Assistant is a small program that you can install on your Windows, MacOS or
Linux computer. It will automatically download files opened from Group-Office and monitor
it for changes. When the file is saved it automatically uploads it back to Group-Office.

   .. figure:: /_static/linux-assistant/1-groupoffice-assistant.png


Debian / Ubuntu / Mint
~~~~~~~~~~~~~~~~~~~~~~

On Debian based distributions you can install the Group Office Assistant via our APT repository. Take the following steps:

1. First add our APT repository::

      echo "deb http://repo.group-office.com/ one main" | sudo tee /etc/apt/sources.list.d/groupoffice-assistant.list

2. Add our public key::

      wget -qO - https://repo.group-office.com/downloads/groupoffice.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/groupoffice.gpg

3. Update APT::

     sudo apt-get update

4. Then install Group Office Assistant by running::

     sudo apt-get install groupoffice-assistant

5. Now double click a file in Group Office and it can be edited on your desktop 
   instantly.

.. note:: For Chrome users. You might be annoyed by the popup dialog everytime you open a file. Here's a solution for
   that: https://superuser.com/questions/1481851/disable-chrome-to-ask-for-confirmation-to-open-external-application-everytime

Fedora RPM
~~~~~~~~~~

We also have an RPM package available here:

https://repo.group-office.com/downloads/groupoffice-assistant-1.1.36-1.x86_64.rpm

You can run this in the terminal to first download and then install it::

    wget https://repo.group-office.com/downloads/groupoffice-assistant-1.1.36-1.x86_64.rpm
    sudo rpm -i groupoffice-assistant-1.1.36-1.x86_64.rpm


WebDAV
------
You can use WebDAV to mount Group-Office as a network drive. Linux Desktops have WebDAV built in. GNOME users you can
launch the file explorer and choose "Connect to server" from the menu. KDE/Plasma users can use the Dolphin file
manager to connect to WebDAV.

Connect the client to:

https://[Server hostname]/webdav
