.. _cli:

Command Line Interface
======================

Group Office also has a Command Line Interface. To implement this do the following:

1. Create a controller that extends the abstract controller in folder 'go/modules/tutorial/music/cli/controller':

   .. code:: php

      <?php

      namespace go\modules\tutorial\music\cli\controller;

      use go\core\Controller;

      class CliDemo extends Controller {
        public function hello($name = "World") {
          echo "Hello $name!\n";
        }
      }
      
   .. note: The controller must be in the "cli\controller" namespace so these methods can't be invoked via JMAP.

2. Run (Notice the path is case sensitive!)::
	
      sudo -u www-data php /usr/share/groupoffice/cli.php tutorial/music/CliDemo/hello --name=Merijn

   or with docker-compose::

      docker-compose exec --user www-data groupoffice-master php /usr/local/share/groupoffice/cli.php tutorial/music/CliDemo/hello --name=Merijn

3. This should output::

      Hello Merijn!

.. note:: Command line methods always run as the administrator user so you should probably need to sudo into the web user (www-data)
				
				
Specify config file
-------------------
				
If you have a multi instance environment you can specify the config file location
with the 'c' argument::
				
   php /usr/share/groupoffice/cli.php tutorial/music/CliDemo/hello --name=Merijn -c=/etc/groupoffice/multi_instance/domain.com/config.php


JMAP via CLI
------------

It's possible to execute any JMAP method via the Command Line Interface. You can do this via the command::

   ./cli.php core/System/jmap

It reads the standard input. It's the easiest way to supply the input via a json file.

Here are some examples for an address book. They can also be used for any other entity as it's all standard JMAP
except for the more advanced export example.

Create address book
```````````````````

jmap.json::

    [
      [
        "AddressBook/set",
        {
          "create": {
            "myClientId": {
              "name": "Shared"
            }
          }
        },
        "call-1"
      ]
    ]


.. note:: You can replace "myClientId" with any ID string you like.

You can run it with this command::

   ./cli.php core/System/jmap < jmap.json

It should output something like this::

    [
        [
            "AddressBook\/set",
            {
                "accountId": null,
                "created": {
                    "myClientId": {
                        "acl": null,
                        "permissionLevel": 50,
                        "id": 11,
                        "aclId": 183,
                        "createdBy": 1,
                        "filesFolderId": null,
                        "salutationTemplate": "Dear [if {{contact.prefixes}}]{{contact.prefixes}}[else][if !{{contact.gender}}]Ms.\/Mr.[else][if {{contact.gender}}==\"M\"]Mr.[else]Ms.[\/if][\/if][\/if][if {{contact.middleName}}] {{contact.middleName}}[\/if] {{contact.lastName}}",
                        "groups": []
                    }
                },
                "updated": null,
                "destroyed": [],
                "notCreated": null,
                "notUpdated": null,
                "notDestroyed": null,
                "oldState": "4:0:2",
                "newState": "5:0:2"
            },
            "call-1"
        ]
    ]

Query address books
```````````````````
jmap.json::

    [
      [
        "AddressBook/query",
        {
          "filter": {
            "name": "Shared"
          }
        },
        "call-1"
      ]
    ]

You can run it with this command::

./cli.php core/System/jmap < jmap.json

It should output something like this::

    [
        [
            "AddressBook\/query",
            {
                "accountId": null,
                "state": "6:0:2",
                "ids": [
                    1
                ],
                "notfound": [],
                "canCalculateUpdates": false,
                "query": "SELECT a.id \nFROM `addressbook_addressbook` `a`\nWHERE \n (\n\t (\n\t\t `a`.`name` LIKE 'Shared'\n\t)\n)"
            },
            "call-1"
        ]
    ]

Get an address book
```````````````````

jmap.json::

    [
      [
        "AddressBook/get",
        {
          "ids": [1]
        },
        "call-1"
      ]
    ]

You can run it with this command::

./cli.php core/System/jmap < jmap.json

It should output something like this::

    [
        [
            "AddressBook\/get",
            {
                "accountId": [],
                "state": "6:0:2",
                "list": [
                    {
                        "acl": {
                            "3": 40
                        },
                        "permissionLevel": 50,
                        "id": 1,
                        "name": "Shared",
                        "aclId": 13,
                        "createdBy": 1,
                        "filesFolderId": null,
                        "salutationTemplate": "Dear [if {{contact.prefixes}}]{{contact.prefixes}}[else][if !{{contact.gender}}]Ms.\/Mr.[else][if {{contact.gender}}==\"M\"]Mr.[else]Ms.[\/if][\/if][\/if][if {{contact.middleName}}] {{contact.middleName}}[\/if] {{contact.lastName}}",
                        "groups": []
                    }
                ],
                "notFound": []
            },
            "call-1"
        ]
    ]

Query and get an address book
`````````````````````````````
The two examples above can be combined with a result references::

    [
      [
        "AddressBook\/query",
        {
          "filter" : {
            "name" : "Shared"
          }
        },
        "call-1"
      ],
      [
        "AddressBook/get",
        {
          "#ids": {
            "resultOf": "call-1",
            "path": "ids"
          }
        },
        "call-2"
      ]
    ]

You can run it with this command::

./cli.php core/System/jmap < jmap.json

It should output something like this::

    [
        [
            "AddressBook\/query",
            {
                "accountId": null,
                "state": "6:0:2",
                "ids": [
                    1
                ],
                "notfound": [],
                "canCalculateUpdates": false,
                "query": "SELECT a.id \nFROM `addressbook_addressbook` `a`\nWHERE \n (\n\t (\n\t\t `a`.`name` LIKE 'Shared'\n\t)\n)"
            },
            "call-1"
        ],
        [
            "AddressBook\/get",
            {
                "accountId": [],
                "state": "6:0:2",
                "list": [
                    {
                        "acl": {
                            "3": 40
                        },
                        "permissionLevel": 50,
                        "id": 1,
                        "name": "Shared",
                        "aclId": 13,
                        "createdBy": 1,
                        "filesFolderId": null,
                        "salutationTemplate": "Dear [if {{contact.prefixes}}]{{contact.prefixes}}[else][if !{{contact.gender}}]Ms.\/Mr.[else][if {{contact.gender}}==\"M\"]Mr.[else]Ms.[\/if][\/if][\/if][if {{contact.middleName}}] {{contact.middleName}}[\/if] {{contact.lastName}}",
                        "groups": []
                    }
                ],
                "notFound": []
            },
            "call-2"
        ]
    ]

Update an address book
``````````````````````
We rename it to public and give group with ID = 1 (Everyone) read permissions.

jmap.json::

    [
      [
        "AddressBook/set",
        {
          "update": {
            "10": {
              "name": "Public",
              "acl": {
                    "3": 40,
                    "1": 10
              }
            }
          }
        },
        "call-1"
      ]
    ]

You can run it with this command::

   ./cli.php core/System/jmap < jmap.json

It should output something like this::

    [
        [
            "AddressBook\/set",
            {
                "accountId": null,
                "created": null,
                "updated": {
                    "10": null
                },
                "destroyed": [],
                "notCreated": null,
                "notUpdated": null,
                "notDestroyed": null,
                "oldState": "3:0:2",
                "newState": "4:0:2"
            },
            "call-1"
        ]
    ]

Delete an address book
``````````````````````

jmap.json::

    [
      [
        "AddressBook/set",
        {
          "destroy": [9]
        },
        "call-1"
      ]
    ]

You can run it with this command::

   ./cli.php core/System/jmap < jmap.json

It should output something like this::

    [
        [
            "AddressBook\/set",
            {
                "accountId": null,
                "created": null,
                "updated": null,
                "destroyed": [
                    9
                ],
                "notCreated": null,
                "notUpdated": null,
                "notDestroyed": null,
                "oldState": "1:0:2",
                "newState": "2:0:2"
            },
            "call-1"
        ]
    ]


Export address book example
```````````````````````````
Here's an example on how to export an address book:

jmap.json::

    [
      [
        "AddressBook/query",
        {
          "filter": {
            "name": "Shared"
          }
        },
        "call-1"
      ],
      [
        "Contact/query", {
          "filter": {
            "#addressBookId": {
              "path": "/ids",
              "resultOf": "call-1"
            }
          }
        },
        "call-2"
      ],
      [
        "Contact/export", {
          "#ids": {
            "path": "/ids",
            "resultOf": "call-2"
          },
          "extension": "xlsx"
        },
        "call-3"
      ],
      [
        "core/System/blob", {
        "#id": {
          "path": "/blob/id",
          "resultOf": "call-3"
        }
      },
        "call-3"
      ]
    ]

There are 4 JMAP calls:

1. Get the address book named "Shared". You can skip this step if you know the ID and pass that directly in call 2.
2. Get all contacts from the address book returned in call 1.
3. Pass the contact id's to the export method.
4. Grab the generated blob ID and output the raw file data.

You can run it with this command::

   ./cli.php core/System/jmap < jmap.json > contacts.xlsx

We pipe the output directly to a file because the System/blob outputs binary data in this case.


.. note:: We also created a wrapper command to do this::

      ./cli.php community/addressbook/AddressBook/export --addressBookId=3 --format=csv
      
   And these too::
   
      ./cli.php community/addressbook/AddressBook/delete --addressBookId=3
      ./cli.php community/tasks/Tasklist/export --tasklistId=4 --format=csv
      ./cli.php community/notes/NoteBook/export --noteBookId=65 --format=csv
      ./cli.php community/tasks/Tasklist/delete --tasklistId=4
      ./cli.php community/tasks/NoteBook/delete --tasklistId=4
      ./cli.php  core/System/deleteGroup --id=29
      ./cli.php  core/System/deleteUser --id=29
      
   
      
      
