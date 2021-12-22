Holidays
========

Using the holidays module, you can manage the leave hours of employees. Every year, an amount of available leave hours
(year credit) can be set per user. In this module, every employee can be given a total year credit of leave hours to
spend in a year. Every subsequent month, 1/12th of this available credit is added to the spendable credit.

Up to version 6.4, for each leave type, the budget had to be set for each individual year. In version 6.5 and up, a yearly
credit is directly applied to the current employee agreement. Each year, the budget is renewed until an agreement is either
updated or cancelled. Please see the :ref:`business <business>` page for more information

Specifically, for every user and every year, the following statistics are tracked:

- Leftover: The number of leave hours that were not used in previous years.
- Yearly credit: The year credit (available leave hours) for the selected year.
- Used: The leave hours that are spent in the selected year.
- Built up: The built up credit ( = LEFTOVER_CREDIT + YEAR_CREDIT x (current month's number/12) )
- Available year: The total available leave hours for the selected year ( = LEFTOVER_CREDIT + YEAR_CREDIT - SPENT_CREDIT )
- Available now: The available leave hours for the current month ( = LEFTOVER_CREDIT + YEAR_CREDIT x (current month's number/12) - SPENT_CREDIT_UNTIL_NEXT_MONTH )

To edit the yearly credit, double-click on a row in the main grid 'Holiday Hour Credits'.

.. figure:: /_static/using/holidays/holidays-module.png
   :width: 100%

   Holidays module

Working week
------------

In the :ref:`user's preferences <my-account>`, you can now set the standard amount working hours per day for users. This will be used to auto-calculate the number of used leave hours when you edit/create a holiday entry. You can always change the number of used leave hours of a holiday.

Note that the working week is by default for all users in the Holidays module: 8 hours on Monday thru Friday, 0 hours on Saturday and Sunday.

Leave types
-----------

There are roughly two types of leave days: leave days (most commonly holidays) and special leave. The main difference is
that leave days are commonly budgeted by year, whereas special leave is incidental.

Holidays
````````

The workflow for a holiday request is pretty simple. An employee can file a request for a holiday. The manager will
either approve or deny the request. After each step, an email message is sent to both parties.

Special leave
`````````````

There are two ways to create a special leave budget:

1. The employee files a leave request in the common way. The only difference is that the chosen leave type is special leave. When the manager approves this request, a special leave budget will be created automatically.
2. The manager can create a special leave budget manually for the employee. It is up to the employee to file requests to spend the budgeted hours.

A manager can edit leave budgets as needed, e.g. when an employee is entitled to more or fewer hours than initially requested.

Manager
-------
For each employee you can set a manager. The manager will get a request to approve the holidays by e-mail when an
employee adds new holidays.

.. note::

   Managers will need manage permissions for the module so they can see all employees hours and approve them.
