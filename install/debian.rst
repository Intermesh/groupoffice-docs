.. _install-debian:

Installation on Debian or Ubuntu
================================

Core system
-----------

Our preferred way of installing is using our Debian packages:

1. On Debian login as the root server and on Ubuntu become root by running::

      sudo -s
      
2. When installing 6.6 on Ubuntu Impish 20.10 or higher you need to install PHP 7.4. See https://groupoffice.blogspot.com/2022/02/ubuntu-impish-2110.html
   
   Group-Office 6.7 (currently in unstable) will run on PHP 7.3 or higher including PHP 8.1.

3. First add our repository to the package management system::

     echo "deb http://repo.group-office.com/ sixsix main" > /etc/apt/sources.list.d/groupoffice.list
     
   Or if you want to try our bleeding edge development then add::
   
     echo "deb http://repo.group-office.com/ testing main" > /etc/apt/sources.list.d/groupoffice.list

4. Add our public key::

      wget -O- https://repo.group-office.com/downloads/groupoffice.gpg | gpg --dearmor | tee /etc/apt/trusted.gpg.d/groupoffice.gpg
      
5. Update APT::

      apt-get update

6. Then install Group-Office by running::

      apt-get install groupoffice
      
      
7. Optionally you can install php-acpu for better performance of the cache::

      apt-get install php-apcu

8. If you purchased **Group-Office Professional licenses** then make sure the 
   `Ioncube loader <http://www.ioncube.com/loaders.php>`_ is installed.
   You might want to use our script: https://github.com/Intermesh/groupoffice/blob/master/scripts/install-ioncube.sh

9. Then visit http://yourserver/groupoffice and the installer should appear:

   .. figure:: /_static/installer.png
      :alt: The Group-Office installer

      The Group-Office installer     

10. Follow the instructions on screen and enjoy Group-Office!


.. _mailserver:

Mailserver
----------

You can also use Group-Office as a complete e-mail platform. It's based on:

1. `Postfix <http://www.postfix.org>`_
2. `Dovecot <https://www.dovecot.org>`_
3. Group-Office module to manage mailboxes in the database

At the moment this is only possible with the Debian / Ubuntu packages.

When Group-Office is already installed you can run::

   apt-get install groupoffice-mailserver

When this command is finished login to Group-Office as admin and install the 
"E-mail domains" module. In this module you can manage the domains, mailboxes
and aliases.

.. figure:: /_static/email-domains.png
   :alt: Manage e-mail domains in Group-Office

   Manage e-mail domains in Group-Office


Serverclient module
```````````````````
The server client allows you to:

1. Create mailboxes when you create a new user
2. Synchronize mailbox passwords when you set a new Group-Office password.

Install the module at Start menu -> modules

Then edit /etc/groupoffice/globalconfig.inc.php or create it if it doesn't exist:

.. code:: php

	<?php
	$config = [
		// GO will connect to this installation to add a mailbox. It is the full url to the Group-Office installation with the postfixadmin module installed.   
		'serverclient_server_url' => 'http://localhost/groupoffice/',
		// A token to authenticate. The token has to be identical on the web and mail server. By default they are the same server so you can just set anything here.

		'serverclient_token' => 'someSecureTokenOfyourChoice',

		// Comma separated list of mailbox domains
		'serverclient_domains' => 'intermeshdev.nl',

		// The email account properties that will be added for the user
		'serverclient_mbroot' => '',
		'serverclient_use_ssl' => false,
		'serverclient_use_tls' => false,
		'serverclient_novalidate_cert' => '0',
		'serverclient_host' => 'localhost',
		'serverclient_port' => 143,
		'serverclient_smtp_host' => 'localhost',
		'serverclient_smtp_port' => 25,
		'serverclient_smtp_encryption' =>'',
		'serverclient_smtp_username' => '',
		'serverclient_smtp_password' => ''
	];

Now when you create a new user you have the option to create::

   <username>@intermeshdev.nl

And when you set your password this account will be updated too.

   .. figure:: /_static/install/create-user-serverclient.png
      :width: 50%

      Option to create mailbox when creating new users

TLS / SSL
`````````

It's required to install SSL certificates for your mailserver to operate 
properly. So obtain an SSL certificate and take these steps:

1. Configure Dovecot IMAP in file */etc/dovecot/conf.d/10-ssl.conf*::

      ssl = yes
      ssl_cert = </etc/letsencrypt/live/YOURHOSTNAME/fullchain.pem
      ssl_key = </etc/letsencrypt/live/YOURHOSTNAME/privkey.pem
      
      


2. Restart dovecot::

      invoke-rc.d dovecot restart
      
3. You can verify the SSL certificate with this command::

      printf 'quit\n' | openssl s_client -connect YOURHOSTNAME:143 -starttls imap | openssl x509 -dates -noout

4. Configure Postfix SMTP with these commands::

      postconf -e 'smtpd_tls_cert_file =/etc/letsencrypt/live/YOURHOSTNAME/fullchain.pem'
      postconf -e 'smtpd_tls_key_file = /etc/letsencrypt/live/YOURHOSTNAME/privkey.pem'

5. Restart postfix::

      invoke-rc.d postfix restart
      
6. You can verify the SSL certificate with this command::

       printf 'quit\n' | openssl s_client -connect YOURHOSTNAME:25 -starttls smtp | openssl x509 -dates -noout
       
Letsencrypt
~~~~~~~~~~~

When using Letsencrypt you'll need a renewal hook to reload dovecot and postix on renewal of the certificates.

Create a file /etc/letsencrypt/renewal-hooks/post/mailservices with this content::

   #!/bin/sh
   systemctl reload postfix
   systemctl reload dovecot

External IMAP access
````````````````````
By default only local connections are allowed. This means only Group-Office can connect. This is very secure but in some cases you want to allow IMAP access from the outside.
You'll have to configure your firewall or router to allow connections to the server on the necessary ports:

- IMAP: 143
- IMAPS: 993

You'll also need to uncomment following line in /etc/dovecot/conf.d/99-groupoffice.conf::

   listen = *
   
Now connect with:

IMAP host: YOURHOSTNAME
TLS encrypttion enabled (Make sure you've setup SSL)
Username: full email address

External SMTP access
````````````````````

.. note:: We recommend to install fail2ban too because spammers will try to abuse your server when you enable SMTP!

External access is possible when using TLS on the submission port (587) with authentication. 

To avoid abuse SMTP access is disabled for accounts by default since version 6.6.139. You can enable external SMTP access in Group-Office at E-mail domains -> Domain -> Mailbox.

If you want to enable it for all you can run this SQL command::

   update pa_mailboxes set smtpAllowed=true;

Anti spam / virus
`````````````````

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

Database credentials
````````````````````

The mailserver connects to the "groupoffice" database to lookup mailboxes, aliases and domains. If you need to change the "groupoffice" database password, username or name. Then you also need to change the login details in these files:

- /etc/dovecot/dovecot-groupoffice-sql.conf.ext
- /etc/postfix/mysql_virtual_mailbox_maps.cf
- /etc/postfix/mysql_virtual_mailbox_domains.cf
- /etc/postfix/mysql_virtual_alias_maps.cf

Afterwards restart postfix and dovecot::

   systemctl restart postfix
   systemctl restart dovecot

.. _install-documents:

Documents
---------

If you purchased the documents package you probably want to install some additional tools required for indexing file contents::

   apt-get install catdoc unzip tar imagemagick tesseract-ocr tesseract-ocr-eng poppler-utils exiv2

These tools provide support for:

- Microsoft Office
- Images
- PDF documents



