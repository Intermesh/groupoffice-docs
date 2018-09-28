Mailserver
==========

You can also use Group-Office as a complete e-mail platform. It's based on:

1. `Postfix <http://www.postfix.org>`_
2. `Dovecot <https://www.dovecot.org>`_
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


Upgrade
-------

If you're upgrading from a previous 6.3.x or higher version simply run::

   apt-get install groupoffice-mailserver

Upgrading from 6.2
``````````````````

1. To upgrade from 6.2 you must start with a clean system by removing all previous
software and configuration. **Make a backup!**::

      apt-get purge groupoffice-mailserver dovecot* postfix* clamav* spamassassin amavisd-new

2. Then install the new package::

      apt-get install groupoffice-mailserver

3. Move the mail to the new location::

      mv /home/vmail/* /var/mail/vhosts
      rmdir /home/vmail

4. Remove no longer required packages::
      
      apt-get autoremove
   
Anti spam / virus
-----------------
The package above installs the bare minimum so you can be free to configure your
system in your own way. But for your convenience we've also prepared an anti 
spam and anti virus solution based on:

1. `rspamd <https://www.rspamd.com>`_
2. `clamav <http://www.clamav.net>`_

To install take these steps:

1. Add the rspamd repository because the official Debian repositories contain
   outdated versions::

      apt-get install -y lsb-release wget # optional
      CODENAME=`lsb_release -c -s`
      wget -O- https://rspamd.com/apt-stable/gpg.key | apt-key add -
      echo "deb [arch=amd64] http://rspamd.com/apt-stable/ $CODENAME main" > /etc/apt/sources.list.d/rspamd.list
      echo "deb-src [arch=amd64] http://rspamd.com/apt-stable/ $CODENAME main" >> /etc/apt/sources.list.d/rspamd.list        

2. Update APT::

      apt-get update
  
3. Install groupoffice-mailserver-antispam::

      apt-get install groupoffice-mailserver-antispam

4. Run the rspamd config wizard::

      rspamadm configwizard

5. Test if the spam filter works by sending a `GTUBE <https://en.wikipedia.org/wiki/GTUBE>`_ message

6. Test if the anti virus works by sending an `EICAR test file <https://en.wikipedia.org/wiki/EICAR_test_file>`_

7. Checkout the rspamd Web GUI at http://yourserver/rspamd/
