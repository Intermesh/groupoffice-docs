.. _translations:

Translations
============

Group-Office comes in many languages thanks to our community!

At the moment we have the following:

- Arabic عربي 
- বাংলা (Bangladesh)
- 한국어
- Català
- Chinese Simplified
- Chinese Traditional
- Čeština
- Dansk
- Deutsch
- English/American
- English/British
- Español
- Estonian
- Ελληνικά
- Francais
- Hrvatski
- Italiano
- Magyar
- Nederlands
- Norsk bokmål
- Polski
- Português - Brazil
- Pусский
- Romanian
- Suomi - Finland
- Svenska
- Türkçe
- ไทย
- Tiếng Việt
- Български

Contribute
----------

We've made it easy for you to contribute to translations. You can download all language as a spreadsheet. 
Make the translations and send it to support@intermesh.nl. Then we can import it into the project and 
include it in the next release.

You can find the **download spreadsheet** button next to the language selection in **System Settings -> General**.

.. note:: If you want to import the language CSV file yourself then install the Community / Developer tools module you
    and run the following command in a terminal:

    .. code::

        ./cli.php community/dev/Language/import --path=lang.csv

.. _customize-language:

Customize
---------

It's possible to customize language by overriding the default language string. For example if you want to rename "Address book" to "Contact" you create this file in the Admin personal file area::

   language/legacy/addressbook/en.php
   
So this is language/<MODULE PACKAGE>/<MODULE NAME>/<LANGCODE>.php

Enter this PHP code in the file::

   <?php
   return [
    "Address book" => "Contacts"
   ];
   
   
After placing the file run /install/upgrade.php to rebuild the server cache. Then check if the address book tab text changed into "Contacts".
   
