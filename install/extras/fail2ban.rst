Fail2ban
========

Fail2ban can be used to block users after a number of failed login attempts.
It works by monitoring the apache access log for invalid logins.

1. Make sure fail2ban is installed and enabled on your server.

2. Add the authentication failed filter definition to /etc/fail2ban/filter.d/groupoffice-auth.conf::

      [Definition]
      failregex = <HOST> - - .*auth.php.* 401\s
      ignoreregex =

3. Add the lost password request filter definition to /etc/fail2ban/filter.d/groupoffice-lost-password.conf::

      [Definition]
      failregex = <HOST> - - .*auth.php.* 202\s
      ignoreregex =


4. Define the jail in /etc/fail2ban/jail.d/groupoffice.conf::

      [groupoffice-auth]
      enabled = true
      port = http,https
      filter = groupoffice
      logpath = /var/log/apache2/access.log
      maxretry = 3

      [groupoffice-lost-password]
      enabled = true
      port = http,https
      filter = groupoffice
      logpath = /var/log/apache2/access.log
      maxretry = 100

   .. note:: Make sure the "logpath" value is set to the access log of the webserver.

For more information about Fail2ban and the configuration of it visit https://www.fail2ban.org

.. note:: The auth filter works from 6.3.62 and up. The lost password works from 6.8.39 and up.

.. note:: If you use the Group-Office mailserver then also enable the sasl, dovecot and postfix filters.



