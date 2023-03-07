.. _install:

Installation
============

This section is for system administrators that want to install Group-Office
on a self hosted server.

There are various ways to install Group-Office. We recommend to install our
Debian packages on the latest stable Debian Linux OS.

Group-Office 6.6 has the following requirements in order to be officially supported:

- Linux OS
- Apache 2.4.x
- PHP 7.2 up to PHP 7.4 - newer is better!
- Mysql from 5.7.0 or MariaDB from 10.0.5
- A running cron daemon

Group-Office 6.6 is **not** officially supported with PHP8.1 . We do backport PHP8 compatible code in the 6.6 branch when
possible. The community version may run fine, but the paid modules probably won't.

.. note:: Group-Office will run on Nginx, but we currently have no documentation on this.
.. tip:: There are several PHP modules that need to be installed in order for Group-Office to run. The test script will warn you if any of these modules is missing.


.. toctree::
   :maxdepth: 2

   Debian / Ubuntu <debian>
   Docker <docker>
   Tarball <tarball>
   extras/extras.rst
   config
