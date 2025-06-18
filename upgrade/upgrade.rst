.. _upgrade:

Upgrade
=======

You can upgrade any version from Group-Office, but please make sure to do this in incremental stops:

- 2.18 can upgrade to 3.7.55
- 3.7.55 can upgrade to 6.2
- 6.2 can upgrade to 6.3, 6.3 can upgrade to 6.4, and so on up to 6.8. Every major release needs to be upgraded to the next from 6.2 and higher.
- 6.8 can upgrade to 25.0


Tips
----

Make sure your system meets the :ref:`system-requirements`. In between certain versions it may be possible or even
necessary to update your PHP version first. Please see the release notes for each major version.

Needless to say, but always make a **backup** of your configuration, database and files before upgrading.

After each update to a major version, please make sure to empty your client side cache for your GO instance or do a hard
refresh (e.g. with Ctrl+F5).

License
-------

When you have a professional, billing and/or documents package, please make sure to enter the correct license before starting the upgrade.
License tokens are updated for each major version and they are backwards compatible. That is: if you are licensed for version 25.0, you will
also be licensed for each earlier version.

Here's how to obtain the updated license key:

- Within your browser, navigate to https://www.group-office.com/
- In the top menu, select "My Account"
- Select the card labeled "Contracts". Your licenses, old and current, are listed in a table. Click the license for the instance you wish to upgrade.
- Log onto your server, move to the Group-Office installation folder and run the following command::

    sudo -u www-data php ./cli.php core/System/setLicense --key=<YOURKEY>

Changes
-------

You can find the change log here:

https://github.com/Intermesh/groupoffice/blob/master/CHANGELOG.md

Release notes are posted to our blog:

https://www.group-office.com/blog/


.. toctree::
   :maxdepth: 2

   Debian / Ubuntu <debian>
   Docker <docker>
   Tarball <tarball>
