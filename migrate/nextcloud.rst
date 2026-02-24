Switch from Nextcloud to GroupOffice
=====================================

You can take the following steps to migrate all your data from Nextcloud to GroupOffice.

Assessment & Prerequisites
-----------------------------

Determine what you need to migrate. The data can be mapped like this:

====================  ============
Nextcloud             GroupOffice
====================  ============
Mail                  E-mail (You need to install the GroupOffice mailserver or another IMAP server)
Files                 Files
Calendar              Calendar
Contacts              Addressbook
====================  ============

Make sure you have the required modules installed. To replace the Nextcloud office you can install :ref:`Collabora office <collabora-office>`.

Sign up or install
------------------

Decide if you want to self host GroupOffice or use our cloud service.
`You can sign up here <https://www.group-office.com/get-started>`_.

Users
-----

Before creating users, :ref:`setup groups and module permissions <user-groups>`.

Start by creating users manually or :ref:`import them via a csv or file <user-import-export>` in GroupOffice.
`Here you can find how to export Nextcloud users <https://apps.nextcloud.com/apps/user_migration>`_.

.. note:: Also consider if you want to use an :ref:`SSO solution with OpenID connect<oauth2>`, :ref:`IMAP authentication <map-authentication>` or or :ref:`LDAP authentication <ldap>`.


E-mail
------

Nextcloud uses similar technology for the mailserver. You could let GroupOffice connect to the same IMAP server. Alternatively
you can migrate the mail using imapsync.

When migrating mail we use `imapsync <https://imapsync.lamiral.info/>`.

The steps to take are:

1. Setup mailserver

   a. When self hosting then install the :ref:`GroupOffice mailserver <mailserver>` or use any IMAP compliant server.
   b. When using our cloud service and you have signed up for a mail domain you will get access to the management where you
      can create mailboxes

2. Prepare your domain. Do not switch yet but determine all DNS records (MX, SPF, DMARC and DKIM) to set after migrating mail. For our cloud service we will
   provide them to you.

3. Create all the mailboxes on the GroupOffice mailserver

4. Create a list of imapsync commands using the `imapsync documentation <https://imapsync.lamiral.info/>`_.

5. Run the sync and test. You can repeat the sync at any time to update the new mailserver.

6. Put the migration live by setting the DNS domains.

7. Finally, run the sync again after 24 hours because some mail might still have arrived at the old mailserver.


Calendar
--------

Migrating calendars goes via export and import of vcalendar (*.ics) files.

To get an ics file from Nextcloud you need to `publish your calendar <https://docs.nextcloud.com/server/latest/user_manual/en/groupware/calendar.html#publishing-a-calendar>`_
 and download that link. Afterwards you can unpublish it.

Take these steps:

1. Export all required calendars by publishing and downloading them.
2. Create all required calendars in GroupOffice. All created users in GroupOffice should have a personal calender when they have access to the calendar module.
3. :ref:`Import all vcalendar files <calendar-import-export>`.


Contacts
--------

Migrating contacts goes via export and import of vCard (*.vcf) files. To download your contacts from the Nextcloud Contacts apps
 click on the **settings** (gear icon) and go to **Address books** in the settings screen. `From the more options menu choose
 **Download** <https://docs.nextcloud.com/server/25/user_manual/en/groupware/contacts.html#adding-and-managing-address-books>`_. and take these steps:

1. Export all contacts to vCard (*.vcf) file
2. Create all required address books in GroupOffice.
3. :ref:`Import all vCard files <addressbook-import-export>`.


Files
-----

Files can be migrated by uploading them manually or you could use `rclone <https://rclone.org>`_` to migrate from Nextcloud to Webdav.
Please consult the rclone documentation and take these steps:

1. Setup GroupOffice Webdav by installing the module.
2. Install rclone
3. Add the Nextcloud webdav remote
4. Add the GroupOffice Webdav remote
5. Use the rclone sync command
