.. _server-account-settings:

Account settings
================

Often it is necessary to create user account settings for modules.
You can do that by extending the User entity with properties.

Create a new property model. For example:

.. code:: php

	<?php

	namespace go\modules\community\addressbook\model;

	use go\core\orm\Property;

	class UserSettings extends Property {

		/**
		 * Primary key to User id
		 * 
		 * @var int
		 */
		public $userId;

		/**
		 * Default address book ID
		 * 
		 * @var int
		 */
		public $defaultAddressBookId;

		protected static function defineMapping() {
			return parent::defineMapping()->addTable("addressbook_user_settings", "abs");
		}
	}


Also create a database table for it:

.. code:: sql

	CREATE TABLE IF NOT EXISTS `addressbook_user_settings` (
		`userId` int(11) NOT NULL,
		`defaultAddressBookId` int(11) DEFAULT NULL,
		PRIMARY KEY (`userId`),
		KEY `defaultAddressBookId` (`defaultAddressBookId`)
	) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=COMPACT;


	ALTER TABLE `addressbook_user_settings`
		ADD CONSTRAINT `addressbook_user_settings_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `core_user` (`id`) ON DELETE CASCADE,
		ADD CONSTRAINT `addressbook_user_settings_ibfk_2` FOREIGN KEY (`defaultAddressBookId`) REFERENCES `addressbook_addressbook` (`id`) ON DELETE SET NULL;


In the Module.php we can use the "Property::EVENT_MAPPING" :ref:`event <events>` to dynamically extend the User 
entity with this property:

.. code:: php

	<?php
	namespace go\modules\community\addressbook;

	use go\core\module\Base;
	use go\modules\community\addressbook\model\Contact;
	use go\modules\core\links\model\Link;
	use go\modules\core\users\model\User;
	use go\modules\community\addressbook\model\UserSettings;


	class Module extends Base {

		public static function defineListeners() {
			// When the User mapping is created listen call static::onMap
			User::on(Property::EVENT_MAPPING, static::class, 'onMap');
		}

		public static function onMap(Mapping $mapping) {
			//Add the relation to the User mapping
			$mapping->addRelation('addressBookSettings', UserSettings::class, ['id' => 'userId'], false);
		}
	}


After these changes you must run install/upgrade.php to rebuild the cache.

Now the User entity has this new property:

.. code:: json

	{
		id: 1,
		username: "admin",
		addressBookSettings: {
			defaultAddressBookId: 1
		}

		etc..
	}



You can now :ref:`implement a settings panel in the webclient <webclient-account-settings>`.