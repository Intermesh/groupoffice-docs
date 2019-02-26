Entities
========

Each module can register entities. For example the notes module registers a "Note"
entity. This entity will be synchronized with the server.

.. code:: javascript

	go.Modules.register("community", 'notes', {
		mainPanel: "go.modules.community.notes.MainPanel",
		title: t("Notes"),
		entities: [{
				name: "Note",			
				hasFiles: true,
				links: [{
					/**
					 * Opens a dialog to create a new linked item
					 * 
					 * @param {string} entity eg. "Note"
					 * @param {string|int} entityId
					 * @returns {go.form.Dialog}
					 */
					linkWindow: function(entity, entityId) {
						return new go.modules.community.notes.NoteForm();
					},

					/**
					 * Return component for the detail view
					 * 
					 * @returns {go.detail.Panel}
					 */
					linkDetail: function() {
						return new go.modules.community.notes.NoteDetail();
					}	
				}]
		}, "NoteBook"],	
		systemSettingsPanels: ["go.modules.community.notes.SystemSettingsPanel"]
	});

An entity can be configured as string for simple entities or as object to provide
more options for linking and files.

Data stores
===========

We assume you're already familiar with the data stores ExtJS already has built in.

We've extended the Ext.data.JsonStore with our own go.data.Store. We also introduced 
a new type of store. The go.data.EntityStore. 


go.data.EntityStore
-------------------

The EntityStore is a single source
of truth for all remote data. You can pass an "entityStore" property to any component or go.data.Store.
The component can then implement and onChanges function to handle data changes to the entity.

A simple contact name component example:

.. code:: javascript

	// A component showing a contact name
	var nameComponent = new Ext.BoxComponent({
		// The current contact
		contact: null,

		//Create <h1>John Doe</h1>
		autoEl: "h1",
		
		//Attach to Contact entity store
		entityStore: "Contact",

		//The onChanges handler
		onChanges: function(entityStore, added, changed, destroyed) {

			//If current contact changed then update the view
			if(this.contact && changed[this.contact.id]) {
				this.setContact(changed);
			}
		},

		//Set contact
		setContact: function(contact) {
			this.contact = contact;

			if(this.rendered) {
				this.update(contact.name);
			}
		}
	});


go.data.Store
-------------
This store is used in views and works with an entityStore.

For example:

.. code:: javascript

   var store = new go.data.Store({
			fields: [
				'id', 
				'name', 
				'content', 
				'excerpt', 
				{name: 'createdAt', type: 'date'}, 
				{name: 'modifiedAt', type: 'date'}, 
				{name: 'creator', type: 'User', key: 'createdBy'},
				{name: 'modifier', type: 'User', key: 'modifiedBy'},
				'permissionLevel'
			],
			entityStore: "Note"
		});


We've created a new data field type. Notice the type = 'User'. You can use any 
entity in a go.data.Store. This field will fetch the User from the entity store
so you can use this object in your grid renderer for example.