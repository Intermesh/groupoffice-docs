.. _media-wiki:

MediaWiki
=========

You can integrate `MediaWiki <https://www.mediawiki.org>`_ with the :ref:`OpenID Connect protocol <openid>`. This way you can authenticate to MediaWiki with your
GroupOffice account.

Take these steps to install:

1. Install and configure `MediaWiki <https://www.mediawiki.org>`_

2. Install the required `PluggableAuth <https://www.mediawiki.org/wiki/Extension:PluggableAuth>`_ extension

3. Install the required `OpenIDConnect <https://www.mediawiki.org/wiki/Extension:OpenID_Connect>`_ extension

4. Create OAuth client in GroupOffice in :ref:`System Settings -> OAuth 2.0 <oauth2>`:

      - Client ID: mediawiki
      - Check "Is confidential"
      - Enter a secret password.
      - Redirect URI to MediaWiki::

            http://example.com/index.php/Special:PluggableAuthLogin

        .. note:: Be careful it could be localized. In Dutch it was "Speciaal:PluggableAuthLogin"

5. Edit Mediawiki's LocalSettings.php and add to the bottom::

        wfLoadExtension( 'PluggableAuth' );
        wfLoadExtension( 'OpenIDConnect' );

        $wgGroupPermissions['*']['autocreateaccount'] = true;
        $wgGroupPermissions['*']['createaccount'] = true;

        //automatically login when logged in to GroupOffice
        $wgPluggableAuth_EnableAutoLogin = true;

        // The above doesn't work when enabling local logins!
        $wgPluggableAuth_EnableLocalLogin = false;

        $wgOpenIDConnect_Config['<<GROUPOFFICE_URL>>/api/oauth.php'] = [
            'clientID' => 'mediawiki',
            'clientsecret' => '<<CLIENT SECRET from GROUP OFFICE Oauth 2.0 module>>',
            'scope' => array( 'openid')
        ];

6. Optionally, you can use the bookmarks module to add the wiki page as a module page.
