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

**Backlog**
```````
Every Kanban board has a backlog column. This backlog contains cards you can add to your board.  
You can choose which cards appear in the backlog by tracking task lists, support lists, project books, or projects.  
The related tasks, tickets, or projects from these sources will appear as backlog cards.

.. figure:: /_static/using/kanban/board-dialog.png  
   :width: 75%  

   Board management  

**Columns**
```````
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
