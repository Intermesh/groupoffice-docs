Cleaning up
===========

Older Group-Office instances that have gone through several version upgrades have lots of old data stored in their
databases. As older modules get replaced by newer modules, old database items are being converted to new database items.
The database of the old module will not be deleted by default, but as the newer modules use the new tables, the old
tables just take up space.

We sometimes get the question which tables are safe to remove. This table will list the old tables, the replacement
tables and the modules if applicable.

.. table:: PHP settings
   :widths: auto

   ==============  =========================  =============  ==============   =======
   Old namespace   Current namespace          Old Module     Current Module   Version
   ==============  =========================  =============  ==============   =======
   ``ab_*``        ``addressbook_*``          Addressbook    Addressbook      6.4
   ``cf_*``        ``core_customfields``      customfields   core             6.3
   ``go_links_*``  ``core_links``             core           core             6.3
   ``go_log``      ``history_log_entry``      core           history          6.5
   ``pm_*``        ``pr2_*``                  projects       projects2        ?
   ``ml_*``        ``newsletters_*``          mailings       newsletters      6.4
   ``sy_*``        ``sync_*``                 sync           sync             6.3
   ``ta_*``        ``tasks_*``                tasks          tasks            6.6
   ``wl_*``        ``core_auth_allow_group``  whitelist      core             6.4
   ==============  =========================  =============  ==============   =======

.. note:: If the old namespace column does not contain an asterisk, please consider it a single database table.

.. warning:: Do this at your own risk!
