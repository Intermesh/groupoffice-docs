Cleanup database
-------------------------------

After deprecated modules get deleted from the source, they are no longer uninstallable.
If you haven't uninstalled the deleted module before upgrading, there might be tables
in the database that remain there forever but are no longer used.

Older GroupOffice instances that have gone through several version upgrades have lots of old data stored in their
databases. As older modules get replaced by newer modules, old database items are being converted to new database 
items. The database of the old module will not be deleted by default, but as the newer modules use the new tables, 
the old tables just take up space.

For this reason we keep a list of ``DROP TABLE`` statements. These can be executed on 
the database after a successful upgrade to remove the old tables.

.. warning:: Do this at your own risk!
	We strongly recommend that you create a backup of the database before using any of these
	cleanup measures.

5.0 or higher
~~~~~~~~~~~~~~~~~~~~~
 	anything starting with ``pm_``;
	anything starting with ``sy_``;


6.4 or higher
~~~~~~~~~~~~~~~~~~~~~
The Contacts module was replace with a new version. Any table starting with `ab_` can
be removed Contacts are in tables starting with `addressbook_`

.. code:: sql

	DROP TABLE IF EXISTS `ab_addressbooks`;
	DROP TABLE IF EXISTS `ab_addresslist_group`;
	DROP TABLE IF EXISTS `ab_companies`;
	DROP TABLE IF EXISTS `ab_contacts_vcard_props`;
	DROP TABLE IF EXISTS `ab_default_email_account_templates`;
	DROP TABLE IF EXISTS `ab_default_email_templates`;
	DROP TABLE IF EXISTS `ab_email_templates`;
	DROP TABLE IF EXISTS `ab_portlet_birthdays`;
	DROP TABLE IF EXISTS `ab_search_queries`;
	DROP TABLE IF EXISTS `ab_sent_mailing_companies`;
	DROP TABLE IF EXISTS `ab_sent_mailing_contacts`;
	DROP TABLE IF EXISTS `ab_sent_mailings`;
	DROP TABLE IF EXISTS `ab_settings`;
	DROP TABLE IF EXISTS `cf_ab_companies`;
	DROP TABLE IF EXISTS `cf_ab_contacts`;


.. warning:: When installing the newsletter module ```ab_contacts``` and ```ab_addresslist*``` are used
	to create address lists in the newsletter module. If newsletters is installed or you want a
	clean newsletter module the following tables are safe to remove:

.. code:: sql

	DROP TABLE IF EXISTS `ab_addresslist_companies`;
	DROP TABLE IF EXISTS `ab_addresslist_contacts`;
	DROP TABLE IF EXISTS `ab_addresslists`;
	DROP TABLE IF EXISTS `ab_contacts`;


Notes module was replaced. All notes are in tables starting with ``notes_`` and all 
tables starting with ``no_`` can be removed.

.. code:: sql

	DROP TABLE IF EXISTS `no_categories`;
	DROP TABLE IF EXISTS `no_notes`;


The linking mechanism was changed, links are new stored in ``core_link``

.. code:: sql

	DROP TABLE IF EXISTS `go_links_ab_addresslists`;
	DROP TABLE IF EXISTS `go_links_ab_companies`;
	DROP TABLE IF EXISTS `go_links_ab_contacts`;
	DROP TABLE IF EXISTS `go_links_bs_orders`;
	DROP TABLE IF EXISTS `go_links_cal_events`;
	DROP TABLE IF EXISTS `go_links_em_links`;
	DROP TABLE IF EXISTS `go_links_fs_files`;
	DROP TABLE IF EXISTS `go_links_fs_folders`;
	DROP TABLE IF EXISTS `go_links_pr2_projects`;
	DROP TABLE IF EXISTS `go_links_ta_tasks`;
	DROP TABLE IF EXISTS `go_links_ti_tickets`;

The ``ipwhitelist`` module was removed and is now part of the core and stored in ``core_auth_allow_group``

.. code:: sql

	DROP TABLE IF EXISTS `wl_ip_addresses`;
	DROP TABLE IF EXISTS `wl_enabled_groups`;



6.5 or higher
~~~~~~~~~~~~~~~~~~~~~
Business / employee management changed
new history module
new search module

Parts of the projects module was moved to a separate Business module data of 
the below tables is stored in ``business_activity``, ``business_activity_rate`` and ``business_employee``

.. code:: sql

	DROP TABLE IF EXISTS `pr2_employees`;
	DROP TABLE IF EXISTS `pr2_standard_tasks`;
	DROP TABLE IF EXISTS `pr2_employee_activity_rate`;



The history module was introduced and the go_log table will no longer be filled with new
log entries. The table is unused.

.. code:: sql

	DROP TABLE IF EXISTS `go_log`;



6.6 or higher
~~~~~~~~~~~~~~~~~~~~~
The Tasks module was replace with a new version. Tables starting with ``ta_``

.. code:: sql

	DROP TABLE IF EXISTS `ta_categories`;
	DROP TABLE IF EXISTS `ta_portlet_tasklists`;
	DROP TABLE IF EXISTS `ta_settings`;
	DROP TABLE IF EXISTS `ta_tasklists`;
	DROP TABLE IF EXISTS `ta_tasks`;
	DROP TABLE IF EXISTS `cf_ta_tasks`;


6.7 or higher
~~~~~~~~~~~~~~~~~~~~~

There is a new billing module but the old one can still be used or uninstalled


6.8 or higher
~~~~~~~~~~~~~~~~~~~~~

This release was focussed to support latest PHP version. There were no database tables obsoleted.


25.1 or higher
~~~~~~~~~~~~~~~~~~~~~

The Calendar module was replaced with a new version.

.. code:: sql

	DROP TABLE IF EXISTS `cal_calendar_user_colors`;
	DROP TABLE IF EXISTS `cal_calendars`;
	DROP TABLE IF EXISTS `cal_categories`;
	DROP TABLE IF EXISTS `cal_events`;
	DROP TABLE IF EXISTS `cal_events_declined`;
	DROP TABLE IF EXISTS `cal_exceptions`;
	DROP TABLE IF EXISTS `cal_group_admins`;
	DROP TABLE IF EXISTS `cal_groups`;
	DROP TABLE IF EXISTS `cal_participants`;
	DROP TABLE IF EXISTS `cal_settings`;
	DROP TABLE IF EXISTS `cal_views`;
	DROP TABLE IF EXISTS `cal_views_calendars`;
	DROP TABLE IF EXISTS `cal_views_groups`;
	DROP TABLE IF EXISTS `cal_visible_tasklists`;

	DROP TABLE IF EXISTS `cf_cal_calendars`;
	DROP TABLE IF EXISTS `cf_cal_events`;
	DROP TABLE IF EXISTS `calcom_event_company`;
	DROP TABLE IF EXISTS `caltt_time_entry`;



Holidays are specified with rules in JSON files for the new calendar.

.. code:: sql

	DROP TABLE IF EXISTS `go_holidays`;

The favorite module is removed. Tasks, Calendars and Address book use a subscribe mechanism

.. code:: sql

	DROP TABLE IF EXISTS `fav_calendar`;
	DROP TABLE IF EXISTS `fav_tasklist`;
	DROP TABLE IF EXISTS `fav_addressbook`;
