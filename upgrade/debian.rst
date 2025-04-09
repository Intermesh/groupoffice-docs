Upgrading on Debian / Ubuntu
============================

Core system
-----------

Running 6.3 or higher
`````````````````````

To upgrade minor releases run:

.. code:: bash

   apt-get update
   apt-get install groupoffice

This will install the new software and upgrades the database.
When Group-Office open Group-Office now they will get a message that the service is unavailable at this time because an
upgrade is being installed.

.. note:: If for any reason you see a maintenance screen when launching Group-Office. Then launch /install to upgrade the database or run it on the command line::

     sudo -u www-data /usr/share/groupoffice/cli.php core/System/upgrade -c=/etc/groupoffice/config.php

Major release upgrade
~~~~~~~~~~~~~~~~~~~~~
When the second digit increases in the version number we call this a major release. For example when upgrading to 6.4 from 6.3.
When upgrading to the next major release follow these steps prior to the above:

1. Run the above command first to upgrade to the latest 6.x

2. Then open your browser to update the database.

3. Make sure to install the latest license key from your group-office.com account in the
   contracts section (https://www.group-office.com/account#account/contracts) if you run
   the professional version. This can be done via the browser GUI in the main menu -> register or via CLI::

      sudo -u www-data php ./cli.php core/System/setLicense --key=<YOURKEY>

4. Major release upgrades can't be skipped so you need to do them step by step.
   Adjust the repository to the next major release in '/etc/apt/sources.list.d/groupoffice.list':

    - For 25.0 change it to:

        deb http://repo.group-office.com/ twentyfivezero main

    For older versions switch to the older manuals:

        https://groupoffice.readthedocs.io/en/6.8/
        https://groupoffice.readthedocs.io/en/6.7/
        https://groupoffice.readthedocs.io/en/6.6/


Mailserver
----------

If you're upgrading from 6.3.x or higher version run::

   apt-get install groupoffice-mailserver

.. note:: When upgrading from 6.8 to 25.0 it will ask to replace modified configuration files for Postfix mysql (/etc/postfix/mysql_*). Answer YES here as the database tables changed.

Or if you also installed the anti spam and virus package:

   apt-get install groupoffice-mailserver groupoffice-mailserver-antispam

Upgrading from 6.2
``````````````````

Visit an older version of the manual here:

https://groupoffice.readthedocs.io/en/6.8/
