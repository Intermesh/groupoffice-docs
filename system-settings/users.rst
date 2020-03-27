Users
=====

When clicking users you will see a list of all Group-Office users. Via the "more"
menu in the record you can:

1. Edit the user
2. Login as this user
3. Delete the user

.. note:: Instead of deleting users you can also disable them. This will keep
   all data and references to the user but the user can't login or used for new
   items. To deactivate a user you must "Edit" it and toggle "Login enabled" on 
   the account page.

.. figure:: /_static/system-settings/users.png
   :alt: User list

   User list

User defaults
-------------

Before adding any user. Check the 'User settings' to avoid unnecessary changes to 
user settings after creating them. 

Click the settings icon to change default values and manage custom fields.

.. figure:: /_static/system-settings/user-settings.png
   :alt: User settings

   User settings

Adding a user
-------------

.. note:: Before adding users make sure you've setup :ref:`user-groups` with the right
   module access. So setting up the user permissions is a simple matter of adding
   it to the right user group.

To add a user click the plus icon. A short wizard opens with three steps.

.. figure:: /_static/system-settings/create-user-1.png
   :alt: Create user step 1
   :width: 50%

   Create step 1

Supply the username, display name and e-mail address.

- Username is case insensitive.
- Display name is used in Group-Office
- Provide an account e-mail address. 
- Because often Group-Office is used as primary e-mail service you must provide
  a secondary e-mail address for e-mail recovery. If not available just use
  your primary e-mail.

.. figure:: /_static/system-settings/create-user-2.png
   :alt: Create user step 2
   :width: 50%

   Create step 2

Provide a password. You can also use the button in the first field top generate
a strong password.

.. figure:: /_static/system-settings/create-user-3.png
   :alt: Create user step 3
   :width: 50%

   Create step 3

Finally, add the user to the right :ref:`user-groups` andf click 'Finish'.

Edit user
---------

To edit a user double click or use the more menu. 
The edit dialog is identical to the ':ref:`my-account`' page but adds some administrative features:

- Group management
- Disable / enable login
- Set disk quota

Disk quota
``````````
If you leave this blank then users can use an unlimited amount of storage. If set
then the user will be limited to this amount of disk space.

Disk quota applies to all files in the user's home folder of the files module.
Other locations such as projects and address book folders are owned by the
"admin" user.

.. figure:: /_static/system-settings/my-account.png
   :width: 100%
   :alt: Edit user

   Edit user
   

.. _user-visibility:

Visibility of users
-------------------

By default all users are visible to eachother. You can see users when you share something with another user for example.
If you'd like to change this you need to change the default permissions of a new user group. Because every user get's
it's own personal group used for permissions. You can change this at :ref:`user-groups-defaults`.

You can change visibility settings per user in the user account page at the "Visible to" tab.

.. note:: After an upgrade from 6.2 none of the users are visible. This is a known issue. If you'd like to make all
   users visible then edit the :ref:`default-permissions` of "Group" and add for example group "Everyone" and click
   "Add to all". Now all users can see all groups and users.
