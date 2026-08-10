Upgrading on Debian / Ubuntu
============================

Core system
-----------

When upgrading a major version other than the latest version, it is recommended to refer to the documentation of the target version:

- https://groupoffice.readthedocs.io/en/25.0/
- https://groupoffice.readthedocs.io/en/6.8/
- https://groupoffice.readthedocs.io/en/6.7/
- https://groupoffice.readthedocs.io/en/6.6/


Running 6.3 or higher
`````````````````````

To upgrade minor releases run:

.. code:: bash

   apt-get update
   apt-get install groupoffice

This will install the new software and upgrades the database.
When GroupOffice open GroupOffice now they will get a message that the service is unavailable at this time because an
upgrade is being installed.

.. note:: If for any reason you see a maintenance screen when launching GroupOffice. Then launch /install to upgrade the database or run it on the command line::

     sudo -u www-data /usr/share/groupoffice/cli.php core/System/upgrade -c=/etc/groupoffice/config.php

Major release upgrade
~~~~~~~~~~~~~~~~~~~~~

Up to version 6.8, when the second digit increases in the version number we call this a major release. For example the
upgrade to 6.8 from 6.7 is considered a major upgrade.

After 6.8, we switched to a yearly versioning scheme. If the second digit is higher than zero, it should be considered
a major update as well (e.g. 26.1 versus 26.0). Otherwise, you can release to the following year (25.0 to 26.0, etcetera).

When upgrading to the next major release follow these steps prior to the above:

1. Upgrade to the latest release of your current version as described above.

2. By default, the database should upgrade automatically. If not, open your browser to update the database.

3. Make sure to install the latest license key from your group-office.com account in the
   contracts section (https://www.group-office.com/account#account/contracts) if you run
   the professional version. This can be done via the browser GUI in the main menu -> register or via CLI::

      sudo -u www-data php ./cli.php core/System/setLicense --key=<YOURKEY>

4. Major release upgrades can't be skipped so you need to do them step by step.
   Adjust the repository to the next major release in ``/etc/apt/sources.list.d/groupoffice.list``::

    deb http://repo.group-office.com/ twentysixzero main

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

Unattended upgrades
-------------------

To keep GroupOffice up to date automatically you may want to use the package unattended upgrades.

Here's how to set up unattended-upgrades for groupoffice on Debian/Ubuntu:

1. Install unattended-upgrades::

      apt-get install unattended-upgrades

2. Configure origin patterns, add the line below (On Debian this section is already present but on Ubuntu you may have to add the new section)::

    Unattended-Upgrade::Origins-Pattern {

    	"site=repo.group-office.com,n=twentysixzero"; // add this entry for groupoffice

    }
3. Enable automatic upgrades
   Edit or create /etc/apt/apt.conf.d/20auto-upgrades::

      APT::Periodic::Update-Package-Lists "1";
      APT::Periodic::Unattended-Upgrade "1";

   The "1" means daily. Set to "7" for weekly, etc.

4. Test your config without actually installing::

      unattended-upgrade --dry-run --debug

   This shows which packages would be upgraded and why others are excluded.

5. Run it manually once to verify::

      unattended-upgrade -v


Now the system will check for GroupOffice updates daily.
