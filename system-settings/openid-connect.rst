.. _oauth2:

OpenID Connect
==============

Group-Office can be configured as client to use an external OpenID connect server for **Single Sign On**. But Group-Office can also
be configured as the OpenID connect server.

OpenID Connect client
---------------------

To configure an external OpenID connect server for **Single Sign On** you must install the **OIDC module**. Then you can
configure openID compliant providers such as:

- `Microsoft Azure <https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc>`_
- `Google <https://developers.google.com/identity/openid-connect/openid-connect>`_
- `Authentik <https://docs.goauthentik.io/add-secure-apps/providers/oauth2/create-oauth2-provider/>`_
- `Keycloak <https://www.keycloak.org/securing-apps/oidc-layers>`_
- Another Group-Office installation

Once installed a button "Sign up with <MYPROVIDER>" will show on the login page of Group-Office

Get started
```````````

1. Configure the OpenID App registration at the provider so you have an **Authority URL**, **Client ID** and **Client secret***.
   You will need to add a **redirect URL**.

   That is: **https://yourgroupoffice.com/api/page.php/go/community/oidc/auth**

   You can get that from the OIDC module too at **System Settings** -> **OIDC** -> **Add**

2. Install the OIDC module at **System Settings** -> **Modules**
3. Create the new client at **System Settings** -> **OIDC**. You will the **Authority URL**, **Client ID** and **Client secret** from step 1 here.

   .. figure:: /_static/system-settings/oidc-client.png
      :alt: Add OIDC Client
      :width: 100%

4. Logout and find the new button to use the single sign on.

   .. figure:: /_static/system-settings/oidc-login.png
         :alt: Login with OIDC
         :width: 100%


Password authentication
```````````````````````
The SSO method above does not store a password in Group-Office. That enhances the security. But because of this services
like WebDAV, CalDAV and Microsoft ActiveSync can't work.
If your authentication backend supports LDAP too you can also setup LDAP authentication so it can offer password authentication for these
services.

.. _openid:

OpenID Connect server
---------------------

`OpenID connect 1.0 <https://openid.net/connect/>`_. is a simple identity layer on top of the OAuth 2.0 protocol. It
allows Clients to verify the identity of the End-User based on the authentication performed by Group-Office as an
Authorization Server, as well as to obtain basic profile information about the End-User in an interoperable and
REST-like manner.

You can add clients at **System Settings** -> **OAuth 2.0.**

We've used this to integrate:

- :ref:`rocketchat`
- :ref:`media-wiki`

But any system supporting OpenID connect should be able to use this feature.


