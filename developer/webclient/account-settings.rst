.. _webclient-account-settings:

Account settings
================

Often it is necessary to create user account settings for modules.
You can do that by extending the User entity with properties.

Create the :ref:`user property on the server <server-account-settings>` before 
implementing the client.

1. Create a new file SettingsPanel.js:

   .. code:: javascript

		/* global go, Ext */

		go.modules.community.addressbook.SettingsPanel = Ext.extend(Ext.Panel, {
			title: t("Address book"),
			iconCls: 'ic-contacts',
			labelWidth: 125,
			layout: "form",
			initComponent: function () {

				//The account dialog is an go.form.Dialog that loads the current User as entity.
				this.items = [{
					xtype: "fieldset",
					items: [{
							xtype: "addressbookcombo",
							hiddenName: "addressBookSettings.defaultAddressBookId",
							fieldLabel: t("Default address book")
						}
					]}
				];

				go.modules.community.addressbook.SettingsPanel.superclass.initComponent.call(this);
			}

		});


2. Add this file to scripts.txt

3. Edit Module.js and add the new "userSettingsPanel" to the array:

   .. code:: javascript
	 
			/* global go */

			go.Modules.register("community", "addressbook", {
				mainPanel: "go.modules.community.addressbook.MainPanel",
				title: t("Address book"),
				userSettingsPanels: ["go.modules.community.addressbook.SettingsPanel"],
				etc...
			});