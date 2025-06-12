CalDAV Client
=============

GroupOffice can function as a calendar server, but it can also connect to other
calendar servers such as iCloud, Google Calendar, or NextCloud. Setting this up
will create two-way synchronization.

After installing the CalDAV Client module, an extra panel under *My Account*
will appear, named **DAV Accounts**. This will present a list of all external
CalDAV servers GroupOffice is connected to. The list will be empty initially.

Press the **+** button at the top to add your first account:

.. figure:: /_static/using/davclient/dav_account.png
   :width: 100%

At this time, the DAV Client only supports calendar synchronization.
Support for task lists and address books may be added later.

- The **Name** field can be anything you like to help recognize the account.
- The **Host** should be the domain name of your CalDAV server.
  GroupOffice will use the auto-discovery protocol to find the calendar home set
  (a list of available calendars on the server).

Authentication
--------------

The CalDAV client in GroupOffice supports **Basic Authentication**.

Some CalDAV providers, such as iCloud, require additional steps to connect
successfully because they do not allow direct login using your main account
password. Instead, you must generate an **app-specific password**.

iCloud Instructions
^^^^^^^^^^^^^^^^^^^

To connect GroupOffice to your iCloud Calendar, follow these steps:

1. Visit the Apple ID website: https://appleid.apple.com/
2. Log in with your Apple ID.
3. Under the **Sign-In and Security** section, click **App-Specific Passwords**.
4. Click **Generate an App-Specific Password**.
5. Enter a label (e.g., “GroupOffice CalDAV”) and click **Create**.
6. Copy the generated password. You will not be able to view it again.
7. Use this password in GroupOffice instead of your main Apple ID password.

.. note::

   If you use two-factor authentication (2FA) on your Apple account—which is
   required for app passwords to work—you must generate a new app-specific
   password for each application that doesn’t support 2FA directly.

Other Providers
^^^^^^^^^^^^^^^

Most other providers that support CalDAV and Basic Authentication—such as
NextCloud or custom servers—will work with a regular username and password.

However, some services (like Google Calendar) may not support CalDAV directly
anymore or may require OAuth or additional setup. Please consult your provider's
documentation for their current CalDAV access policy.

as of October 2024, Google no longer supports app-specific passwords for CalDAV. 
They have officially deprecated this method in favor of OAuth 2.0.

OAuth2 is not yet available for the DAV client module.


Service discovery
-----------------

There is support for both ``well-known`` and SRV records in DNS.
An example of an SRV record would look like this:

::

   _caldavs._tcp 86400 IN SRV 10 20 443 dav.example.org.

Here, ``443`` is the port used for HTTPS.

.. note::

   SRV records can only point to domain names, not full paths.

Therefore, GroupOffice will attempt discovery using the ``well-known`` protocol.
It will make an HTTP request to:

::

   https://dav.example.org/.well-known/caldav

This path can be a redirect to the correct location. If not, GroupOffice will try
to retrieve the user principal URI directly from the well-known path.

If this fails, you will get a **"Could not find principalUri"** error. In that case,
you can either:

- Manually specify the correct path, or
- Check if your CalDAV server is properly configured.

If all goes well, the DAV account will be added to the list. However, no data
will be fetched immediately. You can either wait for the cron job to run, or
press the **Sync** button under the 3-dot menu next to the added account.

.. note::

   Synchronization can take a while if there’s a lot of calendar data.
   Be patient. If the browser connection times out, **do not** restart the sync
   process until a **Last Sync** value appears next to your account.

GroupOffice uses a cron task to periodically run the synchronization process,
based on the sync interval defined in your account settings.

If there are calendars you don't want to see, you can unsubscribe from them
via the calendar module.

Calendars from CalDAV servers will have a **Synchronize** button in the calendar
module, which can be used to manually sync a single calendar.

Delete an Account
-----------------

.. figure:: /_static/using/davclient/on_delete.png
   :width: 50%

When deleting an account from the list, GroupOffice will ask if you want to
keep the calendar data. If you choose to keep it, the calendars will be converted
to local calendars that no longer synchronize.

This is useful if you want to import calendar data from a third party.

.. note::

   Even if you choose to keep the data, the calendars can still be manually
   deleted one by one later.
