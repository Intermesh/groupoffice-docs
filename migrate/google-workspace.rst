Switch from Google Workspace to GroupOffice
============================================

You can take the following steps to migrate all your data from Google Workspace to GroupOffice.

Assessment & Prerequisites
-----------------------------

Determine what you need to migrate. The data can be mapped like this:

=================  ============
Google Workspace   GroupOffice
=================  ============
Gmail              E-mail (You need to install the GroupOffice mailserver or another IMAP server)
Drive              Files
Calendar           Calendar
Contacts           Addressbook
=================  ============

Make sure you have the required modules installed. To replace the google docs editors you can install :ref:`Collabora office <collabora-office>`.

Sign up or install
------------------

Decide if you want to self host GroupOffice or use our cloud service.
`You can sign up here <https://www.group-office.com/get-started>`_.

Users
-----

Before creating users, :ref:`setup groups and module permissions <user-groups>`.

Start by creating users manually or :ref:`import them via a csv or file <user-import-export>` in GroupOffice.
`Here you can find how to export Google Workspace users <https://support.google.com/a/answer/7348070>`_.

.. note:: Also consider if you want to use an :ref:`SSO solution with OpenID connect<oauth2>`, :ref:`IMAP authentication <map-authentication>` or :ref:`LDAP authentication <ldap>`.


Gmail
-----

When migrating mail we use `imapsync <https://imapsync.lamiral.info/>`.

The steps to take are:

1. Setup mailserver

   a. When self hosting then install the :ref:`GroupOffice mailserver <mailserver>` or use any IMAP compliant server.
   b. When using our cloud service and you have signed up for a mail domain you will get access to the management where you
      can create mailboxes

2. Prepare your domain. Do not switch yet but determine all DNS records (MX, SPF, DMARC and DKIM) to set after migrating mail. For our cloud service we will
   provide them to you.

3. Create all the mailboxes on the GroupOffice mailserver

4. Create a list of imapsync commands using the `imapsync documentation <https://imapsync.lamiral.info/>`_. Also read the google specific parts.

5. Run the sync and test. You can repeat the sync at any time to update the new mailserver.

6. Put the migration live by setting the DNS domains.

7. Finally, run the sync again after 24 hours because some mail might still have arrived at Google.


Calendar
--------

Migrating calendars goes via export and import of vcalendar (\*.ics) files. `Learn how to export your Google calendars here.
<https://support.google.com/calendar/answer/37111?hl=en>`_ and take these steps:

1. Export all required calendars in Google Workpace
2. Create all required calendars in GroupOffice. All created users in GroupOffice should have a personal calender when they have access to the calendar module.
3. :ref:`Import all vcalendar files <calendar-import-export>`.


Contacts
--------

Migrating contacts goes via export and import of vCard (\*.vcf) files. `Learn how to export your Google Contacts here.
<https://support.google.com/contacts/answer/7199294>`_ and take these steps:

1. Export all contacts to vCard (*.vcf) file
2. Create all required addressbooks in GroupOffice.
3. :ref:`Import all vCard files <addressbook-import-export>`.


Drive
-----

Files can be migrated by uploading them manually or you could use `rclone <https://rclone.org>`_` to migrate from Google Drive to Webdav.
Please consult the rclone documentation and take these steps:


1. Setup GroupOffice Webdav by installing the module.
2. Install rclone
3. Add the Google drive remote
4. Add the Webdav remote
5. Use the rclone sync command
