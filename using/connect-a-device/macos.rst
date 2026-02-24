MacOS
=====

On Mac OS you can synchronize:

- Files
- Calendar
- Contacts
- E-mail

.. _assistant-for-macos:

Files - GroupOffice Assistant
------------------------------

The GroupOffice Assistant is a small program that you can install on your Windows, MacOS or
Linux computer. It will automatically download files opened from GroupOffice and monitor
it for changes. When the file is saved it automatically uploads it back to GroupOffice.

Download the GroupOffice Assistant for:

- `MacOS (Sillicon) <https://repo.group-office.com/downloads/group-office-assistant-macos-aarch64.dmg>`_.
- `MacOS (Intel) <https://repo.group-office.com/downloads/group-office-assistant-macos-x64.dmg>`_.

After downloading take the following steps to install:

1. Open the DMG file and drag "GroupOffice Assistant" in the "Applications" folder.

   .. figure:: /_static/macos-assistant/1-dmg.png
      :width: 400px

2. In GroupOffice right click on a file and choose "Open with".

3. Select the "Your desktop application (WebDAV) option to use the assistant.

   .. figure:: /_static/macos-assistant/4-select-application.png
      :width: 400px


.. note:: For Chrome users. You might be annoyed by the popup dialog everytime you open a file. Here's a solution for
   that: https://superuser.com/questions/1481851/disable-chrome-to-ask-for-confirmation-to-open-external-application-everytime

WebDAV clients
``````````````
You can use WebDAV to mount GroupOffice as a network drive. Unfortunately the MacOS webdav implementation can be rather
slow due to a lot of redundant requests.
We found that the `Mountain Duck WebDAV client <https://mountainduck.io>`_ is much faster. Additionally, it has
a smart synchronisation feature to work with your files offline. Connect the client to:

\https://[:ref:`server-hostname`]/webdav

Calendar, Reminders and Contacts
--------------------------------

Adding contacts and calendar accounts work identically in MacOS. Just choose 
"CalDAV" for calendars and "CardDAV" for contacts.

1. Open System Preferences and click "Internet Accounts".

   .. figure:: /_static/macos/1-system-preferences.png
      :width: 400px

2. Click the "+" button in the bottom left to add an account. Scroll down and choose "Other account".

   .. figure:: /_static/macos/2-internet-accounts.png
      :width: 400px

3. Now choose "CalDAV" for calendars or "CardDAV" for contacts.

   .. figure:: /_static/macos-caldav/3-caldav-account.png
      :width: 400px

4. Select "Manual" in the "Account Type" dropdown and enter the username, password and :ref:`server-hostname`.

   .. figure:: /_static/macos-caldav/4-add-caldav-account.png
      :width: 400px

   .. note:: On some servers the auto detection fails. In that case you can try to set the type to advanced and add this
      path (The trailing / is important here)::

         /caldav/principals/<YOURUSERNAME>/

5. Click "Sign in" to finish and you might be able to select additional data sources in the account settings screen.

   .. figure:: /_static/macos-caldav/5-account-settings.png
      :width: 400px

6. Now check your Calendar or Contact app for your GroupOffice data!

.. note:: Unfortunately the Contacts app on MacOS will only sync the first address book in CardDAV.

E-mail
------

E-mail on MacOS works with IMAP and SMTP. These settings vary between providers so please ask your
system administrator for the right IMAP and SMTP settings.

Intermesh uses:

+-----------------------------+-----------------------------------+
| Username                    | E-mail address                    |
+-----------------------------+-----------------------------------+
| Password                    | GroupOffice password             |
+-----------------------------+-----------------------------------+
| Incoming mail server (IMAP) | imap.group-office.com on port 143 |
+-----------------------------+-----------------------------------+
| Outgoing mail server (SMTP) | smtp.group-office.com on port 587 |
+-----------------------------+-----------------------------------+
| Encryption                  | TLS Encryption for both servers   |
+-----------------------------+-----------------------------------+

To add a mail account take the following steps:

1. Open System Preferences and click "Internet Accounts".

   .. figure:: /_static/macos/1-system-preferences.png
      :width: 400px

2. Click the "+" button in the bottom left to add an account. Scroll down and choose "Other account".

   .. figure:: /_static/macos/2-internet-accounts.png
      :width: 400px

3. Click on "Mail account".

   .. figure:: /_static/macos-mail/1-mail-account.png
      :width: 400px

4. Enter your e-mail address and password and click "Sign in".

   .. figure:: /_static/macos-mail/2-add-mail-account.png
      :width: 400px

5. If auto discovery fails enter the server addresses and click "Sign in".

   .. figure:: /_static/macos-mail/3-server-addresses.png
      :width: 400px

6. Select the apps you'd like to synchronize and click "Done".

   .. figure:: /_static/macos-mail/4-select-apps.png
      :width: 400px

7. Check your mail!
