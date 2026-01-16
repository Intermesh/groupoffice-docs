.. _maildomains:

Mail domain management
======================

.. figure:: /_static/using/maildomains/maildomains_overview.png
   :alt: Maildomains module
   :width: 100%

   Mail domains

In the maildomains module the administrator can manage their dovecot domain configurations. It replaces the venerable
postfix_admin module.

Domains
-------


DNS Checks
``````````
DNS checks can be performed by clicking the little button in the top right corner next to the 'DNS Settings' header. A
script will be run that will retrieve and verify DNS records. If any records are missing or incorrect, they are marked
with a red warning icon.

Mailboxes
---------

It is perfectly possible to manage mailboxes from this module, just like in the old postfix_admin module.

.. figure:: /_static/using/maildomains/maildomains_mailboxes.png
   :alt: Mailbox management
   :width: 100%

   Mailbox management


Aliases
-------

.. figure:: /_static/using/maildomains/maildomains_alias.png
   :alt: Alias
   :width: 100%

   Alias management

This module also enables the administrator to manage mail aliases easily.

