Fail2ban
========

Fail2ban can be used to block users after a number of failed login attempts.
It works by monitoring the apache access log for invalid logins.

1. Make sure fail2ban is installed and enabled on your server.

2. Add the authentication failed filter definitions in /etc/fail2ban/filter.d:

      - Web auth in groupoffice.conf::

            # Fail2Ban filter for Group-Office authentication failures
            # logpath must be the webserver error log

            [Definition]

            failregex = Password authentication failed for '\S+' from IP: '<HOST>'
            ignoreregex =

      - Lost password request groupoffice-lost-password.conf::

            # Fail2Ban filter for Group-Office lost password requests
            # logpath must be the webserver error log

            [Definition]

            failregex = Lost password request from IP: '<HOST>'
            ignoreregex =



3. Define the jail in /etc/fail2ban/jail.d/groupoffice.conf::

      [groupoffice]
      enabled = true
      port = http,https
      logpath = /var/log/apache2/error.log
      maxretry = 5

      [groupoffice-lost-password]
      enabled = true
      port = http,https
      logpath = /var/log/apache2/error.log
      maxretry = 100

   .. note:: Make sure the "logpath" value is set to the error log of the webserver.

For more information about Fail2ban and the configuration of it visit https://www.fail2ban.org

.. note:: These filters work from version 6.8.40 and up

.. note:: If you use the Group-Office mailserver then also enable the postfix-sasl, postfix, dovecot, sieve filters.



