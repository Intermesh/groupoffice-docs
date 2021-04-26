System Tasks
============

The system tasks tab enables you to schedule automated tasks. These automated tasks are commonly referred to as
cron jobs, after the cron scheduling sysstem in most common Unix systems.

.. figure:: /_static/system-settings/system-tasks-overview.png
   :alt: System Settings - System Tasks

   System settings - System Tasks

The configuration of the scheduled jobs is easy:

.. figure:: /_static/system-settings/edit-system-task.png
   :alt: Edit a system task

   Edit a system task

When a scheduled task is disabled, it exists, but will not run at the scheduled time.

The `Expression` field refers to the time and date fields that a scheduled job runs. The syntax for this field is the
same as the ``/etc/crontab`` file. The five fields are separated by spaces and are respectively minute, hour, day of
month, month and day of week. In the screen shot above, the scheduled job is simply run every day at midnight. For more
syntax options, simply refer to the crontab manual page or the `online documentation
<https://manpages.debian.org/buster/cron/crontab.5.en.html>`_.

.. note:: The `BuildSearchCache` system task is disabled by default. You can manually enable it, but it will
   automatically disable itself. This is by design; a reindex may take a long time and should be done carefully.
