Newsletters
===========

.. figure:: /_static/using/newsletters/newsletters.png
   :alt: Newsletters
   :width: 100%

   Newsletters

The newsletters module is an easy tool to manage address lists and send out newsletters. Using powerful templates you can personalize your messages.

Create lists
------------

Create a list by clicking the add button in the "Lists" toolbar.
Then click the add button from the "Contents" toolbar in the middle to add
contacts.

You can add contacts one by one but you can also add entire search results using
filters.

Compose
-------

To send a newsletter click the add button from the "Sent items" panel.

.. figure:: /_static/using/newsletters/compose.png
   :alt: Compose
   :width: 100%

   Compose

Templates
---------

From the composer you can also manage templates. Via the menu shown in the screenshot above.
You can use the following variables in these templates:

Contact
```````
Fields of the recipient

- contact.name
- contact.prefix
- contact.firstName
- contact.middleName
- contact.lastName
- contact.suffix
- contact.jobTitle
- contact.gender
- contact.organizations: Array(same properties as contact)
- contact.dates: Array (type, date)
- contact.emailAddresses: Array(type, email)
- contact.phoneNumbers: Array(type, number)
- contact.addresses: Array(type, street, street2, zipCode, city, state, country, countryCode)
- contact.urls: Array(type, url)
- contact.debtorNumber
- contact.IBAN
- contact.vatNo
- :ref:`custom-fields` (The database name prefixed with "contact.customFields.")

Other
`````
- unsubscribeUrl
- now (Date) The time the message is sent

Creator
```````
Fields of the user who created the newsletter

- creator.displayName
- creator.email
- creator.username


Syntax
``````

A variable is written like this::

   {{contact.name}}
   
Or a custom field:

   {{contact.customFields.<DATABASE_NAME_OF_CUSTOMFIELD>>}}

Arrays can be written like this::

  {{contact.emailAddresses[0].email}}

You can also iterator over arrays::

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


An advanced example for printing the salutation::

   Dear [if {{contact.prefixes}}]{{contact.prefixes}}[else][if !{{contact.gender}}]Ms./Mr.[else][if {{contact.gender}}=="M"]Mr.[else]Ms.[/if][/if][/if] {{contact.lastName}}


An simple example template::

   Hi {{contact.firstName}},


   Best regards,

   {{creator.displayName}}
   {{creator.profile.organizations[0].name}}
