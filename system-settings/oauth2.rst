.. _oauth2:

OAuth 2.0
=========

Group-Office has a built in Oauth 2.0 server for authentication. At the moment it's mainly used to offer the `OpenID
connect 1.0 protocol <https://openid.net/connect/>`_.

.. _openid:

OpenID Connect
--------------
`OpenID connect 1.0 <https://openid.net/connect/>`_. is a simple identity layer on top of the OAuth 2.0 protocol. It
allows Clients to verify the identity of the End-User based on the authentication performed by Group-Office as an
Authorization Server, as well as to obtain basic profile information about the End-User in an interoperable and
REST-like manner.

You can add clients at System Settings -> OAuth 2.0.

We've used this to integrate:

- :ref:`rocketchat`
- :ref:`mediawiki`

But any system supporting OpenID connect should be able to use this feature.
