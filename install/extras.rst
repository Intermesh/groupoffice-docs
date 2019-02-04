Extras
======

Fail2ban
--------

Fail2ban can be used to block users after a number of failed login attempts.
It works by monitoring the apache access log for invalid logins.

1. Make sure fail2ban is installed and enabled on your server.

2. Add the filter definition to /etc/fail2ban/jail.d/groupoffice.conf::

      [Definition]
      failregex = <HOST> - - .*auth.php.* 401\s 
      ignoreregex =


3. Define the jail in /etc/fail2ban/jail.d/groupoffice.conf::

      [groupoffice]
      enabled = true
      port = http,https
      filter = groupoffice
      logpath = /var/log/apache2/access.log
      maxretry = 3

For more information about Fail2ban and the configuration of it visit https://www.fail2ban.org

.. note:: This works from 6.3.62 and up.