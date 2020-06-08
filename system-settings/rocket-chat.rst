.. _rocketchat:

Rocket Chat
===========

Since version 6.4.145 Group-Office can integrate with `Rocket.Chat <https://rocket.chat>`_. With rocket chat you can chat with your team in
different channels, share files and even start a **video conference** from your desktop, phone or tablet!

.. figure:: /_static/system-settings/rocketchat/rocket-chat.png
   :width: 100%

   Rocket Chat


Installation
============

To install you need a working Rocket.Chat installation. See the `Rocket.Chat documentation <https://docs.rocket.chat>`_
for that.

Login to Rocket.Chat as administrator and:

1. go to Administration -> Settings -> OAuth.
2. On the top right choose "Add custom oauth".
3. Note the callback URL on top. You need that later when adding the client in Group-Office.
4. Fill in your URL to Group-Office plus /api/oauth.php. For exampl.e https://groupoffice.example.com/api/oauth.php
5. Copy the settings from the image below. Instead of the example password choose a strong password.:

   .. figure:: /_static/system-settings/rocketchat/custom-oauth.png
      :width: 100%

       Rocket Chat custom oauth settings

6. Login to Group-Office and go to System Settings -> Oauth 2.0
7. Click "Add client" and fill in the fields:
   - Match the "Identifier" and "Secret" from step 5.
   - Enable "Is confidential"
   - The redirect URI is on top of the Rocket.Chat custom oauth page.
8. Click save and test if you can login with Group-Office. You should see a "Login with Group-Office" button.

   .. figure:: /_static/system-settings/rocketchat/login-with-group-office.png
      :width: 100%

       Rocket Chat login with Group-Office button