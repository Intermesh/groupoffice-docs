
Override an existing module
===========================

This tutorial will explain how to override existing modules in Group Office. As we are in the process of transitioning
from the old ActiveRecord framework to a more modern `JMAP <https://jmap.io/>`_ approach, both frameworks get a bit of
attention.

Please read the articles in the :ref: Server API and Webclient API series. It is also a good idea to read the server module
and webclient module tutorials first, as these will give you some insight on how a Group Office module is structured.

A prerequisite of this tutorial is that you already have an environment up and running and that you are familiar with
our coding standards and best practices. The tutorial is written in the new framework, both on the server side and on
client side. That does not prevent us from overriding the older modules, as you'll see below.

.. note:: As you will be overriding mainly the community modules, you can familiarize yourself with them by browsing the very module files themselves in your development environment.

Example use case
----------------

Let's consider the fictional use case: you have access to an external API that sends SMS messages and you wish to use
this in Group Office. As Group Office has no access to this by default, you have to override some modules. A good
starting point would be the calendar (which at the time of this writing is in the old framework). Upon inviting a customer,
they should receive an SMS message.

Furthermore, when a new customer is added to a certain address book in the address book module, it should be possible to
send them a welcome message upon creation. Finally, it should be possible to send an SMS manually to a customer from
within the address book itself.

Create a module
---------------

The first step of an override is to create a new module directory. Let's call your package 'acme', as you will be doing
some Wile E. Coyote style work. The module itself will simply be named 'sms'.

As we will be developing the module as a modern style module, we will create it in the ``go/modules`` subdirectory. The
end result will be ``go/modules/acme/sms``. We will refer to this as the **module subdirectory** or **module root**.

``Module.php`` file
```````````````````

Module parameters and server side overrides are defined in the ``Module.php`` file in the module root. Let's open your
favorite editor and create it. Initially it should look somewhat like this:

.. code:: php

	<?php

	namespace go\modules\acme\sms;

	use Exception;
	use go\core;

	class Module extends core\Module
	{

		/**
		 * @return string
		 */
		function getAuthor(): string
		{
			return "Wile E. Coyote <coyote@acme.inc>";
		}


		/**
	     * Overrides for the ActiveDirectory based API
		 */
		public static function initListeners()
		{
			// ...
		}

		/**
		 * JMAP style overrides
		 */
		public function defineListeners()
		{
			// ...
		}


		/**
	     * The modules on which your override will depend
		 */
		public function getDependencies(): array
		{
			return ['community/addressbook', 'legacy/calendar'];
		}


		/**
		 * Code to be run directly after installation
		 * @throws Exception
		 */
		protected function afterInstall(model\Module $model): bool
		{
			return true;
		}
	}

``install`` subdirectory
````````````````````````

As with normal modules, this subdirectory will contain an ``install.sql`` file, an ``updates.php`` file and an ``uninstall.sql``
file. The install file will be run upon installation, the updates file will be run for each update and the uninstall file
is run when uninstalling the new module.

``language`` subdirectory
`````````````````````````

Contains translations. You may not need any (you will). At the very least, this subdirectory should contain an ``en.php``
file with the following values:

.. code:: php

	<?php
	return [
		'name' => 'SMS',
		'description' => 'Send SMS messages through Group Office'
	];

This will ensure that when browsing available modules, you will get a helpful description.

``views/Extjs3/`` subdirectory
``````````````````````````````

If you need any changes to the Javascript code, the Javascript files are organized exactly like the normal Javascript
modules. In this subdirectory you can add new windows, dialogs or panels or override existing ones. This is compatible
with both the legacy framework and the new framework.


Server module - ActiveRecord framework
--------------------------------------

Let's review our use case. We want to send a customer an SMS when they are invited to an appointment. Therefore, we will
have to create an override for the legacy calendar module, more specifically' the ``EventController`` class. Old style
controllers and active record models will fire events when performing certain actions. The event we are looking for, is
the *submit* event.

.. tip:: When you wish to explore the events that you can hook into, find calls to the ``fireEvent`` method in the Controller class, the Model class and their parent classes.

In the ``initListeners`` method in your ``Module.php`` file, add the following code:

.. code:: php

	<?php
	public static function initListeners()
	{
		$ctrlr = new \GO\Calendar\Controller\EventController();
		$ctrlr->addListener('submit', self::class, 'onEventSubmit');
	}

Check which parameters the new function will need to find the `submit` hook. Make sure to pass these parameters in the
correct order. Otherwise, your event handler method will not match the expected input. Here's a bit of pseudocode that
will read the event, check whether it is new and send an SMS to each participant:

.. code:: php

	<?php
	public static function onEventSubmit(&$ctnl, &$response, &$event, &$params, $modifiedAttributes)
	{
		if (!isset($params['id']) || !is_numeric($params['id'])) {
			foreach($event->participants() as $participant) {
				if(!$participant->contact_id) {
					continue;
				}
				$cnt = Contact::findById($participant->contact_id);

				// Send the SMS to the contact.
			}
		}
		// Make sure that the return value is true if the method was run successfully.
		return true;
	}

After creating this method, it is important to run the upgrade script. As the code is being cached, you need to refresh
the server side code. Once the method exists, you can just test it after each edit without refreshing the cache.


Server module - JMAP framework
------------------------------

In our JMAP :ref:`ORM<orm>`,  events are tied to database objects. As database objects are roughly split into entities
and properties, you can find the event names in the entity and property classes in the ``go/core/orm`` subdirectory.
They can easily be found by grepping 'EVENT_' and the names of the entities are pretty consistent: ``EVENT_FOO``is
triggered when a `foo` action is performed, whereas ``EVENT_BEFORE_FOO`` is triggered before doing the actual `foo`
action.

As our use case states that an welcome SMS is to be sent to a new customer in a certain address, the event to be hooked
into is most probably ``EVENT_SAVE``. First, we define a listener for contacts in our override method:

.. code:: php

	<?php
	public function defineListeners()
	{
		Contact::on(Entity::EVENT_SAVE, static::class, 'onSave');
	}

The onSave function will look somewhat like this:

.. code:: php

	<?php
	/**
	 * @param Contact $task
	 * @return void
	 */
	public static function onSave(Contact $contact)
	{
		$myAddressBookId = 42;
		if($contact->isNew() && $contact->addressbook->id === $myAddressBookId) {
			// Send a welcome SMS
		}
	}

After saving, this handler function will check whether the contact is new and it is part of the correct address book. If
that is the case, the SMS is being sent.

Webclient module
----------------

As with normal modules, please add all javascript files to the ``scripts.txt`` file. Otherwise, they will not be used.

The ``module.js`` file
``````````````````````

If you need client-side overrides, you need to define your custom namespace and register your module:

.. code:: javascript
	Ext.namespace('go.modules.acme.sms');

	go.Modules.register("acme", 'sms', {
		// this may be interesting if you need to configure the SMS module as administrator
		systemSettingsPanels: [
			'go.modules.acme.sms.SystemSettingsPanel'
		],
	});

Now we have registered a module that will do absolutely nothing yet. This ``module.js`` file is in every way compatible
with any other ``module.js`` files, so you can define your entities, relations, main panels and whatever you like.

.. tip:: In the system settings panel, you can add configuration options. You override the normal system settings dialog by adding a new panel. This panel will not differ from any other system settings panel.


Overrides
`````````

The juicy bit is to override javascript files for the end user. Overrides can be done in three ways:

1. Before running the original method, use the ExtJS ``createInterceptor`` function;
2. After running the original method, use the ExtJS ``createSequence`` function;
3. Instead of running the original method, just define the overriding function with the same name as the original;

As we have now handled the theory, let's make some code. Let's say that we have decided to add a field to the calendar
settings in which we store the SMS service API key. After all, creating an entirely new panel for one field is a bit
too much.

A sensible way to create overrides is to create a Javascript file with the name ``moduleNameOverrides.js``, so in our
case it will be ``calendarOverrides.js``. See the pseudocode snippet below:

.. code:: javascript

	GO.moduleManager.onModuleReady('calendar',function(){
		Ext.override(GO.calendar.SettingsPanel, {

			initComponent : GO.calendar.SettingsPanel.prototype.initComponent.createSequence(function () {
				const url =  this.getUrl();

				this.externalApiFieldset = new Ext.form.FieldSet({
					forceLayout:true,
					xtype : 'fieldset',
					autoHeight : true,
					layout : 'form',
					title : t("Your SMS service", "sms", 'acme'),
					items : [
						{
							xtype:'text',
							fieldLabel:  t("API key", "sms", 'acme'),
							allowBlank: false,
							/* et cetera */
						}
					]

				});

				this.add(this.externalApiFieldset);
			}),

		});
	});

What happens here, is that after the calendar function has been fully initiated, the API key field is being added to the
settings panel. This can only happen after the settings panel has been initialized, so after the ``initComponent`` call.
Hence the ``createSequence``.

Likewise, when viewing a customer contact, let's add a new button 'Send SMS message'. The class you will want to override,
is the ``ContactDetail`` class, more specifically the toolbar:

.. code:: javascript

	Ext.onReady(function(){

		Ext.override(go.modules.community.addressbook.ContactDetail, {

			initToolbar : go.modules.community.addressbook.ContactDetail.prototype.initToolbar.createSequence(function(){
				this.moreMenu.menu.push('-',{
					iconCls: "ic-sms",
					text: t("Send an SMS", "sms", "acme"),
					handler: function () {
						this.openMessageBox();
					},
					scope: this
				});

			}),

			openMessageBox: function() {
				// Open a dialog...
			}
		});
	});

.. note:: It is customary to have one overrides file for each module you override. With each ``Ext.override`` call you can override a separate class.

