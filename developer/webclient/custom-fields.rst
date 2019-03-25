Custom fields
=============

You don't have to do anything to make custom fields work in the web client.

The only thing you might want to do is customize the filter of the field sets. With 
the filter property you can define when a fieldset displays in a dialog. For example
when set to::

	{
		"isOrganization": true
	}

the field set will only show if that property matches the form entity.

You can override the field set dialog by defining the field set dialog class in 
the entity in Module.js:

.. code:: javascript

  entities: [{
			
			name: "Contact",
			customFields: {
				fieldSetDialog: "go.modules.community.addressbook.CustomFieldSetDialog"
			},
			.. snippet ..
	}]
   
