Events
======

Because Group Office is a modular system it has events. Modules can register
listeners to Objects implementing the "go\\core\\event\\EventEmitterTrait" trait.

All entities do this already. They fire an event on:

1. save
2. delete
3. mapping, so you can add new relational properties.


Adding listeners
----------------

The community/googleauthenticator uses events for example, to add a "googleauthenticator" property to the User entity.

Listeners are always defined in the Module.php file of the module. A method
"defineListeners" can be created for it. Look at 
go/modules/community/googleauthenticator/Module.php for the complete file.

.. code:: php

	public function defineListeners() {
		User::on(Property::EVENT_MAPPING, static::class, 'onMap');
	}
	
	public static function onMap(Mapping $mapping) {		
		$mapping->addRelation("googleauthenticator", model\Googleauthenticator::class, ['id' => 'userId'], false);		
		return true;
	}


Firing events
-------------

To fire an event your object must use the "go\\core\\event\\EventEmitterTrait" trait.

Then define an EVENT_* constant and document your event:

.. code:: php

   /**
    * Something very special happens here.
    */
   const EVENT_MYEVENT;

Then you can call:

.. code:: php

   $this->fireEvent(self::EVENT_MYEVENT, $this, "arg2", "arg3");