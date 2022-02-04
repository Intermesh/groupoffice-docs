.. _rocketchat:

Rocket Chat
===========

Since version 6.4.145 Group-Office can integrate with `Rocket.Chat <https://rocket.chat>`_. With rocket chat you can chat with your team in
different channels, share files and even start a **video conference** from your desktop, phone or tablet!

.. figure:: /_static/system-settings/rocketchat/rocket-chat.png
   :width: 100%

   Rocket Chat


Installation
------------

To install you need a working Rocket.Chat installation. See the `Rocket.Chat documentation <https://docs.rocket.chat>`_
for that.

Login to Rocket.Chat as administrator and:

1. Important: Disable OTP authentication at Administration -> Settings -> Accounts or it won't work.
2. go to Administration -> Settings -> OAuth.
3. On the top right choose "Add custom oauth".
4. Note the callback URL / or redirect URI on top. For some reason they made it grey so it doesn't stand out. You need that later when adding the client in Group-Office.
5. Fill in your URL to Group-Office plus /api/oauth.php. For example: https://groupoffice.example.com/api/oauth.php
6. Copy the settings from the image below. Instead of the example password choose a strong password.:

   .. figure:: /_static/system-settings/rocketchat/custom-oauth.png
      :width: 100%

       Rocket Chat custom oauth settings

7. Login to Group-Office and go to System Settings -> Oauth 2.0
8. Click "Add client" and fill in the fields:

   - Match the "Identifier" and "Secret" from step 5.
   - Enable "Is confidential"
   - The redirect URI is the callback URL on top of the Rocket.Chat custom oauth page. It's marked in the red square in the screenshot below:

      .. figure:: /_static/system-settings/rocketchat/callback-url.png
         :width: 80%

          Rocket Chat callback URL

      The input should look like this:

      .. figure:: /_static/system-settings/rocketchat/rocket-chat-oauth-client.png
         :width: 80%

          Rocket Chat oauth client

9. Click save and test if you can login with Group-Office. You should see a "Login with Group-Office" button.

   .. figure:: /_static/system-settings/rocketchat/login-with-group-office.png
      :width: 100%

       Rocket Chat login with Group-Office button


.. note:: If you get an error double check these settings:

   - Administration -> General -> Site URL. It has to match for the openid handshake to work.
   - Administration -> Oauth -> Groupoffice: check if id and secret match the parameters in the
     Group-Office client. Also verify the other fields.