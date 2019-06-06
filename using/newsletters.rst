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

- name
- prefix
- firstName
- middleName
- lastName
- suffix
- jobTitle
- gender
- organizations: Array(same properties as contact)
- dates: Array (type, date)
- emailAddresses: Array(type, email)
- phoneNumbers: Array(type, number)
- addresses: Array(type, street, street2, zipCode, city, state, country, countryCode)
- urls: Array(type, url)
- debtorNumber
- IBAN
- vatNo
- :ref:`custom-fields`


Syntax
``````

A variable is written like this::

   {{contact.name}}

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