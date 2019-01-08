E-mail
======

The administration of the e-mail module is pretty straight forward. You can 
setup multiple IMAP accounts for each user. There are however some advanced 
topics that we'll describe here.

.. figure:: /_static/using/email/email-module.png
   :width: 100%

   E-mail module

Creating accounts
-----------------

Only users with manage permissions for the e-mail module can create e-mail 
accounts. If you don't have manage permissions then you can only edit your 
e-mail address, sender name and signature if you have one pre-configured.

Go to:

E-mail -> Administration -> Accounts

to view your accounts. You can double click one to edit it.

To setup a new account you need some information from your e-mail service 
provider. You need the following values:

- Your e-mail address
- The hostname of the incoming mail server (IMAP).
- The port (usually 143)
- Your username and password
- Outgoing SMTP server hostname and port

With this information you can create an account easily. Go to:

E-mail -> Administration -> Accounts -> Add

After that fill in the e-mail address and name that should be associated with 
this account. If you are an administrator you can also set it up for another 
user by selecting it here. At last fill in the other values you got from your 
e-mail service provider. If you get a 'certificate-failure' error then tick 
the 'Don't validate certificate' option.

Synchronize e-mail
------------------
You can synchronize your mail to your desktop or mobile device. Read more about 
:ref:`connecting your device here <connect-a-device>`.

Sharing e-mail accounts
-----------------------

If you want to edit the e-mail account permissions to share an account you must 
go to:

E-mail -> Administration -> Accounts -> Double click account -> Permissions

Here you can add the users and user groups you want to grant access. 

Secretary
---------

If you want a secretary who handles calendar invitations, you may need to share 
the e-mail accounts too. It's important that you share the owner's e-mail 
account instead of adding a duplicate mail account. Group-Office uses the e-mail 
account owner to find the right calendar to store the appointments in.

When you share an account there are three levels:

+-------------------+---------------------------------------------------------+
| Level             | Extra privileges with manage permissions                |
+===================+=========================================================+
| Read	            | User's can only view messages                           |
+-------------------+---------------------------------------------------------+
| Read and delegate | Users can view, mark messages as read and reply with    | 
|                   | their own account. The account owner will be cc'd       |
|                   | automatically.                                          |
+-------------------+---------------------------------------------------------+
| Manage            | The user has full access to the account                 |
+-------------------+---------------------------------------------------------+

Creating e-mail signatures or templates
---------------------------------------

You can create multiple signatures with e-mail templates. Templates can be 
shared too. It's easy to setup a default e-mail template for the whole 
organization. You can also include automatic data tags that will be replaced 
with data from the logged in user or recipient. 

.. figure:: /_static/using/email/email-template.png

   E-mail template

To edit or create templates, 
go to:

System settings -> E-mail Templates.

Double click on a template or create a new one to edit it. If you drafted an 
HTML document in another program, make sure this HTML only contains inline style. 
Style sections in the head are not supported. You may need to use a tool 
to convert the head style to inline style such as 
this: http://inlinestyler.torchboxapps.com/

Images
------

When you insert an image make sure you don't copy paste it from another 
template or web page. Always insert it through the insert image toolbar from the 
template editor. This way the image will be embedded into the HTML e-mail 
template and will automatically be sent along with your e-mail messages.

Choose the right signature feature
----------------------------------

You can't use this feature together with the plain text signature at 
E-mail -> Administration -> Accounts -> Double click account row. Either use 
the simple plain text signature here or the e-mail templates.

Changing the font
-----------------

You can't select a font in the template editor. The font is globally defined in 
config.php. The administrator can change the default font:

$config['$html_editor_font']="font-size:13px; font-family:Arial, Helvetica, sans-serif;";

.. _template-variables:

Template variables
------------------

You can use the following values in the document:

Custom fields
`````````````

You can use custom fields like this:

- {project:databaseName}
- {contact:databaseName}
- {company:databaseName}
- etc.


Common fields
`````````````

- {date} Current date
- {filename} The filename of the document.

Fields of the logged in user

- {user:displayName}
- {user:email}
- {user:username}

Fields of the contact
`````````````````````

- {contact:sirmadam} Sir or Madam depending on the gender.
- {contact:salutation} The salutation
- {contact:formatted_address} Get the full address formatted according to the country standards.

- {contact:beginning} Dear sir / madam
- {contact:first_name} First name
- {contact:middle_name}
- {contact:last_name}
- {contact:initials}
- {contact:title}
- {contact:email}
- {contact:email2}
- {contact:email3}
- {contact:home_phone}
- {contact:fax}
- {contact:cellular}
- {contact:address}
- {contact:address_no}
- {contact:zip}
- {contact:city}
- {contact:state}
- {contact:country}
- {contact:department}
- {contact:function}
- {contact:work_phone}
- {contact:work_fax}
- {contact:homepage}

Fields of the contact
`````````````````````

- {company:formatted_address} Get the full address formatted according to the country standards.
- {company:formatted_post_address} Get the full address formatted according to the country standards.

- {company:mtime}
- {company:ctime}
- {company:crn} Company registration number
- {company:iban}
- {company:vat_no}
- {company:bank_no}
- {company:comment}
- {company:homepage}
- {company:email}
- {company:fax}
- {company:phone}
- {company:post_zip}
- {company:post_country}
- {company:post_state}
- {company:post_city}
- {company:post_address_no}
- {company:post_address}
- {company:country}
- {company:state}
- {company:city}
- {company:zip}
- {company:address}
- {company:address_no}
- {company:name2}
- {company:name}
- {company:id}
- {company:invoice_email}

Project fields
``````````````

- {project:name}
- {project:customer}
- {project:description}
- {project:ctime} Creation time
- {project:mtime} Modification time
- {project:status}
- {project:type}
- {project:start_time}
- {project:due_time}
- {project:units_budget}
- {project:responsibleUser:name} The manager

Example template for standard letter
````````````````````````````````````

{company:name}
{company:formatted_address}



Date:    {date}
About:   {filename}


{contact:salutation},



Best regards,


{user:displayName}

Spam filter
-----------

Most e-mail servers are setup with a spam filter. We use spamassassin on our 
hosted services. Spam filters flag messages as spam but you need a mail 
filtering rule to do something with it. Group-Office creates one by default 
but if for some reason it isn't there you can create it at:

E-mail -> Administration -> Account -> Filters.

Click on "Add" and match the settings like in this screenshot:

