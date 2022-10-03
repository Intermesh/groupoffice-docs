.. _configuration:

Configuration file
==================

The configuration file can be found in:

- /etc/groupoffice/config.php
- /etc/groupoffice/multi_instance/<DOMAINNAME>/config.php
- The root of the Group-Office installation

Here's a list of config options:

.. table:: Config options
   :widths: auto

   ============================  ======  ===========
   Name                          Type    Description
   ============================  ======  ===========
   db_name                       string  Database name
   db_host                       string  Database server hostname
   db_port                       string  Database server port
   db_user                       string  Database username
   db_pass                       string  Database password
   file_storage_path             string  Where the files on disk are stored
   tmpdir                        string  Temporary files directory
   sseEnabled                    bool    Enable Server Sent Events for live push updates. Some servers don't support two connections!
   quota                         int     Max storage in bytes this installation may use
   max_users                     int     Max number of users this system may have
   allowed_modules               array   Array of modules or packages the system may use. Eg. ['legacy/\*', 'community/\*', 'business/newsletters']. For backwards compatibility this can also be a comma separated string.
   product_name                  string  For branding the system to another name
   debug                         bool    Enable debugging for developers. Can also be temporarily enabled with CTRL + F7 or Cmd + F7 in the browser.
   debug_log                     bool    Disable debug log when debug = true.
   debug_usernames               array   Debug only for these usernames. eg. ['demo', 'foo']
   debugEmail                    string  Set to an e-mail address to redirect all mail to for testing purposes.
   email_allow_body_search       bool    Enable searching in email bodies. Disabled by default as per version 6.6.103 .  
   servermanager                 bool    Set by multi_instance module. This will copy system settings and create welcome message on install.
   zpush2_loglevel               int     Set to 32 to generate debugging info in log/z-push.log
   zpush2_special_log_users      array   Set to usernames you want to debug. eg. ['testuser', 'testuser2']
   vmail_path                    string  Customize where mail is stored. Defaults to "/var/mail/vhosts/"
   custom_css_url                string  URL to stylesheet to load in the web interface.
   email_enable_labels           bool    Enable labels for e-mail if IMAP server supports it
   allow_themes.                 bool    Enable themes
   theme                         bool    Default theme ("Paper")
   ============================  ======  ===========


Global configuration
--------------------

You can also create a file called::

   /etc/groupoffice/globalconfig.inc.php

this file supports the same properties as the regular file but applies to all Group-Office instances on the server when
running :ref:`multiple instances <multi-instance>`.

You can also preconfigure module settings that are normallly set in the user interface. For example you can set
the OnlyOffice server URL for all instances::

    $config['business'] = [

        'onlyoffice' => [
            'documentServerUrl' => 'https://onlyoffice.example.com',
            'documentServerSecret' => 'mysecretkey'
        ]

    ];

Recommended PHP settings
------------------------

For optimal Group-Office perfomance we recommend these settings. This will allow users to upload files up to 1GB:

.. table:: PHP settings
   :widths: auto

   ======================  ===========  ========================================================================================
   Name                    Value        Explanation
   ======================  ===========  ========================================================================================
   memory_limit            256M         For example parsing large e-mail messages for ActiveSync require high memory usage.
   post_max_size           1G           Allows for uploading files of 1GB size. Raise if you need more.
   upload_max_filesize     1G.          Allows for uploading files of 1GB size. Raise if you need more.
   session.gc_maxlifetime  86400        The default of 30 minutes will cause a logout if you leave your computer for 30 minutes.
   ======================  ===========  ========================================================================================

Locking system settings
-----------------------
Configuration properties configurable in the GUI at System settings can be locked in the config.php or globalconfig.inc.php file::

    $config['core'] => [
        'title' => 'Pinned title',
        'primaryColor' => '2E7D32',
        'passwordMinLength' => 6,
        'smtpEncryption => 'tls',
        'smtpHost => 'localhost',
        'smtpUsername => null,
        'smtpPassword => null,
        'smtpPort' => 587
    ];

Branding
--------

If you'd like to brand Group-Office you can easily do this:

Edit the configuration or global configuration file and add::

    $config['product_name'] = 'My Office'; //Will replace the word 'Group-Office' with 'My Office'
    $config['custom_css_url'] = '/branding/style.css'; //Loads a custom CSS stylesheet.
    $config['support_link'] = 'https://docs.example.com/'; //Changes the URL behind "Help" in the main menu. Can also be an e-mail address

In the branding folder create a style.css stylesheet with for example this content::

    /**
     * Preferred primary theme colors
     */
    :root {
        --c-primary: rgb(27, 100, 139);
        --c-header-bg: rgb(27, 100, 139);
        --c-primary-tp: rgba(27, 100, 139, .16);
        --c-secondary: brown;
        --c-accent: orange;
    }

    /**
     * Override logo
     */
    .go-app-logo, .go-about-logo, .go-settings-logo, #go-logo {
        background-image: url('my-group-office.png');
        width: 240px;
        height: 40px;
    }


.. note:: It will still leave copyright notices to Intermesh. It's not allowed to remove those.
