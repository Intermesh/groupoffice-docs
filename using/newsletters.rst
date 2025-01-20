Newsletters
===========

.. figure:: /_static/using/newsletters/newsletters.png
   :alt: Newsletters
   :width: 100%

   Newsletters

The newsletters module is an easy tool to manage address lists and send out newsletters. Using powerful templates you can personalize your messages.

Accounts
--------

If you have manage permissions for the newsletters module, you can manage SMTP accounts from System Settings screen, tab Newsletters.

.. figure:: /_static/using/newsletters/system-settings.png
   :alt: Account management
   :width: 100%

   Account management

.. tip:: If you need to prevent your SMTP server to end up on a spam blacklist, you can maximize the number of messages sent per minute.

Create lists
------------

Create a list by clicking the add button in the "Lists" toolbar.
Then click the add button from the "Contents" toolbar in the middle to add
contacts.

You can add contacts one by one but you can also add entire search results using
filters. You can also include entire lists into a new distribution list by selecting them from their respective tabs.

.. note:: Individual newsletters inherit their permissions from the parent distribution list. In practice this means that users can only manage newsletters for distirbution lists that users have actual permissions to.

Compose
-------

To send a newsletter, click the "Compose" button from the "Sent items" panel. Start sending the message by clicking the
"Send" button.

Testing a newsletter is easy. Just click the "Test message" button and you will send the newsletter to the selected recipients only.

.. figure:: /_static/using/newsletters/compose.png
   :alt: Compose
   :width: 100%

   Compose


.. tip:: After hitting the "Send" button you can pause / unpause the distribution of the newsletter. That will pause or unpause the next batch of emails to be sent the next minute.

Templates
---------

From the composer you can also manage :ref:`templates<templates>` . Via the menu shown in the screenshot above.
You can use the following variables in these templates:

Contact
```````
Fields of the recipient:

- contact.salutation
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
- :ref:`custom-fields`, :ref:`See the templates section for the syntax<templates>`

Other
`````
- unsubscribeUrl: The URL a recipient can use to remove himself from the list. eg. <a href="{{unsubscribeUrl}}">unsubscribe</a>
- now: (Date) The time the message is sent

Creator
```````
Fields of the user who created the newsletter

- creator.displayName
- creator.email
- creator.username


You can read more about :ref:`templates and the syntax here<templates>`.


Upload message
--------------

.. figure:: /_static/using/newsletters/upload.png
   :alt: Upload message
   :width: 100%

Upload a pre-created email message by pressing the "Upload message" button in the Newletter composer.
The file needs to be a .ZIP with the following content:

- /index.html
- /images/*

.. note:: Email template creators like BeeFree will generate exported messages in this format.

All the images references in `index.html` need to be inside the `images/` folder.
If images are not in this folder they can not be extracted and included in the email.

Once the message is uploaded the Compsoser dialog will switch to read-only mode.

