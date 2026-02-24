.. _msteams:

===============
Microsoft Teams
===============

This document describes how to create an Azure App registration to enable Microsoft Teams integration in the GroupOffice calendar.
Once configured, you can generate Teams meeting links when creating new calendar events.

.. figure:: /_static/using/msteams/Microsoft-Teams.jpg
   :alt: Microsoft Teams
   :width: 100%

Prerequisites
=============

- Access to an Azure Active Directory (Azure AD) tenant.
- Administrator privileges in Azure AD.
- GroupOffice installation with Calendar and Microsoft Teams (Pro version) module enabled.
- Microsoft 365 account with Teams enabled.

Step 1: Create an Azure App Registration
========================================

1. Sign in to the Azure portal at https://portal.azure.com.
2. Navigate to **Azure Active Directory** > **App registrations**.
3. Click **New registration**.
4. Fill in the registration form:

   - **Name:** `GroupOffice Teams Integration`
   - **Supported account types:** Select `Accounts in this organizational directory only (Single tenant)` unless multi-tenant access is needed.
   - **Redirect URI (optional):** Set type to **Web** and enter your GroupOffice URL followed by `/api/page.php/business/msteams/auth`, for example:
     `https://yourgroupoffice.com/api/page.php/business/msteams/auth` ( You can also view the correct URI in GroupOffice at System Settings -> Microsoft Teams)

5. Click **Register**.


.. figure:: /_static/using/msteams/azure-app-authentication-settings.png
   :alt: Azure App API Permissions
   :width: 100%


Step 2: Configure API Permissions
=================================

1. In your newly created app, navigate to **API permissions** > **Add a permission**.
2. Choose **Microsoft Graph**.
3. Select **Delegated permissions** and add the following:

   - `OnlineMeetings.ReadWrite`
   - `User.Read`

4. Click **Add permissions**.
5. If your app requires admin consent, click **Grant admin consent for [Tenant Name]**.


.. figure:: /_static/using/msteams/azure-app-api-permissions.png
   :alt: Azure App API Permissions
   :width: 100%


Step 3: Create a Client Secret
==============================

1. Navigate to **Certificates & secrets**.
2. Click **New client secret**.
3. Enter a description, e.g., `GroupOffice Teams Secret`.
4. Choose an expiration period (recommended: 6 or 12 months).
5. Click **Add** and **copy the secret value immediately**. You will not be able to retrieve it again.

Step 4: Collect Application Details
===================================

You will need the following information for GroupOffice configuration:

- **Application (client) ID:** Found on the app's **Overview** page.
- **Directory (tenant) ID:** Found on the app's **Overview** page.
- **Client secret:** Copied from step 3.

Step 5: Configure GroupOffice
==============================

1. Log in to GroupOffice as an administrator.
2. Navigate to **System Settings** > **Microsoft Teams**
3. Enter the Azure App details:

   - **Client ID**
   - **Client Secret**
   - **Tenant ID**

4. Save the settings.
5. Test the integration by creating a new calendar event and checking if the **Add Teams Meeting** button is available.


.. figure:: /_static/using/msteams/groupoffice-msteams-app-settings.png
   :alt: GroupOffice Microsoft Teams settings
   :width: 100%

Step 6: Using Microsoft Teams in Calendar Events
======================================

1. Create a new calendar event in GroupOffice.
2. When you click the camera button next to the location field it should generate a unique Microsoft Teams link for your event.
3. The link is automatically added to the event location field.

.. figure:: /_static/using/calendar/video-call.png
   :alt: Add video meeting url
   :width: 100%

Troubleshooting
===============

- **Invalid redirect URI:** Make sure the redirect URI in Azure matches exactly what is configured in GroupOffice.
- **Permission errors:** Ensure that the `OnlineMeetings.ReadWrite` permission is granted and admin consent is approved.
- **Teams button not appearing:** Clear your browser cache or log out and back in after configuring the app.

