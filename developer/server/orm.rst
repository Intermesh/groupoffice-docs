.. _orm:

Object Relational Mapping
=========================

Group Office features an ORM package in go\\core\\orm.

There are two main types of models:

1. Entity: A model that can be changed directly by the user. Such as a Contact.
2. Property: A model that belongs to an Entity. Such as a Contact's E-mail address.


Mapping
-------

Each model must implement the ``defineMapping`` method. This mapping maps database
tables to the object and defines other models as properties.

For example the ``go/modules/community/music/model/Artist`` model defines:

.. code:: php

  protected static function defineMapping() {
    return parent::defineMapping()
            ->addTable("music_artist", "a")
            ->addArray('albums', Album::class, ['id' => 'artistId']);
  }

You can see that it maps a table ``music_artist`` and adds a property 'albums' as an array. If you'd like to retrieve
relations between entity models, use the ``addScalar`` method instead of the ``addArray`` method.

Furthermore, one can define custom properties from database queries by using the ``addQuery`` method. For example, one
could define an `albumcount` property for an artist like this:

.. code:: php

  protected static function defineMapping() {
    return parent::defineMapping()
        ->addTable("music_artist", "artist")
            ->addQuery((new Query())->select('COUNT(alb.id) AS albumcount')
            ->join('music_album', 'alb','artist.id=alb.artistId')->groupBy(['alb.artistId']) );
    }

A property must be defined for all database columns the model should use.
There should also be a public $albums property.

.. note:: Mappings are cached for performance. When making changes you need to 
   run ``/install/upgrade.php`` to rebuild the cache. You can also disable cache in the :ref:`config.php <configuration>` file::

        $config['core'] = [
            'general' => [
                'cache' => 'go\\core\\cache\\None'
            ]
        ];


.. warning:: As per Group Office 6.6, the ``setQuery`` method has been deprecated in favor of the ``addQuery`` method.
   Any custom development that uses the ``setQuery`` method, will fall back on the ``addQuery`` method, but you will
   get a deprecation warning in your IDE.

addTable() method
`````````````````
With the ``addTable()`` method you map table database columns to object properties.
All protected and public properties of the object that match a database column 
name will be loaded from and saved to that table. You can add multiple tables
to one entity. The primary keys must match or a key mapping can be passed to the
method. See the code documentation for more details.

addArray() method
`````````````````
If you wish to retrieve the full set of um.. properties of a property for an entity,
you can use the ``addArray()`` method. For instance, if you want to retrieve entire
albums for an artist as per the tutorial, your ``defineMapping()`` method for the Artist
model should look like this::

	protected static function defineMapping() {
		return parent::defineMapping()
						->addTable('music_artist', 'artist')
						->addArray('albums', Album::class, ['id' => 'artistId']);
	}

The ``addArray()`` method yields a flat array of properties, i.e. an array that does not use a
key-value pair.

addMap() method
```````````````

If you prefer to retrieve relationships as key-value pairs, for instance of relation management,
use the ``addMap()`` method::


	protected static function defineMapping() {
		return parent::defineMapping()
			->addTable('music_artist', 'artist')
	        ->addMap('albums', Album::class, ['id' => 'artistId']);
	}

This method returns an object, in which the ``id`` of a relation entity serves as a key. Its
values are nested inside the object.

addScalar() method
``````````````````
The ``addScalar()`` method retrieves an array of ``id`` fields for related items. If there are
no known relations, an empty array is returned.

.. note:: This is a way to relate entities to properties. However, it it more common practice
   to define such relatable items as entities.

addHasOne() method
``````````````````
A special relation is the ``addHasOne()`` method. It is commonly used with a ``UserSettings`` model,
which gives a default entity of a certain type to each user.

For instance, the address book module has the following lines in its ``module.php`` file::

    public static function onMap(Mapping $mapping) {
		$mapping->addHasOne('addressBookSettings', UserSettings::class, ['id' => 'userId'], true);
	}

This will create a new default address book for each new user and will assign it as default address book.

addRelation() method
````````````````````
With the ``addRelation()`` method you can map "Property" models with a has one or has many
relation. These properties will be loaded and saved automatically.

.. note:: You can't add relations to other entities. Only "Property" models can
   be mapped. Fetch other entities in the client by key. If you would implement a
   getOtherEntity() method, it would be very hard to synchronize the entities to
   clients. Because each entity keeps it's own sync state. If the "OtherEntity" 
   changes it would mean that this entity would change too.

   If you need to create a method to retrieve another entity on the server side
   only then it's recommended to name it "findOtherEntity()" so it won't become
   a public API property.

addQuery() method
`````````````````

As per Group Office 6.6, the ``addQuery()`` method allows you to add custom SQL code to your mapping. The parameter is a
``go/core/db/Query`` Object. It replaces the ``setQuery()`` method in earlier Group Office versions and has the
advantage of being stackable. That is, depending on the modules installed, the mapping will merge custom SQL code
instead of overwriting it.

As per the tutorial, a valid use case would be to add the album title to a music review:

.. code:: php

      protected static function defineMapping()
      {
          return parent::defineMapping()
              ->addTable('music_review')
              ->addQuery((new Query())->select('a.name AS albumtitle')
                  ->join('music_album', 'a', 'a.id=music_review.albumId'));
      }


.. note:: When developing against Group Office 6.5 or below, you can still use the ``setQuery()`` method, but you
   will not be able to use multiple ``setQuery()`` methods for your entities. One will overwrite the other.

Getters and Setters
-------------------

All models can implement get and set methods to create API properties.

For example if you have a property "foo" in the database but this property needs
some processing when you get or set it. You can make this property "protected".

.. note:: You should never make database properties private because then the 
   parent class can't access it for saving and loading.

In this example the property "foo" is JSON encoded in the database but turned
into an array in the API:

.. code:: php

   protected $foo;
   
   public function setFoo($value) {
     $this->foo = json_encode($value);
   }
   
   public function getFoo() {
     return json_decode($value, true);
   }


Working with entities
---------------------

You can find entities with the find() and findById() method.

.. note:: The method find() returns a Query object. You can read more on that in the :ref:`dal` chapter.

Here's how to find the first Artist entity.

.. code:: php

   $artist = \go\modules\community\music\model\Artist::find()->single();
   echo json_encode($artist);

This will out put the artist in JSON format:

.. code:: json

   {
       "permissionLevel": 50,
       "name": "De Scherings",
       "createdAt": "2018-08-17T14:42:17+00:00",
       "modifiedAt": "2018-08-24T12:42:20+00:00",
       "createdBy": 1,
       "modifiedBy": 1,
       "albums": [
           {
               "artistId": 3,
               "name": "Good times",
               "releaseDate": "2018-08-24T00:00:00+00:00",
               "genreId": 2
           }
       ],
       "photo": "a1a82b74532fcd822f0923cd84ab23533eb92d5f",
       "id": "3"
   }

Here's how to create a new one with an album:

.. code:: php

   $artist = new Artist();
   $artist->name = "The Doors";
   $artist->albums[] = (new Album())->setValues(['name' => 'The Doors', 'releaseDate' => new DateTime('1968-01-04'), 'genreId' => 2]);
   
   if(!$artist->save()) {
     echo "Save went wrong: ". var_export($artist->getValidationErrors(), true) . "\n";
   } else
   {
     echo "Artist saved!\n";
   }

Or you can use "setValues" this is what the JMAP API uses when it POSTS values in JSON:

.. code:: php

    $artist = (new Artist)
            ->setValues([
                'name' => 'The War On Drugs',
                'albums' => [
                    ['name' => 'Album 1', 'releaseDate' => new DateTime('2018-01-04'), 'genreId' => 2],
                    ['name' => 'Album 2', 'releaseDate' => new DateTime('2018-01-04'), 'genreId' => 2]
                ]
            ]);
    
    if(!$artist->save()) {
      echo "Save went wrong: ". var_export($artist->getValidationErrors(), true) . "\n";
    } else
    {
      echo "Artist saved!\n";
    }



Cascading delete
----------------

It's recommended to take advantage of the database foreign keys to cascade delete
relations. This is much faster then deleting relations in code.
It does however cause a problem in the JMAP sync protocol. Because these deletes
are not automatically registered as a change. You can use Entity::getType()->change()
and Entity::getType()->changes() for an example. See the address books's 
`Group <https://github.com/Intermesh/groupoffice/blob/master/www/go/modules/community/addressbook/model/Group.php>`_ 
entity for an example.

Relations with Active Record Models
------------------------------------

Since we are moving from the old ActiveRecord models to our modern JMAP ORM, chances are that at some point you
will need to create relations between entities and older ActiveRecord models.

There is no official support for such relations in GroupOffice, but there is a workaround. Consider the following
example: we have a module named planner, that depends on the `community/tasks` module `legacy/timeregistration2` and
the `legacy/projects` modules.

There is already a JMAP entity named `Task` and it has time registrations connected to it as per the old `pr2_hours`
table in the projects module. We need to aggregate these time registrations for each task. There are roughly three ways
to achieve this, a very bad way, a somewhat hackish, but slightly better way and another hackish way which may or may
not suit your use case.

The bad
```````

In the ``Modules.php`` class (see the :ref:`the server module tutorial <building-a-server-module>` for details), you can
write an event listener function like below:

.. code:: php

	// go\core\modules\community\tasks\Module.php

	public static function defineListeners()
	{
		Task::on(Task::EVENT_MAPPING,  static::class, 'onTaskMap');
	}
	public static function onTaskMap(Mapping $mapping)
	{
		$mapping->addQuery((new Query())->select('COALESCE(SUM(prh.duration), 0) AS timeBooked')->
		// etc..
	}

This may or may not work. In some cases, the use of ``addQuery`` is simply being blocked in case of an override. A poor
alternative would be to edit the ``defineMapping()`` method of the `Task` entity. This has two major disadvantages:

1. **Performance**: Whether you want to or not, you have an extra join and an expensive aggregate function as soon as you try to retrieve tasks. That is not desirable.
2. **Dependencies**: projects2 is an optional module. You will run into trouble as soon as the projects2 module is not installed

In short: just don't!

The ugly
````````

In your custom development module, add a relation, in our case a `HasOne` relation:

.. code:: php

	public static function defineListeners()
	{
		Task::on(Task::EVENT_MAPPING, static::class, 'onTaskMap');
	}
	public static function onTaskMap(Mapping $mapping)
	{
		$mapping->addHasOne('hours', ProjectHoursProperty::class, ['id' => 'task_id'], false);
	}

We also create a property model named ProjectHoursProperty.

.. code:: php

	class ProjectHoursProperty extends Property
	{
		public $task_id = null;
		public $timeBooked;
		protected static function defineMapping()
		{
			return parent::defineMapping()->addTable('pr2_hours', 'prh')->addQuery(
				(new Query())->select('COALESCE(SUM(prh.duration), 0) AS timeBooked')
				->groupBy(['prh.task_id'])
			);
		}

		public function getTimeBooked()
		{
			return $this->timeBooked;
		}

		public function internalSave()
		{
			return true; // but do nothing
		}
	}

As soon as the `hours` relation is requested, a sum of worked hours for the current tasks is retrieved from the old
ActiveRecord model.

.. note:: You may notice the `internalSave()` override. This is automatically called upon saving a task with hours. Since we do not wish to override anything, we just tell the model to do nothing.

Bonus: The good
```````````````

Since worked hours for tasks are being managed in the time registration module, the Task entity can be extended from
within the time registration module. If the time registration module is not enabled, the timeBooked property will
be irrelevant to the task and the extra query will not be added to the mapping.

.. code:: php

	/*
	 * modules\Timeregistration2\Timeregistration2Module.php
	 */
	class Timeregistration2Module extends \GO\Professional\Module
	{

		 // (...)

		public function defineListeners()
		{
		    Task::on(Property::EVENT_MAPPING, static::class, 'onTaskMap');
	    }

		public static function onTaskMap(Mapping $mapping)
		{
			$mapping->addQuery((new Query())
				->select('COALESCE(SUM(prh.duration) * 60, 0) AS timeBooked')
			    ->join('pr2_hours', 'prh', 'prh.task_id = task.id', 'left')
			    ->groupBy(['task.id'])
		    );
	    }

		// (...)
	}



Another bonus: scalars
``````````````````````

In theory, one can use a scalar relation to retrieve related ActiveRecord models for an entity:

.. code:: php

	public static function defineListeners()
	{
		Task::on(Task::EVENT_MAPPING, static::class, 'onTaskMap');
	}
	public static function onTaskMap(Mapping $mapping)
	{
		$mapping->addScalar('hours', 'pr2_hours, ['id' => 'task_id']);
	}

However, since scalar relations merely return identifier fields for said related models, the only possible use case for
using scalars to retrieve related ActiveRecord models is to check whether they exist. If you really want to use scalar
relations in this way, you may want to add the following code to your Entity model:

.. code:: php

	public function hasTimeRegistrations()
	{
		return count($this->hours) > 0;
	}

