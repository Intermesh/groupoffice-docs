Object Relational Mapping
=========================

Group Office features an ORM package in go\\core\\orm.

There are two main types of models:

1. Entity: A model that can be changed directly by the user. Such as a Contact.
2. Property: A model that belongs to an Entity. Such as a Contact's E-mail address.


Mapping
-------

Each model must implement the "defineMapping" method. This mapping maps database
tables to the object and defines other models as properties.

For example the "go\\modules\\community\\music\\model\\Artist" model defines:

.. code:: php

  protected static function defineMapping() {
    return parent::defineMapping()
            ->addTable("music_artist", "a")
            ->addRelation('albums', Album::class, ['id' => 'artistId'])
						->addProperty('sumOfTableBIds', "SUM(b.id)", (new Query())->join('test_b', 'bc', 'bc.id=a.id')->groupBy(['a.id']))
  }

You can see that it maps a table "music_artist" and add's a property 'albums'.

A property must be defined for all database columns the model should use.
There should also be a public $albums property.

.. note:: Mappings are cached for performance. When making changes you need to 
   run /install/upgrade.php to rebuild the cache.

	 You can also disable cache in the config.php file::

		$config['core'] = [
			'general' => [
					'cache' => 'go\\core\\cache\\None'
				]
		];

addTable() method
`````````````````
With the addTable() method you map table database columns to object properties.
All protected and public properties of the object that match a database column 
name will be loaded from and saved to that table. You can add multiple tables
to one entity. The primary keys must match or a key mapping can be passed to the
method. See the code documentation for more details.

addRelation() method
````````````````````
With add addRelation() you can map "Property" models with a has one or has many
relation. These properties will be loaded and saved automatically.

.. note:: You can't add relations to other entities. Only "Property" models can
   be mapped. Fetch other entities in the client by key. If you would implement a
   getOtherEntity() method, it would be very hard to synchronize the entities to
   clients. Because each entity keeps it's own sync state. If the "OtherEntity" 
   changes it would mean that this entity would change too.

   If you need to create a method to retrieve another entity on the server side
   only then it's recommended to name it "findOtherEntity()" so it won't become
   a public API property.


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

