OAuth2 Client
=============

The OAuth2 client module enables you to connect to cloud services using a OAuth2 connection. It is part of the community package.

.. note:: This module is supported from 6.6 and up.

Create a connection
```````````````````

First, you should install the OAuth2Client module. It is in the community package.

Next, you should make sure to configure your :ref:`provider <supported-providers>`.

The next step is creating a connection in system settings. Regardless of OAuth2 service that you wish to configure, the
following fields are common:

* **Name**: This is the name that of the connection that will be displayed in the OAuth2 connection combobox when configuring an email account.
* **Provider**: Select one of the know provider. See below for details. When a default provider is selected, one does not need to configure IMAP and SMTP servers.
* **Client Id**: Refers to the client Id as given by your provider.
* **Client Secret**: Refers to the client secret at given by your provider.
* **API Project Id**: The naming of this field differs by provider. Google names it Project Id, whereas Azure refers to it as Tenant Id.


.. figure:: /_static/using/oauth2/system-settings-oauth2-connection.png
   :width: 800px

	An example Google connection, used to connect to Gmail

Configure an email account
``````````````````````````

If you have set up your app in the API dashboard, you can :ref:`set up <email>` your configured connection in Group
Office.

1. Open the accounts dialog and either add a new account or open an existing account.
2. In the tab 'Properties', select the configured OAuth2 connection in the combobox.

.. figure:: /_static/using/oauth2/email-account-tab-properties.png
   :width: 800px

3. Click Apply. This will save the account.
4. Gain a refresh token by clicking the button 'Refresh token'. A new window will open. If you have not already done so, log into the external service. Give permission for Group Office to use OAuth2.
5. If all goes well, you see a friendly welcome message. A refresh token will have been added to your configured account. You can now close the account dialog by clicking 'Ok'.

From now on, you will be able to use email in Group Office using OAuth2. Please note that in OAuth2, tokens need to be
refreshed periodically. This happens automatically.

.. note:: When you still get logged out, you must renew a refresh token. However, this should happen very rarely.

.. _supported-providers:

Supported providers
```````````````````

Currently, we support the following OAuth2 providers:

.. toctree::
   :maxdepth: 2

   oauth2/gmail
   oauth2/azure
