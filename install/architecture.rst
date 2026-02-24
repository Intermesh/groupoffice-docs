GroupOffice Architecture
=========================

GroupOffice consists of the following services which we all host with Debian Bookworm Linux:

Web server
----------
- Linux OS
- Apache (mod PHP or PHP FPM) or nginx + php fpm
- Uses filesystem to store file uploads and session data. Shared storage (Like with NFS or Ceph) is required for scaling on multiple web servers.
- Serves HTTP(S) (Web client), CalDAV, CardDAV, WebDAV, Microsoft ActiveSync, JMAP API
- Connects to mail server via IMAP, SMTP and MANAGESIEVE

Database
--------
- Linux OS
- MariaDB or MySQL Database
- Scaling MariaDB: https://mariadb.com/database-topics/scalability/
- Scaling MySQL: https://galeracluster.com

Mailserver
----------
- Linux OS
- Dovecot (IMAP, MANAGESIEVE)
- Postfix (SMTP)
- OpenDKIM
- Rspamd