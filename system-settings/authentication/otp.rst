.. _otp:

One-Time-Password Authentication
================================

You can use two factor authentication (2FA for short) when the OTP Authenticator module has been installed. You can
find it in the Community package.

First install any OTP app on your mobile phone or desktop. You can use for example:

1. `Google Authenticator <https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=nl>`_
2. OTP Auth (`iOS <https://itunes.apple.com/us/app/otp-auth/id659877384>`_ and `MacOS <https://apps.apple.com/us/app/otp-auth/id1471867429?mt=12>`_)
3. `Aegis Authenticator <https://getaegis.app>`_ is a powerful open source OTP client for Android

After installing an OTP app on your phone go to "My Account" -> "Account" and 
click on the "Enable OTP Authenticator" button.

.. figure:: ../../_static/google-authenticator.png
	 :alt: OTP Authenticator

	 OTP Authenticator module

You will be prompted for your GroupOffice password. Next you will be asked to
scan the QR code with your app to register GroupOffice. Enter the code from
the phone to confirm you've set it up and you're done.

Enforce 2FA for user groups
---------------------------

System administrators can enforce two factor authentication for specific user groups. In the system settings screen,
open the tab 'Authentication' and select a group.

.. figure:: ../../_static/system-settings/otp-system-settings.png
	:alt: Force 2FA for user groups

	Enforcing 2FA

