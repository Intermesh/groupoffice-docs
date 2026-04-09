.. _templates:

Templates
=========

GroupOffice has a flexible template system supporting variables with filters and structural blocks.
They are used for newsletters, reports, invoice templates etc.

.. _template_syntax:

Syntax
------

Variable instantiations
```````````````````````

Assign
~~~~~~

Our templating has very rudimentary variable assignment::

  [assign mainFile = {{entity.files | first}}]



Configuration
~~~~~~~~~~~~~

If you work with PDF templates that are not in the main langugage, you can configure a number of formatting settings::

  [config thousandsSeparator=.]
  [config decimalSeparator=,]

Currently, the configurable settings and their default values are:

- ``decimals`` (``2``)
- ``decimalSeparator`` (``.``)
- ``thousandsSeparator`` (``,``)
- ``dateFormat`` (``d-m-Y``)

Control flows
`````````````

Out of the box, two types of control flows are supported. Keywords and conditions must be surrounded by square brackets.

If - else
~~~~~~~~~

A typical if-statement looks like this::

  [if {{entity.field}} == "<VALUE>"]
    <!-- Do something -->
  [/if]

You can optianally fall back on a default with {{[else]}}::

  [if {{entity.field}} == "<VALUE>"]
    <!-- Do something -->
  [else]
    <!-- Do something else -->
  [/fi]

Each in
~~~~~~~

Iterations are handled in each-loops, e.g.::

  [each file in entity.files]
    <!-- do something with file -->
  [/each]

The index of the array you are iterating through can be used or manipulated as well with the ``{{eachIndex}}`` variable::

  <ul>
  [each file in entity.files]
    <li>{{eachIndex}}: {{file.name}}</li>
  [/each]
  </ul>

Variables
`````````
By default some variables are already present:

 - ``{{now|date:Y-m-d}}`` The current date time object. In this example a date filter is used.
 - ``{{system.title}}`` The title configured at System Settings -> General
 - ``{{system.url}}`` The URL to GroupOffice configured at System Settings -> General
 - ``{{:pnp:}}`` The current page number
 - ``{{:ptp:}}`` The total number of pages


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
   {{creator.profile.jobTitle}}
   {{creator.profile.organizations[0].name}}
   {{creator.profile.phoneNumbers | first | prop:number}}


Attachment field with photo's in e-mail template::

    [each photo in contact.customFields.Photos]
    <h3>{{photo.name}}</h3>
    <img src="{{photo.blobId|blobUrl}}" alt="{{photo.name|htmlEncode}}" style="max-width:100%"><hr>
    [/each]

Or photo's from the entity's files folder::

    [each photo in document|entityFiles]
    <h3>{{photo.name}}</h3>
    <img src="{{photo.blobId|blobUrl}}" alt="{{photo.name|htmlEncode}}" style="max-width:100%"><hr>
    [/each]

.. note::
  In PDF templates, use the ``{{blobPath}}`` filter if the ``{{blobUrl}}`` filter does not display an image file.

Filters
```````

You can use filters to format or manipulate data. They can be used with a pipe sign (``|``) followed by the filter name. Optionally the filter can take arguments separated by a ``:``.

- date(format as in PHP)::

  {{contact.dates[0].date|date:d-m-Y}}


- dateAdd(interval) (See https://en.wikipedia.org/wiki/ISO_8601#Durations)::

  {{document.date|dateAdd:P1M|date:d-m-Y}}


- number(decimals,decimal separator,thousands separator::

   {{contact.customFields.number|number:2:,:.}}

- multiply(multiplier): Multiply a number::

   {{contact.customFields.number|multiply:2}}

- add(number): Add to a number::

   {{contact.customFields.number|add:2}}

- entity(type, id): Fetch an entity by ID::

        [assign contact = 1 | entity:Contact]

- links(entityName, properties (comma separated): gets the linked entities::

    [assign firstContactLink = someEntityVar | links:Contact | first]

- prop(property) get a property from an object or array by name::

      [assign formattedAddress = contact.addresses | sort:type:"postal" | first | prop:formatted]

- substr(start, length) Get a substring. For example to obscure a customer IBAN: {{customer.IBAN|substr:0:6}}xxxxxxxx{{customer.IBAN|substr:-3}}

- nl2br: Change line breaks to HTML <br> tags

- empty: returns true if empty or false if not

- dump: For debugging only. Dumps the variable type and value.

Arrays
~~~~~~

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

- newRow: useful when rendering tables. Check whether a new row should be started using a default modulo of 2.



