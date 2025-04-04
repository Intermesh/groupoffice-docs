
JMAP API
==========

This part explains how you can use the `JMAP API <https://jmap.io>`_ from 3rd party software. With the API you can control every function in Group-Office. Via the link below you can find various example PHP scripts that use cUrl to make API requests like:

- Create contacts
- Send newsletters
- Upload files
- Send e-mail

API key
-------

First make sure the "API keys" module from the 'Community' package is installed at
System settings -> modules.

Then visit System settings -> API Keys and add a token.

.. figure:: /_static/developer/jmap/apikeys.png
   :width: 100%

Obtain the token via the more menu and choose "View token".

API Methods
-----------

From v25 you can view the methods on your API on https://your.host/api/doc.php

For example: https://demo.groupoffice.net/api/doc.php

Example script
--------------

You can find some example PHP scripts to use the JMAP API here:

https://github.com/Intermesh/groupoffice/tree/master/www/go/modules/community/apikeys/examples

You can of course use any programming language with the JMAP API.
