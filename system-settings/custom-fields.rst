.. _custom-fields:

Custom fields
=============

Every organization is different and has different data to store. That's why most 
entities in Group-Office can be extended with custom fields.

Custom fields show in the:

- Edit dialogs
- Detail views
- Grid columns
- Advanced search and filters

You can create custom fields via System settings at:

- Notes
- Address book
- Billing
- Projects
- Tickets
- Calendar
- Tasks
- Files
- ... and many more!

.. note:: The above list depends on the modules installed. You may have less or
   more options.

Creating and editing fields
---------------------------

Navigate to System settings -> Custom fields. You'll see a list of customizable entities
and their corresponding modules.

.. figure:: /_static/system-settings/custom-fields-window.png

   Custom fields overview window

Click on the pencil icon in the right column to manage custom fields for a certain object. For
an non-customized object, the resulting window wll look like below:

.. figure:: /_static/system-settings/custom-fields-add-empty.png

   Custom fields for a non-customized object

Click the + icon to add a field set first. A field set is a group of fields that 
has a title and an optional description that will be shown on the form.
You can also hide field set in some cases. This depends on the module. In the 
address book you can only show it on certain address books for example.

When you've created a field set you can add a field via the '+' button on the 
field set row:

.. figure:: /_static/system-settings/custom-fields-add-fieldset.png

  Add custom field set

The image below shows the custom field types you can add.

.. figure:: /_static/system-settings/custom-fields-add-field.png
   :width: 200px

   Custom field types

.. note:: The types of custom fields that you can add depend on the modules you
   have installed.

Depending on the type of custom field, you have a plethora of options for your customization. For instance, you can
conditionally require and/or hide a field:

.. figure:: /_static/system-settings/custom-fields-add-text-field-example.png

   Example text fields with extra conditions

The custom field will show in the:

.. figure:: /_static/system-settings/custom-fields-form.png

   Example edit dialog. Please note the separate tab

.. figure:: /_static/system-settings/custom-fields-detail.png

   Detail view

.. figure:: /_static/system-settings/custom-fields-grid.png

   Toggle custom fields in grid columns


Filters
-------

Aside from displaying and storing data, it is a breeze to filter items by custom field values. In the left column,
near the Filters header, click on the + and select Filter:

.. figure:: /_static/system-settings/custom-fields-filter.png

   An example filter


Conditionally required fields
-----------------------------

It's possible to make fields required based on one or more simple conditions. You can also hide the field if the condition does not match.

For example you could create a checkbox called "provideDetails" and create a text field "details" with a condition 'provideDetails = true'.
The result will be that when you check the box the provideDetails field will be shown and made required.

The condition syntax is very simple::

    <fieldName> <operator> <value>

Where:

- fieldName can be any property or custom field
- operator can be: =, !=, >, >=, <, <=
- value is a string without quotes. For checkboxes you can use 0,1 or true or false.
- multiple conditions can be combined with either AND or OR.
- Grouping is also possible since 6.4.219. eg. <fieldName1> is true AND (<fieldName2> = test OR <fieldName2> = 1234)

.. warning:: The fieldName, operator and value must be separated by spaces.


Template field
--------------

The template field can render data using :ref:`templates`.

The template holds the "entity" model as variable. Which is the entity the custom field belongs too.

You can for example take the first linked contact and store it's name::

    [assign firstContactLink = entity | links:Contact | first]
    {{firstContactLink.name}}

Or store the postal code of the first linked contact::

    [assign firstContactLink = entity | links:Contact | first]
    [assign address = firstContactLink.addresses | first]{{address.zipCode}}

Or if you want addresses of the contact in the grid you could create a field with this template::

    {{entity.addresses | column:formatted| implode}}

