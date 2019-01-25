Router
======

Group-Office has 3 routers:

1. The JMAP router for routing JMAP requests. See https://jmap.io/spec-core.html
2. The CLI router for routing Command Line Interface commands
3. A download hash for routing download id's to a method.


JMAP Router
-----------

The standard JMAP calls are already built in. Every Entity is registered in the 
"core_entity" table. The router uses this table to find the corresponding module.
For example method call "Contact/get" is mapped to PHP class::

   go\modules\community\addressbook\controller\Contact
   
and public method::

   get($params); 
   
All parameters are passed in the $params argument.

CLI Router
----------

There's also a command line interface router. :ref:`Read more about that here <cli>`

Download router
---------------
All downloads go through "download.php?blob=<HASH>". The <HASH> is typically a 
hash pointing to a BLOB on the system. But it can also contain a route to a special 
download method defined in the Module.php file of the module.
Methods prefixed with "download" can be accessed. For example method::

   go\modules\community\addressbook\Module::downloadVcard($contactId);
   
can be accessed with::

   download.php?blob=community/addressbook/vcard/1
