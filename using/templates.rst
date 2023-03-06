.. _templates:

Templates
=========

Group-Office has a flexible template system supporting variables with filters and structural blocks.
They are used for newsletters, reports, invoice templates etc.

.. _template_syntax:

Syntax
------

Variables
`````````
By default some variables are already present:

 - {{now|date:Y-m-d}} The current date time object. In this example a date filter is used.
 - {{system.title}} The title configured at System Settings -> General
 - {{system.url}} The URL to Group-Office configured at System Settings -> General

A variable is written like this::

   {{contact.name}}

Custom fields
~~~~~~~~~~~~~
A custom field can be accessed like this::

   {{contact.customFields.<DATABASE_NAME_OF_CUSTOMFIELD>}}

Some custom fields are stored with an ID. Like a select field for example. You can get the text like this::

   {{contact.customFields.asText.<DATABASE_NAME_OF_CUSTOMFIELD>}}

Arrays
~~~~~~
Arrays can be written like this::

  {{contact.emailAddresses[0].email}}

You can also iterate arrays using an [each] block::

   [each address in contact.addresses]
     [if {{address.type}} == "billing"]
       {{address.formatted}}
     [/if]
   [/each]

And filter arrays by property and only write first match using "eachIndex"::

    [each emailAddress in contact.emailAddresses | filter:type:"billing"]
        [if {{eachIndex}} == 1]
            {{emailAddress.email}}
        [/if]
    [/each]

Assign
~~~~~~
But this is probably the best way to handle the case where you prefer a type of address but just use the first if that's
not found. It uses [assign] to create a new variable. If it's empty it will use the first address::

  [assign address = contact.addresses | filter:type:"postal" | first]
  [if !{{address}}]
  [assign address = contact.addresses | first]
  [/if]
  {{address.formatted}}

Finding a contact with id = 1 using the "entity" filter with parameter "Contact" (Available entities in your instance can be found in the core_entity database table)::

    [assign contact = 1 | entity:Contact]
    {{contact.name}}

Find the first linked contact::

    [assign firstContactLink = someEntityVar | links:Contact | first]
    {{firstContactLink.name}}


Using [assign] to do some basic math

Note that inside the [each] block we access total with parent.total::

    [assign total = 0]

    [each invoice in invoices]
     <tr>
       <td>{{invoice.number}}</td>
       <td>{{invoice.date|date:d-m-Y}}</td>
       <td>{{invoice.expiresAt|date:d-m-Y}}</td>
       <td align="right">{{business.finance.currency}} {{invoice.totalPrice|number}}</td>
       <td align="right">{{business.finance.currency}} {{invoice.paidAmount|number}}</td>
       [assign balance = {{invoice.totalPrice}} - {{invoice.paidAmount}} ]
       [assign parent.total = {{parent.total}} + {{balance}}]
       <td align="right">{{business.finance.currency}} {{balance|number}}</td>
     </tr>
    [/each]

    {{business.finance.currency}} {{total|number}}


More examples
~~~~~~~~~~~~~
An advanced example for printing a custom salutation (Just an example. You can use {{contact.salutation}})::

   Dear [if {{contact.prefixes}}]{{contact.prefixes}}[else][if !{{contact.gender}}]Ms./Mr.[else][if {{contact.gender}}=="M"]Mr.[else]Ms.[/if][/if][/if] {{contact.lastName}}


A simple example template::

   Hi {{contact.salutation}},


   Best regards,

   {{creator.displayName}}
   {{creator.profile.organizations[0].name}}
   {{creator.profile.phoneNumbers[0].number}}



Filters
~~~~~~~

You can use filters to format data. They can be used with a "|" char followed by the filter name. Optionally the filter can take arguments separated by a ":".

- date(format as in PHP)::

  {{contact.dates[0].date|date:d-m-Y}}


- number(decimals,decimal separator,thousands separator::

   {{contact.customFields.number|number:2:,:.}}

- multiply(multiplier)
- add(number)
- entity(type, id): Fetch an entity::

        [assign contact = 1 | entity:Contact]

- links(entityName, properties (comma separated): gets the linked entities::

    [assign firstContactLink = someEntityVar | links:Contact | first]

- prop(property) get the propery name
- nl2br: Change line breaks to HTML <br> tags
- empty: returns true if empty or false if not

Arrays
++++++

- filter(property, value): Filters the array by property values::

    {{contact.addresses | filter:type:"postal" | first}}

- sort(property, value?) or rsort::

    [assign formattedAddress = contact.addresses | sort:type:"postal" | first | prop:formatted]
    {{formattedAddress}}

- count
- first: Grab the first item of the array
- prop(property): change the array to a sub property of all items.
- implode(glue = ', '): Implode an array of strings::

    {{contact.emailAddresses | prop:email | implode}}





