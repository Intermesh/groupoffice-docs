Switch to Group-Office from other software
==========================================

You can take the following steps to migrate all your data from other software to Group-Office.

Assessment & Prerequisites
-----------------------------

Determine what you need to migrate. For example, e-mail, contacts, files and calendars. Install the required modules.

Sign up or install
------------------

Decide if you want to self host Group-Office or use our cloud service.
`You can sign up here <https://www.group-office.com/get-started>`_.

Users
-----

Before creating users, :ref:`setup groups and module permissions <user-groups>`.

Start by creating users manually or :ref:`import them via a csv or file <user-import-export>` in Group-Office.
Find out how you can export users from your current software.

.. note:: Also consider if you want to use an :ref:`SSO solution with OpenID connect<oauth2>`, :ref:`IMAP authentication <map-authentication>` or or :ref:`LDAP authentication <ldap>`.


E-mail
------

Ideally you can migrate mail from your current software via IMAP. Find out if IMAP is supported.
If so, you can migrate the mail using imapsync.

When migrating mail we use `imapsync <https://imapsync.lamiral.info/>`.

The steps to take are:

1. Setup mailserver

   a. When self hosting then install the :ref:`Group-Office mailserver <mailserver>` or use any IMAP compliant server.
   b. When using our cloud service and you have signed up for a mail domain you will get access to the management where you
      can create mailboxes

2. Prepare your domain. Do not switch yet but determine all DNS records (MX, SPF, DMARC and DKIM) to set after migrating mail. For our cloud service we will
   provide them to you.

3. Create all the mailboxes on the Group-Office mailserver

4. Create a list of imapsync commands using the `imapsync documentation <https://imapsync.lamiral.info/>`_.

5. Run the sync and test. You can repeat the sync at any time to update the new mailserver.

6. Put the migration live by setting the DNS domains.

7. Finally, run the sync again after 24 hours because some mail might still have arrived at the old mailserver.


Calendar
--------

Migrating calendars goes via export and import of vcalendar (*.ics) files. Take these steps:

1. Find out how to export all required calendars to vcalendar (*.ics) files.
2. Create all required calendars in Group-Office. All created users in Group-Office should have a personal calender when they have access to the calendar module.
3. :ref:`Import all vcalendar files <calendar-import-export>`.


Contacts
--------

Migrating contacts goes via export and import of vCard (*.vcf) files Take these steps:

1. Find out how to export all required contacts to vCard to vCard (*.vcf) file(s).
2. Create all required address books in Group-Office.
3. :ref:`Import all vCard files <addressbook-import-export>`.


Files
-----

Files can be migrated by uploading them manually or you could use `rclone <https://rclone.org>`_` to migrate from your current software to Webdav.
Please consult the rclone documentation and take these steps:

1. Setup Group-Office Webdav by installing the module.
2. Install rclone
3. Add the old webdav remote
4. Add the Group-Office Webdav remote
5. Use the rclone sync command
