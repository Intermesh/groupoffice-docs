.. _support:

Support
=======

The support module enables you and your users to manage support requests. It is intended to replace the :ref:`tickets`
module. In version 6.7, both modules are supported. This may make it easier for administrators to migrate from
the obsolete Tickets module to the more modern Support module.

.. figure:: /_static/using/support/support-module.png
   :width: 100%

   Support module

The tickets module supports:

- :ref:`links`
- :ref:`custom-fields`
- :ref:`sharing`
- :ref:`files`

One can install and configure the 'Help' module to enable end users to submit support requests from within Group-Office.

Roles
-----

1. **End users** are the users that need support and will enter tickets.
2. **Ticket agents** are the people who need to pick up and solve said tickets.
3. **Managers** configure the ticket module.

Entering a ticket
-----------------

There are roughly three ways to enter a ticket:

1. Send an email to a certain mailbox;
2. Create one manually from within the Support module;
3. Create one manually from within the Help module;

When an end user sends an email to a support mailbox, they are matched to an existing user in Group-Office. If they do
not exist, a new user is created. In order for this to work, currently you must enable user registration in System Settings.

Help module
```````````

This is a simple module that enables end users to submit tickets from within Group-Office itself. In this module, the
user can see their own submitted tickets. Entering a new ticket is as easy as clicking the button 'New Request':

.. figure:: /_static/using/support/new-request.png
   :width: 100%

   Submit a support request from within Group-Office


Usage by ticket agents
----------------------

Ticket types
````````````

Tickets are commonly divided among certain types, depending on the nature of the ticket. For a ticket agent, a bug fix is
commonly different from a documentation request or an invoicing issue. The administrator can assign permissions by ticket
type, both on the customer side and on the agent side.


Ticket categories
`````````````````

A secondary means of adding contextual information to tickets is by assigning categories. These are agnostic of
ticket type or permissions. Categories are intended to act as quick filters.

Ticket statuses
```````````````
In order to know which tickets are still actionable, you can assign ticket statuses. At the time of this writing, we use
the standard task statuses as `specified <https://datatracker.ietf.org/doc/html/rfc5545>`_ in the iCalendar specification.


.. note:: If you compare the support module to the :ref:`Tasks` module, you'll notice heavy similarities. This is by
	design, as we consider support tickets a special type of tasks.



Administration
--------------

Module permissions
``````````````````

When a user has 'Manage' permissions for the Support module, they will be considered a manager. Users and groups with
use permissions for the module are considered ticket agents.

System settings
```````````````

.. figure:: /_static/using/support/system-settings.png
   :width: 100%

   System settings panel for the support module

The system settings panel allows the administrator to configure task lists and link email accounts to said task lists.
A task list is considered its own ticket type. This will enable the administrator to assign different ticket types
to different users or groups as they wish.

Emails sent to a configured mailbox will be automatically converted to tickets.

Task list management
````````````````````

Task lists can be assigned names, groups, customer permissions and agent permissions. The difference between customer
permissions and agent permissions is that customer permissions are meant for the users who can enter new tickets, whereas
the agent permissions are meant for the ticket agents and their permissions for tickets within the list.

.. note:: Under the hood, tickets are simply saved as tasks. Hence, the classification of task lists as ticket types.


