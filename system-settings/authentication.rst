Authentication
==============

On the authentication page you can manage:

1. The minimum password length of user passwords
2. Logout users automatically if they are inactive and disable the "Remember my login until I press logout on this computer".
3. Two factor authentication using an OTP client or for ActiveSync devices
4. Restrict access based on IP addresses
5. Enable or disable whether passwords were hacked earlier
6. LDAP Authentication
7. IMAP Authentication
8. Allow Cross Origin Requests from certain origins.

.. note:: 

   The features vary depending on which modules are installed on your system.

.. toctree::
   :maxdepth: 2
   :caption: Authentication:

   authentication/auth-allow-groups
   authentication/ldap
   authentication/imap
   authentication/otp
   authentication/2fa-eas

.. figure:: /_static/system-settings/authentication.png
   :alt: System Settings - Authentication

   System settings - Authentication
