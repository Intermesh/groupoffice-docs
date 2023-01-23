Custom fields
=============

In our modern JMAP ORM, custom fields are commonly assigned to entities only, as properties are dependent on entities
and cannot exist without entities. Our legacy ActiveRecord items do not have this condition.

Add custom fields to an entity
------------------------------

Consider the Note entity, that has custom fields by default. However, let us pretend that they have been added as an
afterthought by the developer (which is not the case).


Install scripts
```````````````
First, the custom fields table has to be created. In the ``install/install.sql`` table, the following queries should be
added:

.. code:: sql

	CREATE TABLE `notes_note_custom_fields` (
	  `id` int(11) NOT NULL
	) ENGINE=InnoDB;

	ALTER TABLE `notes_note_custom_fields`
	  ADD CONSTRAINT `notes_note_custom_fields_ibfk_1` FOREIGN KEY (`id`) REFERENCES `notes_note` (`id`) ON DELETE CASCADE;

Of course, the ``unintall.sql`` file should drop the custom field table too:

.. code:: SQL

	DROP TABLE IF EXISTS `notes_note_custom_fields`;

Edit the entity model
`````````````````````

All you need to do in order for the entity to use the custom fields functions, is to include the ``CustomFieldsTrait``
trait:

.. code:: PHP

	<?php
	namespace go\modules\community\notes\model;

	use go\core\orm\CustomFieldsTrait;

	class Note extends AclItemEntity
	{

		/**
		 * The Entity ID
		 *
		 * @var int
		 */
		public $id;

		/*
		 * Et cetera
		 */
		use CustomFieldsTrait;

		/*
		 * ... insert methods here
		 */

The entity should now pop up in the System Settings > Custom Fields tab. Thu custom field mapping is automatically added,
so you do not need to do this manually.

Getting / setting custom fields on the server side
--------------------------------------------------

By now, you should be able to add custom fields to your JMAP entity. If you haven't already, please read the
:ref:`documentation on adding custom field sets and fields<custom-fields>`.

Building upon our earlier example: now that you have added custom fields to your note entity, let's add a fieldset named
'documentation' and add a field 'URI' to it. Programmatically, you can add a note with the custom field somewhat like
this:

.. code:: PHP

	<?php
	$note = new Note();
	// Add the normal fields
	$note->customFields->URI = "/path/to/your/documentation/page";
	$note->save();

The custom field is automatically mapped to the entity, so you can easily refer to the custom field by using the
customFields relation.

Conversely, retrieving the value of a custom field is done in a similar way:

.. code:: PHP

	<?php
	$note = Note::findById($id);
	$documentationUri = $note->customFields->URI;

Although the older ActiveRecord model falls outside the scope of this document, please note that getting and setting
custom field values works in the same way. 