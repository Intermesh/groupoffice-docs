.. _system-requirements:

System requirements
===================

Group-Office 6.8 has the following requirements in order to be officially supported:

.. table:: Software
   :widths: auto

   ====================  ===========================================================
   Type                  Requirement
   ====================  ===========================================================
   Operating System      Linux / Docker
   Webserver             Apache 2.4.x+ / php-fpm or fastcgi
   Database              MySQL 5.7+ / MariaDB 10.0.5+
   Programming language	 PHP 8.1 or 8.2
   ====================  ===========================================================

.. note:: Group-Office will run on Nginx + fpm, but we currently have no documentation on this.

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
- intl

Recommended:

- acpu (for better caching performance)
- SourceGuardian (For professional version with Intermesh support)

.. tip:: The install procedure will warn you if any of these modules is missing.
