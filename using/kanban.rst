Kanban
======

The Kanban module lets you create boards to implement the Kanban method. It uses entities from other Group Office modules, such as **Tasks** and **Projects**, so you can create cards based on those items.

**Core features:**
 * Create boards with custom columns
 * Use existing entities (tasks, support tickets, projects) as cards
 * Map statuses to columns per entity type

.. figure:: /_static/using/kanban/kanban-module.png  
   :width: 100%  

   Kanban module  

The Board
~~~~~~~~~

A kanban board can be used for many things and we have tried to make this module as adaptable as it can be to your workflow.
Every board is separate from each other, which means that cards referencing the same task, project or support ticket can exist in multiple boards at once.

.. figure:: /_static/using/kanban/board-dialog.png
   :width: 75%

   Board management


Besides the name of the board you are also free to edit the columns, permissions and retention days.

Backlog
~~~~~~~~~
Every Kanban board has a backlog column. This backlog contains cards you can add to your board.  
You can choose which cards appear in the backlog by setting a filter.

.. figure:: /_static/using/kanban/filter-dialog.png
   :width: 75%

   Filter management

The related tasks, tickets, or projects from these sources will appear as backlog cards.
These filters can be changed at any time, if you prefer to add a card directly to a column you can do so by searching Group Office or creating a new entity directly.

.. figure:: /_static/using/kanban/add-button.png
   :width: 50%

   Add card to column


Columns
~~~~~~~~~
Besides the backlog, you can define as many columns as you need. By default the board will create the columns: TODO,
Doing and Done. There is no need to keep these columns, you can rename and reorder columns to fit your workflow.

**Status mapping:**  
Each column can have an optional status mapping that sets the status of an entity when its card is moved to that column.

.. figure:: /_static/using/kanban/column-dialog.png  
   :width: 75%  

   Status mapping  

.. note:: If an entity’s status changes outside the Kanban board, its card will automatically move to the column mapped to the new status, if available.  

For each board, you can designate one column as the final column. Cards in this column will automatically be removed after the defined retention period.  
If no final column is set, the rightmost column will be treated as the final one.

Cards
~~~~~~~~~
Each card on a board represents either a task, project or support ticket from their respective modules in Group Office.
It is important to note that a card is dependent on the entity it represents but not the other way around.
For example if the task that a card is based on is deleted that card will also be deleted, but if the card is deleted the task will still exist.
