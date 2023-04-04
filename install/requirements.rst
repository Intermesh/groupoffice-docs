.. _system-requirements:

System requirements
===================

Group-Office 6.6 has the following requirements in order to be officially supported:

.. table:: Software
   :widths: auto

   ====================  ===========
   Type                  Requirement
   ====================  ===========
   Operating System      Linux / Docker
   Webserver             Apache 2.4.x+ / php-fpm or fastcgi
   Database              MySQL 5.7+ / MariaDB 10.0.5
   Programming language	 PHP 7.2 - 7.4
   ====================  ===========

.. note:: Group-Office will run on Nginx, but we currently have no documentation on this.

PHP 8 support
-------------

Group-Office 6.6 is **not** officially supported with PHP8. We do backport PHP8 compatible code in the 6.6 branch when
possible. The community version may run fine, but the paid modules probably won't.

Required PHP Extensions
+++++++++++++++++++++++

- pcre
- mbstring
- ctype
- date
- iconv
- curl
- zip
- soap
- gd
- pdo
- pdo_mysql (With mysqlnd, nd_pdo_mysql)
- mysqlnd
- calendar

Recommended:

- acpu (for better caching performance)
- ioncube (For professional version with Intermesh support)

.. tip:: The install procedure will warn you if any of these modules is missing.
