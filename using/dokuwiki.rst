.. _dokuwiki:

DokuWiki
========

From the `DokuWiki <https://www.dokuwiki.org>`_ website:

	DokuWiki is a simple to use and highly versatile Open Source wiki software that doesn't require a database. It is loved by users for its clean and readable syntax. The ease of maintenance, backup and integration makes it an administrator's favorite.

...and that's where this documentation page comes in.

Preconditions
-------------


- You need to turn off `suhosin.session.encrypt` in the `suhosin.ini` file to let this module work. Otherwise this module cannot read the GroupOffice session.
- Dokuwiki needs to be installed on the same domain as your GroupOffice installation.
- After this install procedure only users of GroupOffice can login to Dokuwiki.
- If for some reason the configuration params are not applied correctly, then also check the `<dokuwiki_path>/conf/local.php` file.

Installation
------------

.. note:: This applies to DokuWiki version 2013-05-10 "Weatherwax" and later. It has been tested against a recent version


1. Install Dokuwiki on the server.
2. Copy the directory: `.../go/modules/community/docuwiki/lib/plugins/authgroupoffice` to the Dokuwiki installation under `<dokuwiki_path>/lib/plugins/authgroupoffice`.
3. Open the dokuwiki config file found in this location: `[path to dokuwiki]/conf/dokuwiki.php`
4. Set the following config variables:

.. code-block:: php

	$conf['authtype'] = 'authgroupoffice';
	$conf['useacl'] = 1;

5. Define the GroupOffice config file location and Create 2 new variables in the config file:

.. code-block:: php

	define("GO_CONFIG_FILE",'[path to the groupoffice config file]'); ( example: define("GO_CONFIG_FILE",'/var/www/groupoffice-4.0/config.php'); )
	$conf['GO_root']  = '[path to the groupoffice dir]';      ( example: $conf['GO_root'] = '/var/www/groupoffice-4.0/'; )
	$conf['GO_php']   = '[path to the groupoffice php file]'  ( example: $conf['GO_php'] = '/var/www/groupoffice-4.0/www/GO.php'; )



.. note:: To configure which user has management options and which is the superuser set the following options too:

.. code-block:: php

    // ( example: $conf['superuser'] = 'admin,testuser'; )
	$conf['superuser'] = '[superuser]';
	// ( example: $conf['manager'] = 'admin,testuser'; )
	$conf['manager'] = '[manager]';

The modification of the files is now complete. Now log into GroupOffice, go to the Dokuwiki tab and click on "Settings".
Set the correct url and title for Dokuwiki and click on "Ok". (example url: http://localhost/dokuwiki)

Now Dokuwiki should be accessible through GroupOffice.

.. tip:: You may want to disable the login/logout button from DokuWiki. This can be done by editing the file `main.php` of the DokuWiki template. Remove this line:

.. code-block:: php

	<?php tpl_button('login')?>
