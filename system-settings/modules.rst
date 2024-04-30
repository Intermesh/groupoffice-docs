.. _modules:

Modules
=======

In this screen you can install modules and configure module access.

.. figure:: /_static/system-settings/modules-66.png
   :alt: Modules

   Modules

As of version 6.6, the modules screen is a bit more modern. The modules are grouped by package and they can be filtered
by status. It is also possible to search a module by name or description.

For each module, you can perform the following actions:

- **Install** a module. See below for details.
- **Disable** a module. You will not be able to use a module, but no data will be deleted. Upon re-enabling a module, it will continue working as before.
- **Permissions**. See below for details;
- **Delete** a module. This will entirely delete the module and all of its data! It cannot be recovered. Please use with care!

Installation
------------
After newly installing a module, a permissions window will pop up where you should select the user groups you want to
grant access. To change permissions later, please click on the 'share' icon.

.. _modules-permissions:

Permissions
-----------

The Current Way
```````````````

Since version 6.6, the module permissions have gotten an overhaul:

.. figure:: /_static/system-settings/module-permissions-66.png
   :alt: Module permissions

   Module permissions for the tasks module

In order to grant access to a group or user, just add them to the list above as per this screen shot. If a user is not
in the listed users or groups in this list, they have no access to the module.

The core module permissions can be set by clicking the button labeled 'System Permissions'. If a user does not have access
to the core module, they cannot use Group-Office. Use with care.

.. figure:: /_static/system-settings/module-add-permissions-66.png
   :alt: Add a group to task permissions

   Add a new group or user to task permissions

A big difference between the old permissions system and the new system, is that it is easier to define custom permissions.
In the example above, you can define which users or groups are allowed to manage task lists or task categories. This
is obviously only relevant to the tasks module, so this custom permission type will not be offered for other modules.



The Old Way
```````````
In the permissions window you can double click the level. You can choose "Use"
which grants basic access or "Manage" for users that need administrative functions
in the module.

You can also manage this at :ref:`group level <user-group-modules>`.

.. figure:: /_static/system-settings/module-permissions.png
   :alt: Module permissions

   Module permissions