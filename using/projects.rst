Projects
========

With the projects module you can easily manage project information in one place and keep track of worked hours, material usage and travel costs. You can also share projects with customers and co-workers. With the project tasks it's easy for employees and the manager to keep track of the project progress.

The managers also have reports about progress and budgeting.

.. figure:: /_static/using/projects/projects-module.png
   :width: 100%

   Projects module

The projects module supports:

- :ref:`links`
- :ref:`custom-fields`
- :ref:`comments`
- :ref:`sharing`
- :ref:`files`


.. note:: Having trouble with making time entries? 

   Make sure the projects are not having a status that is closed. Also make sure 
   the user account is set as an `employee <employees_>`_ and project resource.

Administration
--------------

Permission types
````````````````
Permission types control who can access projects in the projects module. You don't set permissions per project but each project can have a permission type. If you're a small organization just one permission type might be sufficient. But if you have different departments it could be useful to setup a permission type for each department. It just depends on who may see the project information.

The permission levels are straight forward and you can read more about it :ref:`here <sharing>`.

.. note:: **Root level**

   Only users with manage permission on the projects module are allowed to create projects on the root level. To create sub projects you need at least create permission on the parent project.

Finance permissions
+++++++++++++++++++

Here you can control which users can see financial data like budgets and actual costs. Also the billing button to create invoices from time entries is only available to those users.

Templates
`````````

Project templates are very powerful. You can control what information the end user sees in the project information panel and edit dialog. The templates control:

1. Which standard fields are enabled on the project dialog.
2. Which custom field categories are enabled on the project dialog
3. Default project files and folders
4. Default project tasks
5. Default permission type and status
6. The icon displayed in the project tree and grid

.. figure:: /_static/using/projects/template.png
   :width: 50%

   Project template

Properties
++++++++++

The following properties can be configured:

+-----------------+------------------------------------------------------------+
| Property        | Description                                                |
+=================+============================================================+
| Name            | The name of the template                                   |
+-----------------+------------------------------------------------------------+
| Type            | The template type. Projects with a container type template |
|                 | have no time tracking and expenses functionality.          |
+-----------------+------------------------------------------------------------+
| Status          | The default status of the project                          |
+-----------------+------------------------------------------------------------+
| Permission type | The default permission type of the project                 |
+-----------------+------------------------------------------------------------+
| Enabled fields  | Controls which standard fields are enabled on the project  | 
|                 | dialog.                                                    |
+-----------------+------------------------------------------------------------+
| Icon            | An icon that will be disabled in the tree and grid         |
+-----------------+------------------------------------------------------------+

Jobs
++++

On this tab you can define default project jobs

.. figure:: /_static/using/projects/jobs.png
   :width: 50%

   Project jobs

Permissions
+++++++++++

On the permissions tab you can control which user may use the template.


Office times
````````````

Set the office times here. These times will be used for guessing the default time for new time entries and also for estimating a project task due date.

Statuses
````````
Manage project statuses here. Per status you can set if a project is completed or not if it's visible in the tree. 

.. note:: Missing projects in the tree or for time entries? Completed projects 
   won't be available for time tracking anymore. You can also set if the project 
   is visible in the tree. This is useful for keeping your projects overview 
   organized.

Activity Types
``````````````

Activity types will be available in a drop down when making time entries. It 
also has a preset for the description and duration.

It's also possible to exclude hours from billing or to setup different fees per activity type.

Employees
`````````

Every user that needs to be set as a resource for time tracking on projects need 
to be added here with their default fee. When a user closes it's time tracking 
week the closed date will be set forward. In this dialog you can set it back if
a mistake was made and the week needs to be opened again.

.. figure:: /_static/using/projects/employees.png
   :width: 50%

   Employees

To make the projects available for the time tracking module of a user you'll also need to define for each project which employees are working on it.
To do that, you'll need to open the edit dialog of a project and go to the "Employees" tab.
Add every employee for that project in this screen.

.. figure:: /_static/using/projects/project-resources.png
   :width: 50%

   Project resources / employees

Reports
-------

Group-Office comes with some reports that are useful for most businesses. But reports can also be customized if you have PHP knowledge. The Group-Office reports are available in source code. Intermesh also offers report customization. Contact us for more information about this.

The default reports are:

1. Time tracking entries in CSV
2. Project information and planning in PDF
3. Time entries in PDF
4. Overview of all projects in PDF

For more information about customizing reports you may want to read our [blog post about it](http://groupoffice.blogspot.com/2014/02/introduction-with-new-projects-version.html)


Time tracking
-------------

For users to be able to use time tracking the following conditions must be met:

1. The user has access to the time tracking module
2. The user is a resource of a project that does not have a [container](#templates) type template.
3. The project is not in a [closed status](#statuses).

Users don't need access to the projects module to use time tracking.

.. figure:: /_static/using/projects/time-tracking.png
   :width: 100%

   Time tracking

.. note:: Closing weeks

   Users can close weeks. When a week is closed the manager can approve the hours and the user can't edit the time entries anymore.

When a user accidentally closed a week the manager can reopen it at Administration -> Employees. Double click an employee and set the close date back in time.


Hours approval
--------------

Project managers can approve hours if this module is installed. The "Manager" property of projects is important here. Users can approve all time entries of projects that they are the manager of. Only hours that are closed will show up for approval. So users must first press the "Close week" button in the time tracking module.

Only approved hours will be billed to the billing module when you use this function.


Billing
-------

It's possible to generate invoices from your time tracking. To do so you have to 
create a project and set the type to "Post calculation". When time is recorded 
now the fees will be stored too. 

The default fees can be set at Administration -> Employees. When you create new
projects these values are copied to the project employees when you add them.

In the detail view of the project you see a summary of hours:

1. Booked: All the entries. 
2. Billable: Billable hours are the ones that have a fee. You can have no fee when 
   the project is not set to "Post calculation". You can also set "Not billable" 
   at activity types in administration. It's also not billable when you set zero 
   fee for the employee in the project.
3. Billed: An income was generated for these time entries.

.. figure:: /_static/using/projects/time-entry-summary.png
   :width: 50%

   Time entries summary in project detail view

Generate invoices
`````````````````

To generate an invoice go to Projects -> Financial -> Post calculation.
Select a time period and projects you want to invoice and click "Continue". An invoice will be stored in the project. 

If you have the billing module installed a popup will appear to also generate an invoice in the billing module.

.. note:: We plan to integrate the billing and projects more in GO 6.5 so this will become one.
