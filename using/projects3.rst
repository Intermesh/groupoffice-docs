Projects and time tracking
==========================

With the projects module you can easily manage project information in one place and keep track of worked hours, tasks, costs and billing.

.. figure:: /_static/using/projects3/projects3.png
   :width: 100%

   Projects module

The projects module supports:

- :ref:`links`
- :ref:`custom-fields`
- :ref:`comments`
- :ref:`sharing`
- :ref:`files`

Business setup
---------------

When you start using the projects module and you want to track time you must setup the business and employees.

Go to **System setting** -> **Business** and configure using the :ref:`business documentation <business>`. If you don't set this
up you can't add project resources and **they can't track time**.

Creating a project
------------------

You can of course add a project by clicking the "**+ Add**" button from the projects module. But you can also create it from
an e-mail. If for example an e-mail comes in from a client requesting to start a project you can create a project from
the e-mail right away:

.. figure:: /_static/using/projects3/4-project-request-email.png
   :width: 100%

   Project request e-mail


From the e-mail view click the **Save as** -> **Project** button:

.. figure:: /_static/using/projects3/5-create-project-from-email.png
    :width: 100%

    Create project from e-mail

The create project dialog will appear. If the contact is recognized the contact and organisation are prefilled:

.. figure:: /_static/using/projects3/6-project-dialog.png
    :width: 100%

    Create project dialog

The original e-mail will be linked to the project as well. In this case we will select "Time is billable by default" because we will
post calculate our fees. We also set a start and due date and we'll add an employee. Click "Save" to continue to the project detail:

.. figure:: /_static/using/projects3/7-project-detail.png
    :width: 100%

    Project detail

Milestones and tasks
--------------------

From the project detail view you can add milestones and tasks in the tasks section:

.. figure:: /_static/using/projects3/8-add-milestone.png
    :width: 100%

    Add milestone


The milestones and tasks appear on the project detail:

.. figure:: /_static/using/projects3/9-project-tasks.png
    :width: 100%

    Project milestones and tasks


Time tracking
-------------

Now that you've setup a project you can register time on for the employees added to the project. Go to the
"Time registration" and click an "Add" button to drag a time entry on the grid. The create time registration dialog
will appear:

.. figure:: /_static/using/projects3/11-add-time-entry.png
    :width: 100%

    Add time entry

Note that the "Billable" switch is on by default as we enabled that in the project. This way we can bill it later.

Select the project and optionally a task and click "Save". You can see the time entries on the grid:

.. figure:: /_static/using/projects3/12-time-entries.png
    :width: 100%

    Time entries

Finance
-------

Now that we have some time entries to bill we can head back to the project detail. A "Project finance" section will appear now:

.. figure:: /_static/using/projects3/13-project-finance.png
    :width: 100%

    Project finance

Here you can see all financial info about the project:

- **Actual hours**: The amount of hours spent from the budget. These are not billable and part of a fixed price project.
- **Billable hours**: The amount of billable hours coming from the time entries. These hours come on top off the budgeted hours based on a fixed price.
- **Outstanding (billable hours)**: The hours that need to be billed.
- **Invoiced**: The amount already invoiced.
- **Outstanding (For invoice)**: The amount to be invoiced.
- **Profit**: The profit diagram and information shows what's left after taking off the costs. The costs come form the linked purchase invoices and the hourly costs form the employees.

Create invoice
--------------

From the project finance detail section you can create an invoice by clicking the "Create invoice" button. A dialog
will appear where you can select what to invoice:

.. figure:: /_static/using/projects3/14-create-invoice-from-project.png
    :width: 100%

    Create invoice from project dialog

Select the date up to which you want to select time entries and click "Create invoice" to continue:

.. figure:: /_static/using/projects3/15-project-invoice.png
    :width: 100%

    Project invoice


Click "E-mail" to send the invoice:

.. figure:: /_static/using/projects3/16-send-project-invoice.png
    :width: 100%

    Send project invoice

Completing the project
----------------------

When the project is done you can change the status to completed by clicking the status in the detail or the grid.


Quoted fixed price
------------------

In the workflow above we bill the time spent. But you might want to follow another workflow where you send a quote to
the client first and complete the project based on a fixed price. We also have this scenario covered.
When you create a project you don't enable "Time registrations are billable by default".
After creating the project you can create a quote (or link an existing one). From the "Add link" menu choose "Finance":

.. figure:: /_static/using/projects3/17-create-quote-from-project.png
    :width: 100%

    Create quote from project

For more information about creating quotes visit the :ref:`finance documentation <finance>`.

After creating the quote the project finance will be updated with the quote information. Note that I also edited the
project resources and added a budget for the hours:

.. figure:: /_static/using/projects3/17-1-finance-with-quote.png
    :width: 100%

    Project finance with quote

Create fixed price invoice
``````````````````````````

When the quote is added the quoted amount will show up in the finance section. When creating an invoice from there you
can choose the percentage of the quote you'd like to invoice:

.. figure:: /_static/using/projects3/18-create-invoice-for-fixed-price-project.png
    :width: 100%

    Create fixed price invoice

Click create invoice to continue.


Purchases
---------
When purchases are made you can create a purchase invoice from the project via the "Add link" menu. Choose "Purchase invoice".
If it's not available then please add a "Purchase invoice" book to the finance module first.

After creating a purchase invoice it will show up on the "Profit" section as "Purchases":

.. figure:: /_static/using/projects3/19-project-finance-with-purchases.png
    :width: 100%

    Project purchases


Reporting
---------

The projects comes with time reports and financial reports.client

Time report
```````````

It's easy to view the time spent on projects. Go to a project and click the **View time entries** button from the finance
section:

.. figure:: /_static/using/projects3/project-view-time-entries.png
    :width: 100%

    Project finance section


This will take you to the time registration list view:

.. figure:: /_static/using/projects3/time-entries-list.png
    :width: 100%

    Time entries list


Coming from the project finance it will automatically filter on billable hours only and on the project. You can change
the filters from the left.

You can export the list to **CSV** or **Microsoft Excel** using the more menu.


Finance report
``````````````

From the main projects view you can access the Finance report from the more menu:

.. figure:: /_static/using/projects3/projects3-more-menu-finance-report.png

    Open finance report

.. figure:: /_static/using/projects3/projects3-finance-report.png
    :width: 100%

    Project finance report


This report shows an overview of all projects with their financial data like **profit**, **outstanding hours and invoices** and **time spent**.

You can also filter on project status and employees.

Books
-----

A default book has been created at the installation. When editing the book you can add more statuses and change permissions.
You can also select the tasklist where project tasks should be created in.


Final words
-----------

This page covers two common workflows but the system is flexible to allow you to find your own ways. You can also add
custom fields, custom filters, files and links. You should have learned the basics now to get you started. If not then
we're here to help.