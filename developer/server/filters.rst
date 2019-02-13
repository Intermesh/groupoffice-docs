Filters
=======

Entities can be filtered according to the `JMAP filter specification <https://jmap.io/spec-core.html#/query>`_.

You can implement filters by overriding the "defineFilters" method in your
Entity. Here's an advanced example of the Contact filters:

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
										->add("addressBookId", function(Criteria $criteria, $value) {
											$criteria->andWhere('addressBookId', '=', $value);
										})
										->add("groupId", function(Criteria $criteria, $value, Query $query) {
											$query->join('addressbook_contact_group', 'g', 'g.contactId = c.id');
											
											$criteria->andWhere('g.groupId', '=', $value);
										})
										->add("isOrganization", function(Criteria $criteria, $value) {
											$criteria->andWhere('isOrganization', '=', $value);
										})
										->add("hasEmailAddresses", function(Criteria $criteria, $value, Query $query) {
											$query->join('addressbook_email_address', 'e', 'e.contactId = c.id', "LEFT")
											->groupBy(['c.id'])
											->having('count(e.id) '.($value ? '>' : '=').' 0');
										})
										->addText("email", function(Criteria $criteria, $comparator, $value, Query $query) {
											$query->join('addressbook_email_address', 'e', 'e.contactId = c.id', "INNER");
											
											$criteria->where('e.email', $comparator, $value);
										})
										->addText("name", function(Criteria $criteria, $comparator, $value) {											
											$criteria->where('name', $comparator, $value);
										})
										->addText("country", function(Criteria $criteria, $comparator, $value, Query $query) {
											if(!$query->isJoined('addressbook_address')) {
												$query->join('addressbook_address', 'adr', 'adr.contactId = c.id', "INNER");
											}
											
											$criteria->where('adr.country', $comparator, $value);
										})
										->addText("city", function(Criteria $criteria, $comparator, $value, Query $query) {
											if(!$query->isJoined('addressbook_address')) {
												$query->join('addressbook_address', 'adr', 'adr.contactId = c.id', "INNER");
											}
											
											$criteria->where('adr.city', $comparator, $value);
										})
										->addNumber("age", function(Criteria $criteria, $comparator, $value, Query $query) {
											
											if(!$query->isJoined('addressbook_date')) {
												$query->join('addressbook_date', 'date', 'date.contactId = c.id', "INNER");
											}
											
											$criteria->where('date.type', '=', Date::TYPE_BIRTHDAY);					
											$tag = ':age'.uniqid();
											$criteria->andWhere('TIMESTAMPDIFF(YEAR,date.date, CURDATE()) ' . $comparator . $tag)->bind($tag, $value);
											
										})
										->addDate("birthday", function(Criteria $criteria, $comparator, $value, Query $query) {
											if(!$query->isJoined('addressbook_date')) {
												$query->join('addressbook_date', 'date', 'date.contactId = c.id', "INNER");
											}
											
											$tag = ':bday'.uniqid();
											$criteria->where('date.type', '=', Date::TYPE_BIRTHDAY)
																->andWhere('DATE_ADD(date.date, 
																		INTERVAL YEAR(CURDATE())-YEAR(date.date)
																						 + IF(DAYOFYEAR(CURDATE()) > DAYOFYEAR(date.date),1,0)
																		YEAR)  
																' . $comparator . $tag)->bind($tag, $value->format(Column::DATE_FORMAT));
										});
										
	}



When this has been implemented you can do use it in a Foo/query call like this:

.. code:: json

   {"filter": {"addressBookId" : [1, 2]}}


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
		$filters->add('isIntermediair', function(Criteria $criteria, $value, Query $query) {
			if($value) {
				$query	->join('applications_application', 'a', 'a.createdBy = u.id')
								->groupBy(['u.id']);

				//We don't want to use the Users acl but the applications acl.
				Acl::applyToQuery($query, 'a.aclId');
			}							
		});
	}

