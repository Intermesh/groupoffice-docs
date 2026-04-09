Switch from Microsoft Office 365 to GroupOffice
================================================

You can take the following steps to migrate all your data from Microsoft Office 365 to GroupOffice.

Assessment & Prerequisites
-----------------------------

Determine what you need to migrate. The data can be mapped like this:

====================  ============
Microsoft Office 365  GroupOffice
====================  ============
Mail                  E-mail (You need to install the GroupOffice mailserver or another IMAP server)
OneDrive              Files
Calendar              Calendar
Contacts              Addressbook
====================  ============

Make sure you have the required modules installed. To replace the office apps you can install :ref:`Collabora office <collabora-office>`.

Sign up or install
------------------

Decide if you want to self host GroupOffice or use our cloud service.
`You can sign up here <https://www.group-office.com/get-started>`_.

Users
-----

Before creating users, :ref:`setup groups and module permissions <user-groups>`.

Start by creating users manually or :ref:`import them via a csv or file <user-import-export>` in GroupOffice.
`Here you can find how to export Microsoft Office 365 users <https://learn.microsoft.com/en-us/answers/questions/4910422/how-do-i-create-a-report-of-365-users-with-their-e>`_.

.. note:: Also consider if you want to use an :ref:`SSO solution with OpenID connect<oauth2>`, :ref:`IMAP authentication <map-authentication>` or or :ref:`LDAP authentication <ldap>`.


E-mail
------

When migrating mail we use `imapsync <https://imapsync.lamiral.info/>`.

The steps to take are:

1. Setup mailserver

   a. When self hosting then install the :ref:`GroupOffice mailserver <mailserver>` or use any IMAP compliant server.
   b. When using our cloud service and you have signed up for a mail domain you will get access to the management where you
      can create mailboxes

2. Prepare your domain. Do not switch yet but determine all DNS records (MX, SPF, DMARC and DKIM) to set after migrating mail. For our cloud service we will
   provide them to you.

3. Create all the mailboxes on the GroupOffice mailserver

4. Create a list of imapsync commands using the `imapsync documentation <https://imapsync.lamiral.info/>`_. Also read the Microsoft specific parts.

5. Run the sync and test. You can repeat the sync at any time to update the new mailserver.

6. Put the migration live by setting the DNS domains.

7. Finally, run the sync again after 24 hours because some mail might still have arrived at Microsoft.


Calendar
--------

Migrating calendars goes via export and import of vcalendar (\*.ics) files.

To get an ics file from Microsoft Office 365 you need to `publish your calendar <https://support.microsoft.com/en-us/office/share-your-calendar-in-outlook-com-0fc1cb48-569d-4d1e-ac20-5a9b3f5e6ff2>`_
 and download that link. Afterwards you can unpublish it.

Take these steps:

1. Export all required calendars by publishing and downloading them.
2. Create all required calendars in GroupOffice. All created users in GroupOffice should have a personal calender when they have access to the calendar module.
3. :ref:`Import all vcalendar files <calendar-import-export>`.


Contacts
--------

Migrating contacts goes via export and import of vCard (\*.vcf) files. `Learn how to export your Outlook Contacts here.
<https://support.microsoft.com/en-us/office/import-or-export-contacts-in-outlook-using-a-csv-file-bb796340-b58a-46c1-90c7-b549b8f3c5f8>`_ and take these steps:

1. Export all contacts to vCard (\*.vcf) file
2. Create all required addressbooks in GroupOffice.
3. :ref:`Import all vCard files <addressbook-import-export>`.


OneDrive
--------

Files can be migrated by uploading them manually or you could use `rclone <https://rclone.org>`_` to migrate from Microsoft OneDrive to GroupOffice Webdav.
Please consult the rclone documentation and take these steps:

1. Setup GroupOffice Webdav by installing the module.
2. Install rclone
3. Add the Microsoft OneDrive remote
4. Add the Webdav remote
5. Use the rclone sync command
