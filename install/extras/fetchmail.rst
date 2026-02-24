Use fetchmail with POP3 on a remote catch-all mailbox for local delivery
========================================================================

You might already have a remote POP-3 mailbox that handles all your mail. When you setup GroupOffice in your office it
can be very useful to save the remote mail in local mailboxes so you don't have to buy a lot of diskspace at your mail
provider and you get optimal speed when reading the mail. For this setup we assume you have installed the GroupOffice
:ref:`mailserver`.

First setup yourdomain.com in GroupOffice at the E-mail domains (postfixadmin) module. Configure all mailboxes.

.. note:: Use the real domain and no fake domain on the group-office server. Otherwise the mail will loop infinitely.
   Fetchmail will try to deliver to the real domain.

After that install fetchmail::

    apt-get install fetchmail

edit /etc/default/fetchmail and change::

    START_DAEMON=yes

Create or edit /etc/fetchmailrc::

    poll mailserverof.provider.com localdomains yourmaildomain.com
        envelope X-Envelope-To
        user catchallusernam@yourdomain.com with pass yourpassword to * here smtphost localhost
        limit 20480000 #Make sure the limit is set to the max message size of postfix. Otherwise it can result in fetchmail trying to get the message forever and waste resources!

Change the permissions::

    chmod 0710 /etc/fetchmailrc
    chown root:root /etc/fetchmailrc

Now start the deamon::

    /etc/init.d/fetchmail start

You should see information logged in /var/log/mail.info.

You can find more information and configuration examples in the Fetchmail manual at https://www.fetchmail.info