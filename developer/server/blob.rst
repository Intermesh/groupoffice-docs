Binary Large Objects
====================

Group Office has a BLOB system to store files. When uploading a file a unique
hash is calculated for the file to identify it. So when the same file is stored
more than once in Group Office it will only be saved to disk once.
You don't have to worry about uploading or downloading the data. Because this 
has already been implemented for you.

Database
--------

In the database you can store the BLOB id in a BINARY (40) type column. 

.. warning:: It's very important that a foreign key constraint is defined for the 
   BLOB id when it's used in a table. Because the garbage collection mechanism
   uses these keys to determine if a BLOB is stale and to be cleaned up. In 
   other words if you don't do this your BLOB data will be removed automatically.


Download / Upload URL's
-----------------------

You can get the download and upload URL's by doing a GET request to the auth.php 
endpoint. 

Also read: https://jmap.io/spec-core.html#binary-data

Using
-----

In the webclient you can use for uploading:

- go.form.FileField(config) : https://github.com/Intermesh/groupoffice/blob/master/www/go/core/views/extjs3/form/FileField.js
- go.util.openFileDialog(config) : https://github.com/Intermesh/groupoffice/blob/master/www/go/core/views/extjs3/util.js

And for downloading:

- go.Jmap.downloadUrl(blobId) : https://github.com/Intermesh/groupoffice/blob/master/www/go/core/views/extjs3/Jmap.js


.. note: The address book module is a good example of storing a blob as a photo in the Contact entity. 


