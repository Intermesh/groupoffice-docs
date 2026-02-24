
.. _workflow:

Workflow
========

With this module you can add steps that need approval to almost every item inside GroupOffice.

Simple example usage (homework)
+++++++++++++++++++++++++++++++

- A student needs to create homework and that needs to be checked by the teacher:
- The teacher can set a workflow process for a folder in the files module.
- If the student uploads a file to the folder, the authorized teacher need to approve the file.
- If the teacher finds that the document is OK, then he can approve the file and add a comment to it or if the document is NOT OK, then the teacher can add a comment to it and decline the document.
- The student can see if the document is approved or declined and he can see the reason of it.
- If it was declined, then the student can upload a new file to the folder and then the checking of the teacher begins again.

Simple example usage (billing)
++++++++++++++++++++++++++++++

- A employee can make invoices for the customers of the company where he is working.
- The administrator sets up a workflow process for the invoices which required approval before sending it to the customer.
- After the employee has created and saved an invoice, the manager gets a reminder that he must check the invoice.
- The manager can approve or decline the invoice and add a comment to it for the sake of the employee.
- If the invoice was declined(wrong) then the employee can edit it and save it again.

Adding a Workflow Process
`````````````````````````

.. note:: This can only done with the proper permissions.

Create a Workflow Process
+++++++++++++++++++++++++

1. Go to the "Workflow" tab inside GroupOffice.
2. Click on the "Administration" button.
3. The "Workflow process" grid will be showed in a new window. Click on "Add" to start creating a new workflow Process.
4. Fill in a name for the new workflow process and click on "Apply" to save it. (After you have clicked on "Apply" the other tabs ("Steps", "Permissions") will be enabled.
    1. In the "Steps" tab you can add the required steps that need to be followed in this workflow process. (See "Add steps to workflow processes" for an explanation)
    2. In the "Permissions" tab, you can set the permission for who can administer this particular workflow process.

Add Steps to Workflow Process
+++++++++++++++++++++++++++++

To add a step in a workflow process you need to go to the "Edit workflow" window. Go to the "Workflow" tab inside GroupOffice.

1. Click on the "Administration" button.
2. The "Workflow process" grid will be showed in a new window. Double click on an existing workflow process or click on "Add" to start creating a new workflow Process.
3. Click on the "Steps" tab.
4. To add a new step click on "Add", if you want to edit an existing step double click on it.
5. In the step edit window fill in the fields.
    - **Name**: This is the Name/Label for the current step.
    - **Description**: Here you can add a short description so you can clarify this step to the users.
    - **Due in (hours)**: Here you need to fill in how long this step will take. (The number of hours)
    - **Email alert**: If you enable this checkbox, every Authorized user will get an email when the workflow process is starting with the current step. (So they are notified by email that there is an step for them to take a look at)
    - **Popup alert**: If this one is enabled the authorized users will get a reminder automatically for the current step.
    - **Approve needed by all**: With this checkbox you can toggle if every or just one authorized user needs to approve the current step.
6. If you have filled in all the fields, click on "Apply" to save the Step.
7. Now the "Authorized groups" and "Authorized users" tabs will become available.
    - **Authorized groups**: Here you can add the groups that can authorize this step.
    - **Authorized users**: Here you can add individual users that can authorize this step.

.. note:: If you have checked the "Approve needed by all" checkbox in the "Properties" panel then every user in the Groups ans in the Users tab needs to approve this step.



Attach Workflow to an Entity
````````````````````````````

Attaching a workflow process to an item inside GroupOffice can be done as described in the steps below.

Attach to single item
+++++++++++++++++++++
1. Click on the item where you want to attach the workflow process on.
2. In the panel on the right side click on "New"->"Workflow".
3. A small window will appear on the screen.
4. Select the workflow process that you want to attach and fill in the "Shift due time (hours)".
5. Click on "OK".

Now the workflow process is attached to the item. You can see the workflow process in the right panel.

Attach workflow processes automatically
+++++++++++++++++++++++++++++++++++++++

For files you can let the system automatically attach a workflow. To set this up you need to follow the steps below:

1. Go to the "Files" module.
2. Right click on the desired folder where to store the items with a workflow process.
3. Choose "Properties".
4. In the folder properties window click on the "Workflow" tab.
5. Select a workflow process that needs to be attached to each file that is added to this folder.
6. Click on "OK" or "Apply" to save it.

Now the selected workflow process will be automatically added to each file that is put inside this folder.

Accept or Decline
`````````````````

If you have permission to administer a step then you can approve or decline items that have that step. Each item
that has a step that you can administer is displayed in the workflow grid. If you double click on an item in the
grid (or just double click on the item itself) a popup will come up in wich you can approve or decline the step.


After you have clicked on "Approve" or "Decline" a small window will appear on the screen in where you need to add
some comments. This comment is needed to clarify your approval or decline back to the user(owner) of the file.
