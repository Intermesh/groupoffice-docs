.. _business:

Business
========

When using GroupOffice Professional, this module is meant to manage one's own businesses or business units as well as
employees, fees and managers. You can also assign work schedules and fees for your employees.

These resources are shared among several other professional modules like :ref:`projects <projects>` and time
registration.

Administration
--------------

Business data is meant to be managed by administrators only. You can view and manage this from the System Administration
screen.

Businesses
``````````

First let's start by adding a business. For the sake of this documentation page, we choose to diversify and start our own
brewery named *Intermash*. We love our bad puns.

First, we add the contact data of the business to the :ref:`address book <address-book>`. Next, we open System Settings
and navigate to the Business tab. Click on the 'Add' button on top of the business list and fill in your data.

.. figure:: /_static/using/business/add-a-business.png
   :width: 100%

   Adding a business

If you like, you can add a default hourly revenue. Select your new organisation as your Contact, fill in the name and you
are set.

Activities
``````````

Our fictional brewery now needs a number of activities. An activity can be assigned to a time registration entry and can
be helpful in planning projects.

An activity can be defined as a type of work that you as an employee can do. Please note that this is not the same as a
task. Whereas a task is a type of action with a certain goal, an activity is a type of work that needs to be done in
order to perform said tasks.

Let's say that a typical brew process consists of roughly five major steps (For the sake of brevity, I omitted a few
cleaning steps):

1. Cleaning
2. Brewing
3. Cleaning
4. Bottling
5. Cleaning

So we need to define three activities: Brewing, Bottling and Cleaning. Of course, a typical brew process consists of
several more steps (milling, mashing, sparging, worrying about dirt and infections) but generally, these are part of
the same activity.

To enter a new activity, click on the 'Plus' sign on top of the right hand pane of the business management tab and
fill in the form.

.. figure:: /_static/using/business/add-an-activity.png
   :width: 100%

   Adding an activity

Activity types
''''''''''''''

When defining an activity, one has to define a type or category for said activity. Currently, the following types are
supported:

1. Work
2. Holidays
3. Absence
4. Special leave

There's also a number of settings available for each activity type:

- Budgetable: in order for the employee to register hours for this activity, a budget in hours needs to be defined.
- The budget expires: When a budget is set and this option is enabled, the remaining budget will be set to zero for the next year.
- Disabled: the employee is unable to register hours to this activity.

.. note:: Special leave and holidays are managed in the :ref:`holidays <holidays>` module.

Employee management
-------------------

In order for your Group Office users to use the business modules like projects, time tracking and finance, they need to be defined as employees. This is done
from the user management screen. When editing a user, select the tab 'Employee'.

.. figure:: /_static/using/business/edit-employee.png
   :width: 100%

   Edit employee data

The least that should be defined for an employee, is their business. In this case, the 'Intermash brewery' is preselected.
It is possible to assign a manager, income and expense rates and if an employee leaves a business, the
quitting date can be defined as well.

.. note:: It is not possible to assign an employee to more than one business.


Rates
`````

For projects and time tracking it's important to enter the hourly rates. The external fee is what should be charged to
clients and the internal fee is what the employee costs per hour.
When you work with multiple activity types you can also setup different rates per activity.

Last but not least, defining a work schedule for employees is easy. Above the 'Employee agreements' grid, click on the
Plus sign and fill in the hours for each week day.

.. figure:: /_static/using/business/employee-work-schedule.png
   :width: 100%

   Edit employee work schedule

Final word
----------

Now that you have defined your businesses and employee data, you should be able to assign employees to projects, tickets
and more and use activities to assign to time registration entries.