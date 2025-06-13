Projects and time tracking
==========================

With the projects module you can easily manage project information in one place and keep track of worked hours, tasks,
 costs and billing.

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

Go to System setting -> Business and configure using the :ref:`business documentation <business>`. If you don't set this
up you can't add project resources and they can't track time.

Creating a project
------------------

If for example an e-mail comes in from a client requesting to start a project you can create a project from the e-mail
right away:

.. figure:: /_static/using/projects3/4-project-request-email.png
   :width: 100%

   Project request e-mail


From the e-mail view click the "Save as" --> "Project" button:

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

From the project detail view you can add milestones and tasks:

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

- Quote amount: In this case 0 as we didn't add a quote to the project. But if you link a quote it will add up here.
- Billable fee: The amount of billable fee coming from the time entries
- Invoiced: The amount already invoiced.
- Outstanding: The amount to be invoiced.
- Profit: The profit diagram and information shows what's left after taking off the costs. The costs come form the
linked quotes and the hourly costs form the employees.

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
When you create a project you don't enable "Time regitrations are billable by default".
After creating the project you can create a quote (or link an existing one). From the "Add link" menu choose "Finance":

.. figure:: /_static/using/projects3/17-create-quote-from-project.png
    :width: 100%

    Create quote from project

For more information about creating quotes visit the :ref:`finance documentation <finance>`.

Create fixed price invoice
``````````````````````````

When the quote is added the quoted amount will show up in the finance section. When creating an invoice from there you
can choose the percentage of the quote you'd like to invoice:

.. figure:: /_static/using/projects3/18-create-invoice-for-fixed-price-project.png
    :width: 100%

    Create fixed price invoice

Click create invoice to continue.



Books
-----

A default book has been created at the installation. When editing the book you can add more statuses and change permissions.
You can also select the tasklist where project tasks should be created in.


Final words
-----------

This page covers two common workflows but the system is flexible to allow you to find your own ways. You can also add
custom fields, custom filters, files and links. You should have learned the basics now to get you started. If not then
we're here to help.