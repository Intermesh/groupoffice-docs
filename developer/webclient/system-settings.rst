System settings
===============

For certain modules, you may want to enable the system administrator to manage settings. In Group Office, this can be
achieved by either adding a panel to the system settings dialog or the user settings dialog.

The main difference between the two is that user settings are defined on a user level and are thus part of the user
profile, whereas system settings are defined on a system level.

As a case study, we dive into the current code for the addressbook module.

``module.js``
-------------

The main ``module.js`` file should have a property for ``userSettingsPanels`` (in case of user settings) or
``systemSettingPanels``, e.g.

.. code:: javascript

	go.Modules.register("community", "addressbook", {
		/* (...) */

		/**
		 * These panels will show in the My Account or user settings dialog
		 */
		userSettingsPanels: [
			"go.modules.community.addressbook.SettingsPanel",
			"go.modules.community.addressbook.SettingsProfilePanel"
		],

		/**
		 * These panels will show in the System settings
		 */
		systemSettingsPanels: [
			"go.modules.community.addressbook.SystemSettingsPanel",
		],

		/* (...) */
	});

.. note:: As both properties are defined as arrays, you are perfectly allowed and able to add more than one panel. Neat, huh?

SystemSettingPanels
-------------------

In your ``scripts.txt`` file, you need to add a line for each javascript file that you wish to implement your system
settings in, e.g. ``SystemSettingsPanel.js``. Having done that, you can add your panel code, which would look somewhat like this:

.. code:: javascript

	go.modules.community.addressbook.SystemSettingsPanel = Ext.extend(go.systemsettings.Panel, {

		title: t("Address book"),
		iconCls: 'ic-contacts',
		labelWidth: 125,
		initComponent: function () {
			//The account dialog is an go.form.Dialog that loads the current User as entity.
			this.items = [{
				xtype: "fieldset",
				items: [
					/* etcetera */
				]
			}];

			go.modules.community.addressbook.SystemSettingsPanel.superclass.initComponent.call(this);
		}
	});

In the inner ``items`` array, you can put the individual settings. Please note that on the server side, these need to be
saved into a settings table, e.g. ``addressbook_settings``.

UserSettingPanels
-----------------

Again, please make sure to add the files in which you want to put the user settings. A sane name for this would be
``SettingsPanel.js`` and that is exactly the name in the addressbook module. A user settings panel simply extends a
vanilla Ext.Panel object:

.. code:: javascript

	go.modules.community.addressbook.SettingsPanel = Ext.extend(Ext.Panel, {
		title: t("Address book"),
		iconCls: 'ic-contacts',
		labelWidth: 125,
		layout: "form",
		initComponent: function () {
			//The account dialog is an go.form.Dialog that loads the current User as entity.
			this.items = [{
				xtype: "fieldset",
				title: t("Display options for address books", "addressbook", "community"),
				items: [
					/* (...) */
				]
			}];
			go.modules.community.addressbook.SettingsPanel.superclass.initComponent.call(this);
		}
	});

