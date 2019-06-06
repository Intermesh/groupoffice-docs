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

Sharing an address book
-----------------------

Via the more menu you in the tree you can edit an address book. Read more about :ref:`sharing here <sharing>`.

Import and export
-----------------

You can import and export a Comma Separated File (*.csv) or a vcard (*.vcf).

These functions are accessible via the more menu in the toolbar above the grid:

.. figure:: /_static/using/address-book/import-export.png
   :alt: Import and export menu options
   :width: 100%

   Import and export menu options

Groups
------

Each address books can have groups. They're useful for organizing your address book.

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

Or::

   age: > 30 age: < 40

Will show all contacts with an age between 30 and 40.


Or::

   birthday:  < 1 months

Will show all contacts with a birthday coming up within one month.

You can use these fields:

- name
- email
- phone
- created (date)
- modified (date)
- age (number)
- gender (M, F or null)
- birthday (date)
- isuser (0 or 1)
- :ref:`custom-fields`