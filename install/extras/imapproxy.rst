IMAP proxy
==========

Webmail systems make lots of imap connections. It's wise to use `imapproxy <http://imapproxy.org>`_ to cache connections to the IMAP server.

Install imapproxy on the webserver and configure it to proxy the imapserver. Accounts can be configured with "localhost" as the hostname and imapproxy will route this to the real IMAP server.

run::

   apt-get install imapproxy ca-certificates

/etc/imapproxy.conf looks like this (Don't forget to add "tls_ca_path /etc/ssl/certs/"):

.. note:: If you're running imapproxy on the same host then use "localhost"
   for "server_hostname" and change "listen_port" to something different than where
   dovecot is actually listening. 1143 for example. Then use 1143 in Group-Office to use
   imapproxy

.. code::

   ## imapproxy.conf
   ##
   ## This is the global configuration file for imapproxy.
   ## Lines beginning with a '#' sign are treated as comments and will be
   ## ignored.  Each line to be processed must be a space delimited
   ## keyword/value pair.
   ##

   #
   ## server_hostname
   ##
   ## This setting controls which imap server we proxy our connections to.
   #
   server_hostname imap.example.com


   #
   ## connect_retries
   ##
   ## This setting controls how many times we retry connecting to our server.
   ## The delay between retries is configurable with 'connect_delay'
   #
   connect_retries 10
   connect_delay 5

   #
   ## cache_size
   ##
   ## This setting determines how many in-core imap connection structures
   ## will be allocated.  As such, it determines not only how many cached
   ## connections will be allowed, but really the total number of simultaneous
   ## connections, cached and active.
   #
   cache_size 3072


   #
   ## listen_port
   ##
   ## This setting specifies which port the proxy server will bind to and
   ## accept incoming connections from.
   #
   listen_port 143


   #
   ## listen_address
   ##
   ## This setting specifies which address the proxy server will bind to and
   ## accept incoming connections to.  If undefined, bind to all.
   ## Must be a dotted decimal IP address.
   #
   #listen_address 127.0.0.1


   tls_ca_path /etc/ssl/certs/


Updating accounts
-----------------
You can of course update accounts one by one but you can also use this SQL command to do it all at once::

   update em_accounts set port = 1143 where host='localhost';
   
   
Managesieve
-----------
If you use manage sieve too, you need to tell Group-Office that localhost actually points to an external mailserver via the proxy. Edit config.php and add::

   $config['sieve_rewrite_hosts']='localhost=mail.example.com';
