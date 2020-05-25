.. _filters:

Custom filters
==============

Some modules support custom filters. You can create a reusable filter in which you create
your own conditions. They also work great together with :ref:`custom-fields`.

For example you've defined a custom field "Education" and you want to show all 
"Software engineers" you can easily do this with a custom filter.

Other useful examples:

- Find all upcoming birthdays
- Find all contacts with invoices with the "Has links to.." and then select invoice.
- Find contacts with recent comments

Here's a screenshot of the address book:

.. figure:: /_static/using/filters/filters.png
   :alt: Filters
   :width: 50%

   Filters

In the picture above you can see two custom filters called "Software engineers" and "Users".

Adding a filter
---------------

Click the add button in the filters toolbar to open the filter dialog.
Add your conditions and click "Save".
If you want to share this filter with other users you can add groups in the permissions tab.

.. figure:: /_static/using/filters/filter.png
   :alt: Filter
   :width: 100%

   Filter


Wildcards
`````````

You can use % to match 0 or more characters. or _ to match a single character.

There are already some wildcards applied automatically. When filtering on strings you can choose:

- Contains, will put a %..% before and after your phrase.
- Equals, will put use no wildcards
- Starts with, will put a ..% after your phrase.
- Ends with, will put a %.. before your phrase.


Sub groups
``````````
To create complex queries, Group-Office supports sub groups. You can use that to create a query for example:

Select all contacts that have job title "CEO" and work in Germany or the Netherlands. You would have to create a sub group
for the countries as they are using an "OR" operator.

It can also be used for inverting one of the queries. For example select all contacts that have job title "CEO" but do
NOT work in the Netherlands.

Click the "Add sub group" button to add one.