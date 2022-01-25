
.. _gmail:

Use Gmail with OAuth2
=====================

Support for the Gmail IMAP server has been expanded with OAuth2. In the old days, a user would be able to log into Gmail
with their email address and password. However, when a user enables 2 factor authentication, this is not possible anymore.
One way to circumvent this, is the configuration of an `App Password or LSA <https://support.google.com/accounts/answer/6010255>`_,
but Google itself `does not recommend this <https://support.google.com/accounts/answer/185833?>`_ :

	Tip: App Passwords aren’t recommended and are unnecessary in most cases. To help keep your account secure, use "Sign
	in with Google" to connect apps to your Google Account.

.. warning:: LSA were supposed to be phased out by 2020. Also, in case you have not clicked the link above, LSA means 'Less Secure App' . Please do not use these anymore!

This guide contains a HOWTO on how to connect your Gmail account through OAuth2 with Group Office.

.. note:: This module is supported for versions 6.5 and up.

Create an app
`````````````
.. note:: Please read the `full documentation for OpenID Connect <https://developers.google.com/identity/protocols/oauth2/openid-connect>`_ for full context.

1. Log into Google using your gmail credentials.
2. Open the `Credentials page <https://console.cloud.google.com/apis/credentials>`_ in the Google API Dashboard.
3. Click the button Create Credentials > OAuth client ID

.. figure:: /_static/using/oauth2/google-credentials-dashboard-1.png

4. A new form is opened.

	1. Enter a name for your app in the field 'name'.
	2. Enter one or more URIs in the field 'URIs' under the header 'Authorized JavaScript origins'. These should match the URL configuration setting in your Group Office instance.
	3. The field 'URIs' under the header 'Authorized redirect URLs' should contain the value `https://yourhost/go/modules/community/oauth2client/gauth.php/callback`. 'Yourhost' refers to the URL configuration setting of your Group Office instance.
	4. In the right column, a Client ID, a Client Secret and a Creation date are displayed. Write these down or download the JSON credential file by clicking the 'Download JSON' button

.. figure:: /_static/using/oauth2/google-credentials-dashboard-2.png
   :width: 800px

5.  The next step is to customize the `OAuth consent screen <https://console.cloud.google.com/apis/credentials/consent>`_:

	1. In the first step, enter an App Name (to be displayed to the end user), a support email address (yours). Fill in the rest of your form as per your domain settings.
	2. In the Scopes Step, be sure to add the scope 'https://mail.google.com'.
	3. The next step is to add test users if needed. Please note that your default email address already has access.
	4. Confirm your settings. Currently, your app is in testing mode. Click the button 'publish app' to move to production. This may take some time.

.. note:: Once an app has been published, anybody with a Gmail account can use this app. Furthermore, refresh tokens will expire while your app remains in test mode.

A note to developers
++++++++++++++++++++

When using the official `Group Office development environment <https://github.com/Intermesh/docker-groupoffice-development>`_,
please make sure to set the URL to `http://localhost:8000` in the system settings. Localhost is the only non-https URL that
accepted by Google. You cannot use `http://host.docker.internal:8000` as the URL in your system configuration.

Configure a Group Office Account
````````````````````````````````

First, you should install the OAuth2Client module. It is in the community package.

If you have set up your app in the API dashboard, you can :ref:`set up <email>` your Gmail account in Group Office. It
does need to be in production status yet, but you have certain restrictions if it is still in testing.

1. Open the accounts dialog and either add a new account or open an existing gmail account.
2. In the tab 'Properties', make sure that the field 'Authentication Method' is set to 'GoogleOauth2'.

.. figure:: /_static/using/oauth2/email-account-tab-properties.png
   :width: 800px

3. In the tab 'OAuth2', enter the client ID, client secret and project Id from the downloaded JSON file. and click 'Apply'.

.. figure:: /_static/using/oauth2/email-account-tab-oauth.png
   :width: 800px

4. Gain a refresh token by clicking the button 'Refresh token'. A new window will open with a Google consent screen. Make sure that you check all checkboxes for gmail in the consent screen.
5. Close the account dialog by clicking 'Ok'. Your refresh token should be saved.

From now on, you will be able to use gmail in Group Office using OAuth2.