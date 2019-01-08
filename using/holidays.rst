Holidays
========

Using the holidays module, you can manage the leave hours of employees. Every year, an amount of available leave hours (year credit) can be set per user. In this module, every employee can be given a total year credit of leave hours to spend in a year. Every subsequent month, 1/12th of this available credit is added to the spendable credit.

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

Manager
-------
For each employee you can set a manager. The manager will get a request to 
approve the holidays by e-mail when an employee adds new holidays.

.. note::

   Managers will need manage permissions for the module so they can see all employees hours and approve them.
