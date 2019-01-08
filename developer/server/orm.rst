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
            ->addTable("music_artist")
            ->addRelation('albums', Album::class, ['id' => 'artistId']);
  }

You can see that it maps a table "music_artist" and add's a property 'albums'.

A property must be defined for all database columns the model should use.
There should also be a public $albums property.


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