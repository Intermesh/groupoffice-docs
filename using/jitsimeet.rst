.. _jitsimeet:
==========
Jitsi Meet
==========

This document describes how to configure GroupOffice Calendar to generate Jitsi Meet links when creating new calendar events.

.. figure:: /_static/using/jitsimeet/Jitsi_Hero_1600x600_opt2_2x_no_btn-scaled.jpg
   :alt: Jitsi Meet
   :width: 100%

Prerequisites
=============

- GroupOffice installation with Calendar and Jitsi meet module enabled.
- A Jitsi Meet server (self-hosted or using https://meet.jit.si/).
- Optional: Authentication enabled on your Jitsi server (if required).

Step 1: Identify Your Jitsi Server URL
======================================

1. For a public Jitsi server, you can use:
   `https://meet.jit.si`
2. For a self-hosted server, use your domain name:
   `https://jitsi.yourdomain.com`
3. Ensure the server is accessible to all users who will create meetings.

Step 2: Configure GroupOffice Calendar
=======================================

1. Log in to GroupOffice as an administrator.
2. Navigate to **System settings** > **Jitsi Meet**
3. Enter the following information:

   - **Jitsi Server URL:** The URL from Step 1.
   - **Authentication (optional):** If your server requires authentication, enter the app secret.

4. Save the settings.

.. figure:: /_static/using/jitsimeet/groupoffice-jitsimeet-settings.png
   :alt: GroupOffice Jitsi Meet settings
   :width: 100%

Step 3: Using Jitsi in Calendar Events
======================================

1. Create a new calendar event in GroupOffice.
2. When you click the camera button next to the location field it should generate a unique Jitsi Meet link for your event.
3. The link is automatically added to the event location field.

.. figure:: /_static/using/calendar/video-call.png
   :alt: Add video meeting url
   :width: 100%
