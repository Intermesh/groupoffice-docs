Address book
============

.. figure:: /_static/using/address-book/address-book.png
   :alt: Address book
   :width: 100%

   Address book

The address book is a very powerful tool to manage contacts and organizations. It's easy to share address books with other users.

The address book module supports:

- :ref:`filters`
- :ref:`links`
- :ref:`custom-fields`
- :ref:`comments`
- :ref:`sharing`
- :ref:`files`

.. _sharing-addressbook:

Sharing an address book
-----------------------

Via the more menu you in the tree you can edit an address book. Read more about :ref:`sharing here <sharing>`.

.. _addressbook-import-export:

Import and export
-----------------

You can import and export a Comma Separated File (*.csv) or a vcard (*.vcf).
The export functions will export what's currently selected on screen. So you can first apply searches or filters and then
choose export.

These functions are accessible via the more menu in the toolbar above the grid:

.. figure:: /_static/using/address-book/import-export.png
   :alt: Import and export menu options
   :width: 100%

   Import and export menu options

VCF format
``````````

VCF or vCard format is the easiest to use. You don't need to map any fields because it's already defined in the standard.

:download:`You can download and example VCF file here. </_static/using/address-book/john-van-doe.vcf>`

CSV format
``````````

Any format can be imported as long as the required columns are available.
After selecting the file a dialog will be opened where you can match the fields:

.. figure:: /_static/using/address-book/import-csv.png
   :alt: Import CSV dialog
   :width: 50%

   Import CSV dialog

When the column names match the name of the Group-Office field name or label it will 
be mapped automatically. It also recognized other common names and the Outlook format.

The best approach for importing would be:

1. Setup your custom fields
2. Create a dummy contact in Group-Office with everything filled in.
3. Export this contact to CSV so you have an example template.
4. Fill this CSV with data
5. Import it.

:download:`You can download and example CSV file here. </_static/using/address-book/john-van-doe.csv>`

Updating existing contacts
~~~~~~~~~~~~~~~~~~~~~~~~~~

It's possible to bulk update your Group-Office contacts with a CSV file. After uploading your CSV you'll get a mapping
dialog. In the first combo box you can select: "Update existing items by" where you can select "ID" or "E-mail". When
selecting the "ID" for example it will update all Group-Office contacts with a matching "ID" in the CSV record.

Labels
``````
You can easily print labels for envelopes. You can enter the rows, columns and margins and generate a PDF to print labels.

.. figure:: /_static/using/address-book/labels.png
   :alt: Print labels
   :width: 100%

   Print labels

In the template you can use the new :ref:`template syntax <templates>` that's also used in the Newsletters module.

Groups
------

Each address books can have groups. They're useful for organizing your address book. You can add a contact to a group by
dragging that contact onto a group in the contact list.

Advanced search syntax
----------------------

Next to :ref:`filters` you can also use an advanced search syntax in the address book search bar.

.. figure:: /_static/using/address-book/advanced-query-syntax.png
   :alt: Advanced query syntax
   :width: 50%

   Advanced query syntax

If you enter a string of text it will search through the name and debtor number fields by default.
But you can also search on other fields. For example::

   modified: > -1 week

Will show all contacts that have been modified in the past week. 

Ranges are also supported for date filters::

   modified: last week..now

Or::

   age: > 30 age: < 40

Will show all contacts with an age between 30 and 40.


Or::

   birthday:  < 1 months

Will show all contacts with a birthday coming up within one month.

Or::

   org:  intermesh,group-office
   
Will show all employees of the organizations Intermesh and Group-Office

You can use these fields:

- name
- email
- phone
- org (Organization name)
- createdat (date)
- createdby (User's display name)
- modifiedat (date)
- modifiedby (User's display name)
- commentedat (date)
- age (number)
- gender (M, F or null)
- birthday (date)
- isuser (0 or 1)
- :ref:`custom-fields` By using <databaseName>: query. Lookup the database name in system settings.


String search explained
```````````````````````

For example when searching for::

   name: John Jacks

It will find anything with name "John Jacks". 
   
If you want to search for every contact with a name starting with an 's' you can search for::

   name: "s%"


Look for duplicates
-------------------

It often occurs that duplicate contacts are created. Group-Office has a feature to deduplicate contacts.

In the more menu choose "Look for duplicates":

.. figure:: /_static/using/address-book/look-for-duplicates-menu.png
   :alt: Look for duplicates menu
   :width: 300px

   Look for duplicates menu


The following dialog will open:

.. figure:: /_static/using/address-book/look-for-duplicates-dialog.png
   :alt: Look for duplicates dialog
   :width: 100%

   Look for duplicates dialog

Here you can choose the properties that should match to find duplicates. You can then select one or more records and
choose "Merge selected".

All links, comments, files etc. will be merged into the first selected record. The other records will be removed.


System settings
---------------

In the System Settings dialog, you can set the following parameters:

-  Create a personal address book for each user, by default each user will get his own private address book. For some
   organizations this is not desirable. You can disable it and delete the private address books afterwards.
-  Automatically :ref:`link<links>` email conversations to users in selected address books. Only available if the
   "Save mail as" professional module is installed. Note that this will create a copy of each mail from the IMAP server
   to the Group-Office storage. You can blacklist or whitelist certain address books from automatically linking emails to the contacts. Please note
   that this will eat a lot of disk space over time.

User profile
````````````

Users can set their default address book. 

Additionally, they can set which address books to show when initially opening address books:

  - All contacts - Just show all contacts regardless of address book;
  - Starred - Only show starred contacts;
  - Default - Open the default address book;
  - Last selected - Open the address book you opened last time. Will fall back on the default address book;