Mailserver
==========

You can also use Group-Office as a complete e-mail platform. It's based on:

1. Postfix
2. Dovecot
3. Group-Office module to manage mailboxes in the database

Install
-------

At the moment this is only possible with the Debian / Ubuntu packages.
When Group-Office is already installed you can run:

.. code:: bash

   apt-get install groupoffice-mailserver

TLS / SSL
`````````

It's required to install SSL certificates for your mailserver to operate 
properly. So obtain an SSL certificate and take these steps:

1. Configure Dovecot IMAP in file */etc/dovecot/conf.d/10-ssl.conf*::

      ssl = yes
      ssl_cert = </etc/ssl/group-office.com/certificate.crt
      ssl_key = </etc/ssl/group-office.com/certificate.key
      ssl_ca = </etc/ssl/group-office.com/cabundle.crt

2. Restart dovecot::

      invoke-rc.d dovecot restart

3. Configure Postfix SMTP with these commands::

      postconf -e 'smtpd_tls_cert_file = /etc/ssl/group-office.com/certificate.crt'
      postconf -e 'smtpd_tls_key_file = /etc/ssl/group-office.com/certificate.key'
      postconf -e 'smtpd_tls_CAfile = /etc/ssl/group-office.com/cabundle.crt'

4. Restart postfix::

      invoke-rc.d postfix restart
   
Anti spam / virus
-----------------
The package above installs the bare minimum so you can be free to configure your
system in your own way. But for your convenience we've also prepared an anti 
spam and anti virus solution based on:

1. rspamd
2. clamav

To install run:

.. code:: bash

   apt-get install groupoffice-mailserver-antispam