IMAP proxy
==========

Webmail systems make lots of imap connections. It's wise to use `imapproxy <http://imapproxy.org>`_ to cache connections to the IMAP server.

Install imapproxy on the webserver and configure it to proxy the imapserver. Accounts can be configured with "localhost" as the hostname and imapproxy will route this to the real IMAP server.

run::

   apt-get install imapproxy ca-certificates

/etc/imapproxy.conf looks like the example below.

You should probablty change at least:

- server_hostname, to the hostname of your IMAP server.
- syslog_prioritymask LOG_WARNING, otherwise it will generate too big log files.
- listen_port, if you're running imapproxy on the same host then use "localhost"
  for "server_hostname" and change "listen_port" to something different than where
  dovecot is actually listening. 1143 for example. Then use 1143 in Group-Office to use
  imapproxy.
- tls_ca_path /etc/ssl/certs/

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
   server_hostname imap.yourserver.com
   
   
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
   
   
   #
   ## server_port
   ##
   ## This setting specifies the port that server_hostname is listening on.
   ## This is the tcp port that we proxy inbound connections to.
   # 
   server_port 143
   
   #
   ## cache_expiration_time
   ##
   ## This setting controls how many seconds an inactive connection will be
   ## cached.
   #
   cache_expiration_time 300
   #cache_expiration_time 150
   
   
   #
   ## proc_username
   ##
   ## This setting controls which username the imap proxy process will run as.
   ## It is not allowed to run as "root".
   #
   proc_username nobody
   
   #
   ## proc_groupname
   ##
   ## This setting controls which groupname the imap proxy process will run as.
   #
   proc_groupname nogroup
   
   
   #
   ## stat_filename
   ##
   ## This is the path to the filename that the proxy server mmap()s to
   ## write statistical data to.  This is the file that pimpstat needs to
   ## look at to be able to provide his useful stats.
   #
   stat_filename /var/run/pimpstats
   
   
   #
   ## protocol_log_filename
   ##
   ## protocol logging may only be turned on for one user at a time.  All
   ## protocol logging data is written to the file specified by this path.
   #
   protocol_log_filename /var/log/imapproxy_protocol.log
   
   
   #
   ## syslog_facility
   ##
   ## The logging facility to be used for all syslog calls.  If nothing is
   ## specified here, it will default to LOG_MAIL.  Any of the possible
   ## facilities listed in the syslog(3C) manpage may be used here except
   ## LOG_KERN.
   #
   syslog_facility LOG_MAIL
   
   
   #
   ## syslog_prioritymask
   ##
   ## This configuration option is provided as a way to limit the verbosity
   ## of imapproxy.  If no value is specified, it will default to no priority
   ## mask and you'll see all possible log messages.  Any of the possible
   ## priority values listed in the syslog(3C) manpage may be used here.
   ## By default, I've left this commented out so you will see all possible
   ## log messages.
   #
   syslog_prioritymask LOG_WARNING
   
   
   #
   ## send_tcp_keepalives
   ##
   ## This determines whether the SO_KEEPALIVE option will be set on all
   ## sockets.
   #
   send_tcp_keepalives no
   
   
   #
   ## enable_select_cache
   ##
   ## This configuration option allows you to turn select caching on or off.
   ## When select caching is enabled, up-imapproxy will cache SELECT responses
   ## from an imap server.
   #
   enable_select_cache no
   
   
   #
   ## foreground_mode
   ##
   ## This will prevent imapproxy from detaching from his parent process and
   ## controlling terminal on startup.
   #
   foreground_mode no
   
   
   #
   ## force_tls
   ##
   ## Force imapproxy to use STARTTLS even if LOGIN is not disabled.
   #
   force_tls yes
   
   
   #
   ## chroot_directory
   ##
   ## This allows imapproxy to run in a chroot jail if desired.
   ## If commented out, imapproxy will not run chroot()ed.  If
   ## a directory is specified here, imapproxy will chroot() to that
   ## directory.
   #
   chroot_directory /var/lib/imapproxy/chroot
   
   
   #
   ## enable_admin_commands
   ##
   ## Used to enable or disable the internal imapproxy administrative commands.
   #
   enable_admin_commands no
   
   
   #
   ## Various path options for SSL CA certificates/directories
   #
   #tls_ca_file /usr/share/ssl/certs/ca-bundle.crt
   tls_ca_path /etc/ssl/certs/
   #tls_cert_file /usr/share/ssl/certs/mycert.crt
   #tls_key_file /usr/share/ssl/certs/mycert.key


Updating accounts
-----------------
You can of course update accounts one by one but you can also use this SQL command to do it all at once::

   update em_accounts set port = 1143 where host='localhost';
   
   
Managesieve
-----------
If you use manage sieve too, you need to tell Group-Office that localhost actually points to an external mailserver via the proxy. Edit config.php and add::

   $config['sieve_rewrite_hosts']='localhost=mail.example.com';
