Windows
=======

On Windows you can connect Outlook using ActiveSync. You can synchronize:

- Files
- Outlook Calendar
- Outlook Contacts
- Outlook E-mail


Outlook / Windows 10
--------------------

Note: This guide describes Outlook but this kind of ActiveSync account also 
works for the Windows 10 Mail, People and Calendar app.

To setup an ActiveSync account take the following steps:

1. Open Outlook and click "File". 
2. Then click "Add account".

   .. figure:: /_static/windows-eas/1-add-account.png
      :width: 400px

3. Select "Manual setup" and click "Next".

   .. figure:: /_static/windows-eas/2-manual-setup.png
      :width: 400px

4. Choose "Outlook.com or Exchange ActiveSync compatible service" and click "Next".

   .. figure:: /_static/windows-eas/3-eas.png
      :width: 400px

5. In the next screen you must adjust your server settings. It will prefill the 
   username with the e-mail address and the server name with the domain from 
   your e-mail address. This is most likely **incorrect**.
   Please adjust to your Group-Office username and enter the :ref:`server-hostname`.
   When done click "Next".

   .. figure:: /_static/windows-eas/4-server-settings.png
      :width: 400px

6. Outlook will test your settings. If all is well you should see the following 
   screen.

   .. figure:: /_static/windows-eas/5-test.png
      :width: 400px

7. Now you must give it some time to sync everything. Then check your contacts, 
   e-mail and calendar for your Group-Office data!

Files
-----

Additionally you can map Group-Office as network drive using WebDAV. 
With Group-Office Assistant you'll connect automatically when you click a file
in Group-Office.

`Click here to download Group-Office Assistant for Windows 
<https://repo.group-office.com/downloads/group-office-assistant-windows.exe>`_.

After installing it you can use it as follows:

1. In Group-Office right click on a file and choose "Open with".

2. Select the "Your desktop application (WebDAV) option to use the assistant.

   .. figure:: /_static/macos-assistant/4-select-application.png
      :width: 400px


WebDAV client issues
````````````````````

Unfortunately there are some known issues with the native Windows WebDAV implementation:

1. When opening office files you have to re-authenticate: https://support.microsoft.com/en-us/help/2019105/authentication-requests-when-you-open-office-documents
2. There's a path length limit in both windows and office. So long paths will fail. The URL of your Group-Office counts as path too.

Both of these issues can be resolved by using the `Mountain Duck WebDAV client <https://mountainduck.io>`_.




