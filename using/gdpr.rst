.. _gdpr:

Privacy tools
=============

Group-Office is written to be privacy-friendly. This module is a tool to ensure the privacy of our users' customer data.
This will make it easier for our users to be GDPR compliant.

GDPR
----

The `GDPR <https://en.wikipedia.org/wiki/General_Data_Protection_Regulation>`_ is a European regulation on information
privacy. Therefore, this module is mostly aimed at our customers within the EU. That being said, if you are in another
region with privacy regulations, or you care about the privacy of your customers, this module may be helpful as well.

Prerequisites
-------------

Customer data is mostly managed in the address book module and is therefore dependent on the addressbook module. You need
a professional license to use the GDPR module.

Installation
------------

You can find the Privacy tools :ref:`module <modules>` in the Business package.

Configuration
-------------

Upon installation, the following things are automatically added to Group-Office:

1. A cron job that moves stale contacts to a 'Trash' address book;
2. An 'Incoming' address book that is monitored by default;
3. A 'Trash' address book that allows the administrator to review cleaned up contacts.
4. Default settings for this module.

You can fine tune the configuration by navigating to the "Privacy Settings" tab in the system settings. Configuration
options are:

- **Inactivity period**: Number of days before a contact is marked as stale and moved to the Trash.
- **Warning period**: If set, warn this number of days prior to moving a contact to trash.
- **Address books**: Here you can set the address books that you wish to monitor for stale contacts. By default, this is the 'Incoming' address book.
- **Trash address book**: This is the address book that stale contacts are being moved to.

Using the Privacy tools module
------------------------------

Upon creating a new contact, it is automatically saved into the 'Incoming' address book. It is up to the end user to
either leave the contact as is, which will remove the contact automatically, or move it to another address book.

Alternatively, one can manually set a deletion date for a contact. In the contact dialog, a tab is available labeled
'Privacy Options'. Set the deletion date there and the contact will be moved to 'Trash' on the configured date.


Emptying the Trash
``````````````````

If a user is set as an administrator, they can empty the trash easily. Go to the address book module and open the
'Trash' address book. A button labeled 'Empty trash' will be available. Click the button and confirm your decision.