.. auth-allow-groups:

Restrict access
===============

To enhance security you can limit the locations (IP Addresses) where users can login to the system.
You can set this per group:

.. figure:: ../../_static/system-settings/auth-allowed-groups.png
	 :alt: Allowed groups

	 Allowed groups

.. warning::

   You can easily lock everybody out from the system with this feature. I recommend that you add group "Admins" with
   pattern "*" first so that Admins can always login. When you're sure everything is setup correctly you can remove
   that rule.

Rules
-----

Login is allowed when:

1. There are no rules defined for any group you are a member of.
2. One of the rules of groups you are a member of matches your IP address

Each rule has a group and a pattern for IP addresses. You can use "*" to match any part of an IP address and '?' to
match a single character.

Some examples:

- "*" will match any IP address
- "192.168.1.?" will match 192.168.1.1 till 192.168.1.9.
- "192.168.1.* will match 192.168.1 till 192.168.1.255

