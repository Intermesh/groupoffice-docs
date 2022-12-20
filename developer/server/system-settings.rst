System settings
===============

On an API level, the system settings can be extended by modules. All system settings are stored
in the ``core_settings`` table.

To create new settings you must implement a settings model:

.. code:: php

	<?php
	namespace go\modules\community\addressbook\model;
	use go\core;

	class Settings extends core\Settings
	{

		/**
		 * Default time zone for users
		 * 
		 * @var string
		 */
		public $autoLinkEmail = false;
	}

This would create a new model with a single setting called "autoLinkEmail".

User settings
-------------

Apart from system settings, settings can also be saved by individual user. These are saved into a JMAP property (of the
User entity) and are normally stored into a database table named ``module_user_settings``, in which `module` would refer to
the module name, e.g. ``addressbook_user_settings``.

A user settings model would look somewhat like this:

.. code:: php

	<?php

	namespace go\modules\community\addressbook\model;

	use go\core\orm\Mapping;
	use go\core\orm\Property;

	class UserSettings extends Property {
		/**
		 * Primary key to User id
		 *
		 * @var int
		 */
		public $userId;

		/*
	     * Several other attributes
	     */

		protected static function defineMapping(): Mapping
		{
			return parent::defineMapping()->addTable("addressbook_user_settings", "abs");
		}
	}

