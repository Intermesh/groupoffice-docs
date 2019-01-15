System settings
===============

The system settings can be extended by modules. All system settings are stored
in the core_settings table.

To create new settings you must implement a settings module:

.. code:: php

	<?php
	namespace go\modules\core\users\model;

	use go\core;
	use go\core\db\Query;

	class Settings extends core\Settings {

		/**
		 * Default time zone for users
		 * 
		 * @var string
		 */
		public $defaultTimezone = "Europe/Amsterdam";
	}

This would create a new module with a single setting called "defaultTimezone".

You also need a controller to handle API calls::


