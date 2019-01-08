Custom fields
=============


Add a system settings panel with a custom fields panel to manage fields:


.. code:: javascript

   go.modules.community.addressbook.SystemSettingsPanel = Ext.extend(Ext.Panel, {
		iconCls: 'ic-contacts',
		autoScroll: true,
		initComponent: function () {
			this.title = t("Address book");		

			this.items = [new go.modules.core.customfields.SystemSettingsPanel({
					// The entity it's for
					entity: "Contact",

					//Optionally override this function to customize the fieldset dialog.
					createFieldSetDialog : function() {
						return new go.modules.community.addressbook.CustomFieldSetDialog();
					}
			})];


			go.modules.community.addressbook.SystemSettingsPanel.superclass.initComponent.call(this);
		}
	});
   


Add the fields to the grid store definitions:

.. code:: javascript

   .concat(go.modules.core.customfields.CustomFields.getFieldDefinitions("Contact"))


.. code:: javascript

	this.store = new go.data.Store({
			fields: [
				'id',
				'name',
				{name: 'createdAt', type: 'date'},
				{name: 'modifiedAt', type: 'date'},
				{name: 'creator', type: go.data.types.User, key: 'createdBy'},
				{name: 'modifier', type: go.data.types.User, key: 'modifiedBy'},
				{name: 'star', type: go.data.types.ContactStar, key: function(r) {return r.id + "-" + go.User.id}},
				'permissionLevel',
				'photoBlobId',
				"isOrganization",
				"organizations"				
			].concat(go.modules.core.customfields.CustomFields.getFieldDefinitions("Contact")),
			sortInfo :{field: "name", direction: "ASC"},
			entityStore: go.Stores.get("Contact")
		});


Add the custom grid columns to the column model with::

   .concat(go.modules.core.customfields.CustomFields.getColumns("Contact"))