Tasks
=====

In the tasks module, the user can manage tasks and task lists. As opposed to projects, tasks are single actions that need
to be done in order to achieve a certain goal. The tasks module is part of the community package.

.. figure:: /_static/using/tasks/tasks-module.png
   :width: 100%

The tasks module supports:

- :ref:`links`
- :ref:`custom-fields`
- :ref:`comments`
- :ref:`sharing`
- :ref:`files`


In version 6.6, the tasks module was entirely refactored, integrating tasks more fully with other modules.
As of 6.6 the :ref:`projects` module supports task lists and tasks. At the time of this writing, other modules
are scheduled to support tasks in a similar way.

Task lists
``````````

The most common way to organize tasks is through task lists. By default, each user has their own personal task list.
Task lists are an ACL entity, which means that a task list can be shared among users. Tasks within the task list inherit
those permissions.

Task list types
+++++++++++++++

In the task module screen, only the task lists are shown that are not part of a project. This is by design. If you have
thousands of projects, each with their own tasks lists, the list of task lists would get very messy.

Currently, the following task list types are used:

1. User task lists
2. Project task lists
3. Board task lists

Default task lists
++++++++++++++++++

A user can set a default task list, such as a personal task list, or a task list that is shared among a user group.
Alternatively, the last used task list can be remembered. If the user visits the tasks module again, it will select the
last selected task list.

This can be set in My Account > Tasks.

Adding and editing tasks
````````````````````````

.. figure:: /_static/using/tasks/tasks-module.png
   :width: 100%

When creating or editing an existing task, there is support for the following fields and settings:


+------------------------+------------------------------------------------------------+
| Property               | Description                                                |
+========================+============================================================+
| Title                  | The title of the task, displayed in your task list         |
+------------------------+------------------------------------------------------------+
| Start / End date       | Optional start and end dates                               |
+------------------------+------------------------------------------------------------+
| Progress / % complete  | Status on the progress of a task. When a task is 100%      |
|                        | complete, it is considered done.                           |
+------------------------+------------------------------------------------------------+
| Estimated duration     | If hours are registered on a task, the %complete field     |
|                        | will update accordingly                                    |
+------------------------+------------------------------------------------------------+
| Recurrence             | Recurring tasks are tasks that repeat themselves using a   |
|                        | preset period.                                             |
+------------------------+------------------------------------------------------------+
| Description / Location | Optional additional information about the task itself      |
+------------------------+------------------------------------------------------------+
| Task list              | Selects parent task list                                   |
+------------------------+------------------------------------------------------------+
| Category               | Add optional categories to your task                       |
+------------------------+------------------------------------------------------------+



Categories
``````````

Categories allow the user to collect tasks that are similar in scope, but not necessarily in the same task lists. They
can be used as quick filters and additional contextual information.