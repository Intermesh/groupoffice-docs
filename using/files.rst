.. _files:

Files
=====

The files module supports:

- :ref:`links`
- :ref:`custom-fields`
- :ref:`comments`
- :ref:`sharing`
- :ref:`files`


.. _assistant:

Assistant
---------

The Group-Office Assistant is a small program that you can install on your Windows, MacOS or
Linux computer. It will automatically download files opened from Group-Office and monitor
it for changes. When the file is saved it automatically uploads it back to Group-Office.

It also assists in mounting a network drive.

Download it for:

- :ref:`Windows <assistant-for-windows>`
- :ref:`MacOS <assistant-for-macos>`
- :ref:`Linux <assistant-for-linux>`

Collabora Online
----------------

.. figure:: /_static/using/files/collabora-online.png
   :alt: Collabora Online

With Collabora Online you can edit office documents in your browser. You need a working
Collabora Online server. More info on https://www.collaboraoffice.com/code/

Configuration
`````````````

For Collabora to work you need to setup SSL and allow your Group-Office URL to use it.

SSL
~~~

We've used the Debian packages and setup SSL with Letsencrypt. Then we've added this SSL
configuration to /etc/loolwsd/loolwsd.xml::

    <ssl desc="SSL settings">
        <enable type="bool" desc="Controls whether SSL encryption is enable (do not disable for production deployment). If default is false, must first be compiled with SSL support to enable." default="true">true</enable>
        <termination desc="Connection via proxy where loolwsd acts as working via https, but actually uses http." type="bool" default="true">false</termination>
        <cert_file_path desc="Path to the cert file" relative="false">/etc/letsencrypt/live/groupoffice.co/cert.pem</cert_file_path>
        <key_file_path desc="Path to the key file" relative="false">/etc/letsencrypt/live/groupoffice.co/privkey.pem</key_file_path>
        <ca_file_path desc="Path to the ca file" relative="false">/etc/letsencrypt/live/groupoffice.co/fullchain.pem</ca_file_path>
        <cipher_list desc="List of OpenSSL ciphers to accept" default="ALL:!ADH:!LOW:!EXP:!MD5:@STRENGTH"></cipher_list>
        <hpkp desc="Enable HTTP Public key pinning" enable="false" report_only="false">
            <max_age desc="HPKP's max-age directive - time in seconds browser should remember the pins" enable="true">1000</max_age>
            <report_uri desc="HPKP's report-uri directive - pin validation failure are reported at this URL" enable="false"></report_uri>
            <pins desc="Base64 encoded SPKI fingerprints of keys to be pinned">
            <pin></pin>
            </pins>
        </hpkp>
    </ssl>

Network
~~~~~~~

Change network settings to allow posting from your Group-Office URL.
We've used *intermesh.group-office.com* for example::

   <net desc="Network settings">
      <proto type="string" default="all" desc="Protocol to use IPv4, IPv6 or all for both">all</proto>
      <listen type="string" default="any" desc="Listen address that loolwsd binds to. Can be 'any' or 'loopback'.">any</listen>
      <service_root type="path" default="" desc="Prefix all the pages, websockets, etc. with this path."></service_root>
      <post_allow desc="Allow/deny client IP address for POST(REST)." allow="true">
        <host desc="The IPv4 private 192.168 block as plain IPv4 dotted decimal addresses.">192\.168\.[0-9]{1,3}\.[0-9]{1,3}</host>
        <host desc="Ditto, but as IPv4-mapped IPv6 addresses">::ffff:192\.168\.[0-9]{1,3}\.[0-9]{1,3}</host>
        <host desc="The IPv4 loopback (localhost) address.">127\.0\.0\.1</host>
        <host desc="Ditto, but as IPv4-mapped IPv6 address">::ffff:127\.0\.0\.1</host>
	    <host desc="The IPv6 loopback (localhost) address.">::1</host>
	    <host desc="intermesh" allow="true">intermesh.group-office.com</host>
	    <host desc="office" allow="true">office.group-office.com</host>
      </post_allow>
      <frame_ancestors desc="Specify who is allowed to embed the LO Online iframe (loolwsd and WOPI host are always allowed). Separate multiple hosts by space."></frame_ancestors>
    </net>

Storage
~~~~~~~

Change the backend storage to allow your Group-Office URL::

    <storage desc="Backend storage">
        <filesystem allow="false" />
	    <wopi desc="Allow/deny wopi storage. Mutually exclusive with webdav." allow="true">
            <host desc="intermesh" allow="true">intermesh.group-office.com</host>
            <host desc="office" allow="true">office.group-office.com</host>

	        <host desc="Regex pattern of hostname to allow or deny." allow="true">localhost</host>
            <host desc="Regex pattern of hostname to allow or deny." allow="true">10\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}</host>
            <host desc="Regex pattern of hostname to allow or deny." allow="true">172\.1[6789]\.[0-9]{1,3}\.[0-9]{1,3}</host>
            <host desc="Regex pattern of hostname to allow or deny." allow="true">172\.2[0-9]\.[0-9]{1,3}\.[0-9]{1,3}</host>
            <host desc="Regex pattern of hostname to allow or deny." allow="true">172\.3[01]\.[0-9]{1,3}\.[0-9]{1,3}</host>
            <host desc="Regex pattern of hostname to allow or deny." allow="true">192\.168\.[0-9]{1,3}\.[0-9]{1,3}</host>
            <host desc="Regex pattern of hostname to allow or deny." allow="false">192\.168\.1\.1</host>
            <max_file_size desc="Maximum document size in bytes to load. 0 for unlimited." type="uint">0</max_file_size>
        </wopi>
        <webdav desc="Allow/deny webdav storage. Mutually exclusive with wopi." allow="false">
            <host desc="Hostname to allow" allow="false">localhost</host>
        </webdav>
    </storage>

After making these changes restart loolwsd::

    sudo systemctl restart loolwsd

Check the status::

    sudo systemctl status loolwsd

If anything is wrong view the logs::

    sudo journalctl -u loolwsd


Group-Office
~~~~~~~~~~~~

When Collabora is running you can setup Group-Office to use it. Install the Office Online module from the Business package.

.. figure:: /_static/using/files/install-office-online.png
   :alt: Install Office Online
   :width: 400px

Reload Group-Office and go to System Settings -> Office Online

Then add your Collabora Code Service. The default port for Collabora is 9980.

.. figure:: /_static/using/files/add-collabora-code-service.png
   :alt: Add Collabora Code Service
   :width: 400px

Now every user can go to the files module and use it. Just right click a file and choose "Open with...".

.. figure:: /_static/using/files/open-with-collabora-online.png
   :alt: Use Collabora Code Service
   :width: 400px


.. note:: If you get a 404 error when editing because /wopi is not found then you probably are missing the alias in your
   webserver configuration. The Debian package automatically do this but with the tarball package you have to do this manually.
   :ref:`Example configuration can be found here. <webserver-aliases>`


