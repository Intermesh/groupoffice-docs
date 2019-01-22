Filters
=======

Entities can be filtered according to the `JMAP filter specification <https://jmap.io/spec-core.html#/query>`_.

You can implement filters by overriding the "defineFilters" method in your
Entity. Here's an example of a "genres" filter:

.. code:: php

	/**
	 * Defines JMAP filters
	 * 
	 * Adds the 'genres' filter which can be an array of genre id's.
	 * 
	 * @link https://jmap.io/spec-core.html#/query
	 * 
	 * @return Filters
	 */
	protected static function defineFilters() {
		return parent::defineFilters()
						->add('genres', function (Query $query, $value, array $filter) {
							if(!empty($value)) {
								$query->join('music_album', 'album', 'album.artistId = artist.id')
									->groupBy(['artist.id']) // group the results by id to filter out duplicates because of the join
									->where(['album.genreId' => $value]);	
							}
						});
	}


When this has been implemented you can do use it in a Foo/query call like this:

.. code:: json

   {"filter": {"genres" : [1, 2]}}


Quick search
------------

By default a "q" filter is already defined. You can use it by specifying the
text fields to search in the method "searchColumns":

.. code:: php

   protected static function searchColumns() {
	   return ['name'];
	 }

You can use it like this:

.. code:: json

   {"filter": {"q" : "test"}}


ACL Permission level
--------------------

If the entity is derived from an AclEntity then the filter "permissionLevel" is
also available:

.. code:: json

   {"filter": {"permissionLevel" : GO.permissionLevels.write}}

By default entities are filtered on read permissions.


Extend filters with modules
---------------------------

You can also extend filters using the Entity::EVENT_FILTER :ref:`event <events>`.

For example:

.. code:: php

	public function defineListeners() {
		User::on(User::EVENT_FILTER, static::class, 'onUserFilter');		
	}
	
	/**
	 * Extends the User filters with "isIntermediair". So we can show only
	 * users that are being an intermediair.
	 * 
	 * @param Filters $filters
	 */
	public static function onUserFilter(Filters $filters) {		
		$filters->add('isIntermediair', function(Query $query, $value, array $filter) {
			if($value) {
				$query	->join('applications_application', 'a', 'a.createdBy = u.id')
								->groupBy(['u.id']);

				//We don't want to use the Users acl but the applications acl.
				Acl::applyToQuery($query, 'a.aclId');
			}							
		});
	}

