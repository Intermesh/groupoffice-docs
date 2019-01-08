.. _dal:

Database Abstraction Layer
==========================

Group Office has a powerful database abstraction layer to make database queries.
It's designed to be as close to regular SQL as possible but to minimize the risk 
of security problems such as SQL injections.

For testing these queries I would suggest to use a :ref:`cli`. controller. You
can simply extend the CliDemo controller from the Music demo module.


Select query
------------

First create a helper function in the controller used to print results:

.. code:: php

  private function printQuery(Query $query) {
    //Query objects are traversable, but you can also use $query->single() to 
    //fetch a single record or $query->all() to fetch all in an array.    
    foreach($query as $record) {      
      foreach($record as $key => $value) {
        echo $key . ": " . var_export($value, true) . "\n";
      }
      echo "-----\n";
    }
  }


Then create this select function. It demonstrates basic usage. It also shows
you can easily print SQL queries for debugging.

.. code:: php

  public function select() {
    
    //Build new select query object
    $query = (new Query())
            ->select('*')
            ->from('music_artist')            
            ->orderBy(['name' => 'ASC']);
    
    //Query objects can be stringified for debugging
    echo $query . "\n";
    
    $this->printQuery($query);    
    
    //Quick way to fetch single result
    $record = (new Query)
            ->select('id, name')
            ->from('music_artist')
            ->single();
    
    var_dump($record);
  }
  
Run these queries by executing::

  docker-compose exec --user www-data groupoffice php /usr/local/share/groupoffice/cli.php community/music/cliDemo/select



Joins
`````

The next example shows how to make a join with a GROUP BY.

.. code:: php

  public function join() {
    // Join example with aliases for the table names
    $query = (new Query)
            ->select('art.id, art.name, count(alb.id) as albumCount')
            ->from('music_artist', 'art')
            ->join('music_album', 'alb', 'art.id = alb.artistId')
            ->groupBy(['art.id']);
            
    
    $this->printQuery($query);
  }

Where conditions
````````````````

Here's the simplest example:

.. code:: php

   $query = (new Query)
            ->select('id, name')
            ->from('music_artist')
            ->where('name', '=' , 'The Doors');

The same query can be written like this:

.. code:: php

   $query = (new Query)
            ->select('id, name')
            ->from('music_artist')
            ->where(['name' => 'The Doors']);

Or with a string and bind parameters:

.. code:: php

   $query = (new Query)
            ->select('id, name')
            ->from('music_artist')
            ->where('name = :name')
            ->bind(['name' => 'The Doors']);
   

Array values are automatically processed as IN conditions:

.. code:: php

   $query = (new Query)
            ->select('id, name')
            ->from('music_artist')
            ->where(['name' => ['The Doors', 'The war on drugs']]);

You can use a go\core\db\Criteria object for sub groups:

.. code:: php

  $query = (new Query)
              ->select('id, name')
              ->from('music_artist')
              // Select only artists that were created in the past 3 hours.
              ->where('createdAt', '>=', new DateTime("-3 hours"))            
              ->andWhere(
                      // This will become a grouped where condition between parenthesis
                      (new Criteria())
                      ->where(['name' => 'The Doors'])
                      ->orWhere(['name' => 'The war on drugs'])
                      );


Sub queries
```````````

Here's an example of a WHERE EXISTS subquery:


.. code:: php

   $query = (new Query)
            ->select('id, name')
            ->from('music_artist', 'art')
            ->whereExists(
                    (new Query)
                    ->select('*')
                    ->from('music_album', 'alb')
                    ->where('alb.artistId = art.id')
                    );


And here's how to do an IN subquery:


.. code:: php

   $query = (new Query)
            ->select('id, name')
            ->from('music_album', 'alb')
            ->where('artistId', 'IN',
                    (new Query)
                    ->select('id')
                    ->from('music_artist', 'art')
                    ->where('art.createdAt', '>' , new DateTime("-3 hours"))
                    );


Expressions
-----------

Sometimes it's useful to pass raw expressions to the Query object. You can use
a go\core\db\Expression object to do this. Here's an example:

.. code:: php

   $query = (new Query)
            ->select('art.id, art.name, count(alb.id) as albumCount')
            ->from('music_artist', 'art')
            ->join('music_album', 'alb', 'art.id = alb.artistId')
            ->groupBy(['art.id'])

            //Normally group by expects a [column => ASC] array but you can use 
            //functions with an Expression object
            ->orderBy([new Expression("count(alb.id) DESC")]);     