iOS (iPhone or iPad)
====================

On iOS you can connect using ActiveSync.
You can synchronize:

- Notes
- Calendar
- Contacts
- E-mail
- Tasks (Called "Reminders" on iOS)
- Files (Using WebDAV)

Microsoft ActiveSync
--------------------

To setup an ActiveSync account take the following steps:

1. Navigate to Settings and lookup the "Accounts & Passwords" page.

2. Click on "Add account".

   .. figure:: /_static/ios-eas/1-accounts-and-passwords.PNG
      :width: 400px

3. Now tap on "Exchange".

   .. figure:: /_static/ios-eas/2-add-account.PNG
      :width: 400px

4. Fill in your e-mail address and an account description

   .. figure:: /_static/ios-eas/3-exchange.PNG
      :width: 400px

5. In the popup dialog choose "Configure manually".

   .. figure:: /_static/ios-eas/4-configure-manually.PNG
      :width: 400px

6. Now enter your password.

   .. figure:: /_static/ios-eas/5-password.PNG
      :width: 400px

7. iOS now attempts to discover settings on the domain of your e-mail address. 
   In this example "intermesh.nl". It is likely to fail because this is not the 
   correct ActiveSync server address. It give a certficate error. Just ignore it 
   by clicking "Continue".

   .. figure:: /_static/ios-eas/6-certificate-warning.PNG
      :width: 400px

8. Enter your :ref:`server-hostname` and your GroupOffice username.

   .. figure:: /_static/ios-eas/7-server-settings.PNG
      :width: 400px

9. In the final screen you can optionally disable some apps.

   .. figure:: /_static/ios-eas/8-enabled-apps.PNG
      :width: 400px

10. Now you must give it some time to sync everything and check your contacts, 
e-mail and calendar for your GroupOffice data!


Files (WebDAV)
--------------

With the app "FilebrowerGO" see https://www.stratospherix.com/products/filebrowser/ you can mount the webdav drive and access files directly from your phone.
