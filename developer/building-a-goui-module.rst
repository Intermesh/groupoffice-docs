.. _goui_module:

Building a webclient module in GOUI
===================================

When you've finished the :ref:`server module<server_module>` it's time to build a web client. Please note
that the reviews are being added in the second part of this tutorial and that they
fall outside the scope of this document. We're going to create a 3 column responsive
layout with a Genre filter, artist list and artist detail view.

Most of our webclient framework is based our own Typescript framework named GOUI. We developed a website with design
principles and examples and you can find the documentation here:

https://goui.io/

On top of the GOUI framework, we have a groupoffice-core package that has everything that you need to run GOUI in Group-
Office.

The webclient code is located in the ``go/modules/tutorial/music/views/goui`` folder. We consider this the root of the
client side module code and will refer to this for the remainder of this tutorial. The root folder has the following files
and subfolders by default:

1. ``script``: This is the folder in which you put your Typescript code.
2. ``style``: This has your CSS overrides for your module, preferably in SASS format.
3. ``package.json``: has dependencies that are required to run this module, both in terms of own packages and third party packages.
4. ``tsconfig.json``: Typescript config.

Getting started
---------------

In order to be able to develop in GOUI, you need a recent LTS version of nodejs (which has the npm utility). At the time
of this writing, version 20 or 22 is a good choice.

If you haven't already, please create the ``go/modules/tutorial/music/views/goui`` folder and the files and subfolders
listed above.

First we create a ``package.json``` file in which you define your build and watch scripts. It should look like this:

.. code:: json

    {
      "type": "module",
      "devDependencies": {
        "concurrently": "latest",
        "esbuild": "latest",
        "sass": "latest",
        "typescript": "latest"
      },

      "scripts": {
        "start": "concurrently --kill-others \"npm run start:ts\"  \"npm run start:sass\"",
        "start:ts": "npx esbuild script/Index.ts --external:../../../../../../views/goui/* --bundle --watch --sourcemap --format=esm --target=esnext --outdir=dist",
        "start:sass": "npx sass --watch style:dist",

        "build": "npm run build:sass && npm run build:ts",
        "build:ts": "npx esbuild script/Index.ts --external:../../../../../../views/goui/* --bundle --minify --sourcemap --format=esm --target=esnext --outdir=dist",
        "build:sass": "npx sass --style=compressed style:dist"
      }
    }

Now we tell Typescript how to behave by creating the ``tsconfig.json`` file:

.. code:: json

    {
      "extends": "../../../../../../views/goui/tsconfig.module.json",
      "compilerOptions": {
        "baseUrl": ".",
        "outDir": "./dist"
      }
    }

Install all dependencies by running ``npm install``. A new subfolder ``node_modules`` should be created in your root
folder now, as well as a file named ``pacakage-lock.json`` which has all the version information of all the installed
npm packages. This makes sure that your packages on the live environments are the exact same packages that you develop
against.

When developing your module, you need to have npm monitor your code, so that it can compile it into
javascript and css. In order to do this, you run the command ``npm run start``. If there's anything to compile, a new
subdirectory named ``dist`` will be created.tutorial

Anatomy of a GOUI module
------------------------

This section both has some naming conventions / best practices and also details how the actual files are ordered. Each
Typescript file letter should start with a capital and should be CamelCased, e.g. ``ArtistWindow.ts``.

Style overrides should be created in the ``style/style.scss`` or ``style/style.css`` file.

By convention, a Group-Office module has at least the following files:

1. ``Index.ts``: in which the module is registered and routing is handled. It should also check whether the user has the right permissions for the module.
2. ``Main.ts``: This is the main screen for the module. It is commonly divided in one to three columns, a filter panel, a list of entities and entity details.
3. ``EntityTable.ts``: Replace `Entity` with the name of your main entity. This has a table of the entities you wish to list.
4. ``EntityDetail.ts``: Has details on a single entity.
5. ``EntityWindow.ts``: New entities are created or existing entities are edited in separate windows.

Elements of a GUI are named components. Examples of this are comboboxes for entities, but also partial components
that share their layout, but may be based on different fields or even different entites. These shared components should
be their own Typescript class. We'll get into this later.

Index.ts
--------

First, we create an empty ``Main.ts`` file:

.. code:: typescript

    import {
        comp,
        Component
    } from "@intermesh/goui";

    export class Main extends Component {
        constructor() {
            super();
            this.items.add(comp({html: '<h2>Welcome!</h2>'}));
        }
    }

This will prevent any compilation errors when first compiling the typescript code into something readable by the browser.
All it does, is generate and render a ``<div>`` with a ``<h2>`` inside.

Next, create an ``Index.ts`` file and paste the following code into it:

.. code:: typescript

    import {client, modules, router} from "@intermesh/groupoffice-core";
    import {Main} from "./Main.js";
    import {t, translate} from "@intermesh/goui";

    modules.register(  {
    	package: "tutorial",
    	name: "music",
    	entities: [
    	    "Genre",
    	    "Artist"
    	]
    	async init () {
    		client.on("authenticated",  (client, session) => {
    			if(!session.capabilities["go:tutorial:music"]) {
    				// User has no access to this module
    				return;
    			}

    			translate.load(GO.lang.core.core, "core", "core");
    			translate.load(GO.lang.tutorial.music, "tutorial", "music");

    			const mainPanel = new Main();

    			router.add(/^music\/(\d+)$/, (taskId) => {
    				modules.openMainPanel("music");
    			});

    			router.add(/^music$/, () => {
    				modules.openMainPanel("music");
    			});

    			modules.addMainPanel( "tutorial", "music", "music", t("Music"), () => {
    				return mainPanel;
    			});
    		});
    	}
    });

What happens, is actually pretty simple: a module is registered inside the `tutorial` package, named `music`. If
Group-Office authentication is successful and the user is actually allowed to use the `music` module, the following things
happen:

1. Translations are loaded
2. A main panel is defined
3. Routing is added. There are two routes, one for the simple list and one for an individual artist.
4. The main panel is added to the available modules in Group-Office.

Please note that there is no way yet to retrieve individual artists, so the routing is not done yet. That is a nice
cliffhanger.

Main.ts
-------

A common layout is the three panel layout. In the left ("west") panel one renders filters, the center panel has the list
of entities and in the right panel, details are shown for a selected entity.

.. code:: typescript

    export class Main extends Component {
    	private west: Component;
    	private center: Component;
    	private east: Component;

    	constructor() {
    		super("section");

    		this.id = "music";
    		this.cls = "vbox fit";

    		this.west = comp({html: "west");
	    	this.center = comp({html: "center");
		    this.east = comp({html: "east");
		    this.items.add(
                comp({
                    flex: 1, cls: "hbox mobile-cards"
                },

                this.west,

                splitter({
                    stateId: "music-splitter-west",
                    resizeComponentPredicate: this.west
                }),

                this.center,

                splitter({
                    stateId: "music-splitter",
                    resizeComponentPredicate: "table-container"
                }),

                this.east)
            );
        }
    }

The code snippet above will generate a three panel horizontal layout with three content blocks. Each block is separated
by a splitter, which allows the user to resize each block at will. Neat!


Creating a filter panel
-----------------------

Next, we will create the filters in the west panel. This is a vertical box with one or more possible filters and possible
some toolbars as well:

In the ``Main.ts`` file, we will create a function to make such a component:

.. code:: typescript

    private createWest(): Component {
        this.genreTable = new GenreTable();
        this.genreTable.rowSelectionConfig = {
            multiSelect: true,
            listeners: {
                selectionchange: (tableRowSelect) => {
                    const genreIds = tableRowSelect.selected.map((index: number) => tableRowSelect.list.store.get(index)!.id);
                    (this.artistTable.store.queryParams.filter as FilterCondition).genres = genreIds;
                    this.artistTable.store.load();
                }
            }
        }

        return comp({
                cls: "vbox scroll",
                width: 300
            },
            tbar({
                    cls: "border-bottom"
                },
                comp({
                    tagName: "h3",
                    text: t("Genre"),
                    flex: 1
                }),
                '->',
                btn({
                    cls: "for-small-device",
                    title: t("Close"),
                    icon: "close",
                    handler: (button, ev) => {
                        this.activatePanel(this.center);
                    }
                })
            ),
            this.genreTable
        );
    }

Also, create a new file named ``GenreTable.ts`` and type or paste the following code
into it:

..  code:: typescript

    interface Genre extends BaseEntity {
        name: string,
    }

    export class GenreTable extends Table<DataSourceStore> {
        constructor() {
            const store = datasourcestore<JmapDataSource<Genre>, Genre>({
                dataSource: jmapds("Genre"),
                queryParams: {
                    limit: 0,
                    filter: {
                        permissionLevel: 5
                    }
                },
                sort: [{property: "name", isAscending: true}]
            });

            const columns = [
                checkboxselectcolumn(),
                column({
                    header: t("Name"),
                    id: "name",
                    resizable: true,
                    width: 312,
                    sortable: true
                })
            ];

            super(store, columns);

            this.fitParent = true;
            this.rowSelectionConfig = {
                multiSelect: true
            };
        }
    }

First, an interface is defined that outlines the structure as a record as a Typescript class. We need this when defining
a table based on a store record. The actual table is definad as a class that extends the ``Table`` class that uses a
``DataSourceStore`` as a generic. This tells us that we need to use a builtin datasource when defining a table and that's
exactly what happens in the first line of the ``constructor()``.

For this particular table, a store is defined as per our built-in JMAP data source store. As long as an entity is properly
defined in the JMAP ORM, you can use the ``jmapds`` function to retrieve these entities.

The two columns mentioned are a special column type that allows the user to select a column. The use case for this is for
the end user to select and thus filter on multiple genres.

In the west panel, the genre table is connected to the artists table's entity store through an event handler that makes
the actual filter work. It retrieves the ID fields of the genres and passes them as a filter to the artists entity store,
thus magically filtering by the selected genre.

The Main grid
--------------

In the center of the main panel, we create a list of artists. Again, this is rendered as a table. In ``Main.js``, make
sure that the center component renders a proper table:

.. code:: typescript

    constructor() {
		super("section");

		this.id = "music";
		this.cls = "vbox fit";
		this.on("render", async () => {
			try {
				await authManager.requireLogin();
			} catch (e) {
				console.warn(e);
				Notifier.error(t("Login is required on this page"));
			}

			await this.genreTable.store.load();
			await this.artistTable.store.load();
		});


		this.artistTable = new ArtistTable();
		this.artistTable.on("navigate", async (table: ArtistTable, rowIndex: number) => {
			await router.goto("music/" + table.store.get(rowIndex)!.id);
		});

		this.west = this.createWest();
		this.items.add(
			comp({
					flex: 1, cls: "hbox mobile-cards"
				},

				this.west,

				splitter({
					stateId: "music-splitter-west",
					resizeComponentPredicate: this.west
				}),

				this.center = comp({
						cls: 'active vbox',
						itemId: 'table-container',
						flex: 1,
						style: {
							minWidth: "365px", //for the resizer's boundaries
							maxWidth: "850px"
						}
					},

					tbar({},
						btn({
							cls: "for-small-device",
							title: t("Menu"),
							icon: "menu",
							handler: (button, ev) => {
								this.activatePanel(this.west);
							}
						}),

						'->',

						searchbtn({
							listeners: {
								input: (sender, text) => {

									(this.artistTable.store.queryParams.filter as FilterCondition).text = text;
									this.artistTable.store.load();

								}
							}
						}),

						mstbar({table: this.artistTable}),

						btn({
							itemId: "add",
							icon: "add",
							cls: "filled primary",
							handler: async () => {
								const w = new ArtistWindow();
								w.on("close", async () => {
									debugger;
								});
								w.show();

							}
						})
					),

					comp({
							flex: 1,
							stateId: "music",
							cls: "scroll border-top main"
						},
						this.artistTable
					),


					paginator({
						store: this.artistTable.store
					})
				),


				splitter({
					stateId: "music-splitter",
					resizeComponentPredicate: "table-container"
				}),

				this.east = new ArtistDetail()
			)
		);
	}

	private activatePanel(active: Component) {
		this.center.el.classList.remove("active");
		this.east.el.classList.remove("active");
		this.west.el.classList.remove("active");

		active.el.classList.add("active");
	}

	private createWest(): Component {
		this.genreTable = new GenreTable();
		this.genreTable.rowSelectionConfig = {
			multiSelect: true,
			listeners: {
				selectionchange: (tableRowSelect) => {
					const genreIds = tableRowSelect.selected.map((index: number) => tableRowSelect.list.store.get(index)!.id);
					(this.artistTable.store.queryParams.filter as FilterCondition).genres = genreIds;
					this.artistTable.store.load();
				}
			}
		}

		return comp({
				cls: "vbox scroll",
				width: 300
			},
			tbar({
					cls: "border-bottom"
				},
				comp({
					tagName: "h3",
					text: t("Genre"),
					flex: 1
				}),
				'->',
				btn({
					cls: "for-small-device",
					title: t("Close"),
					icon: "close",
					handler: (button, ev) => {
						this.activatePanel(this.center);
					}
				})
			),
			this.genreTable
		);
	}

	async load(id?: EntityID) {
		if(id) {
			void this.east.load(id);
			this.activatePanel(this.east);
		} else {
			this.activatePanel(this.center);
		}
	}

A number of interesting things are created here:

- The artist table is defined an an event handler is attached to it: when clicking a row, a route is being triggered that loads the artist details in the east panel.
- As with the filter panel, the center panel is rendered as a vertical box. In this case, it has a toolbar, the artist grid and a paginator.
- A search button is created that tells the entity store what to do with its input
- The grid is rendered in a scrollable component. The ``flex`` attribute makes sure that this component takes up as much space as possible.
- A paginator is rendered that interacts with the store as defined in the artist table.
- A loader function will load a single entity in the east panel and activate it.

Our next step is to create a table that renders the artist entities! As per our convention, create a new file named ``ArtistTable.ts``
and type or paste the following code into it:

.. code:: typescript

    interface Artist extends BaseEntity {
    	name: string,
    }

    export class ArtistTable extends Table<DataSourceStore> {
    	constructor() {
    		const store = datasourcestore<JmapDataSource<Artist>, Artist>({
    			dataSource: jmapds("Artist"),
    			queryParams: {
    				limit: 0,
    				filter: {
    					permissionLevel: 5
    				}
    			},
    			sort: [{property: "name", isAscending: true}]
    		});

    		const columns = [
    			column({
    				id: "id",
    				hidden: true,
    				sortable: true,
    			}),
    			column({
    				header: t("Photo"),
    				id: "photo",
    				resizable: false,
    				width: 80,
    				renderer: (v, record) => {
    					const c = comp({
    						itemId: "avatar-container"
    					});
    					if (v) {
    						c.items.add(img({
    							cls: "goui-avatar",
    							blobId: v,
    							title: record.name
    						}))
    					}  else {
    						c.items.add(avatar({displayName: record.name}));
    					}
    					return c;
    				}
    			}),
    			column({
    				header: t("Name"),
    				id: "name",
    				resizable: true,
    				sortable: true
    			})
    		];

    		super(store, columns);
    		this.fitParent = true;
    		this.rowSelectionConfig = {
    			multiSelect: true
    		};
    	}
    }

Compared to the earlier genres table, not much has changed. The first visible column has a nice avatar when the user has
uploaded a picture for the artist.

The Detail panel
----------------

Now let's move on to the detail panel. First, the ``Main`` class needs to be amended with a function that loads artist
data:

.. code:: typescript

	async load(id?: EntityID) {
		if(id) {
			void this.east.load(id);
			this.activatePanel(this.east);
		} else {
			this.activatePanel(this.center);
		}
	}

We also directly define the east panel in the constructor:

.. code:: typescript

    this.east = new ArtistDetail()

Time to spin up a detail panel! Create a new Typescript file named ``ArtistDetail.ts``. `

.. code:: typescript

    export class ArtistDetail extends DetailPanel<Artist> {
    	private form: DataSourceForm<Artist>;
    	private avatarContainer: Component;
    	private albumsTable: Table;

    	constructor() {
    		super("Artist");
    		this.width = 500;
    		this.itemId = "detail";
    		this.stateId = "music-detail";

    		this.scroller.items.add(
    			this.form = datasourceform({
    					dataSource: jmapds("Artist")
    				},

    				comp({cls: "card"},
    					tbar({},
    						this.titleCmp = comp({tagName: "h3", flex: 1}),
    					),
    					comp({cls: "hflow", flex: 1},
    						this.avatarContainer = comp({
    							cls: "go-detail-view-avatar pad",
    							itemId: "avatar-container"
    						}),
    					),
    				)
    			),

    			fieldset({legend: t("Albums")},
    				tbar({}, "->", btn({icon: "add", cls: "primary", text: t("Add"), handler:() => {
    					// TODO
    				}})),
    			this.albumsTable = table({
    				fitParent: true,
    				// headers: false,
    				store: store({
    					data: []
    				}),
    				columns: [
    					column({
    						id: "id",
    						hidden: true,
    					}),
    					column({
    						id: "name",
    						header: t("Title"),
    						resizable: true,
    						sortable: true
    					}),
    					datecolumn({
    						id: "releaseDate",
    						header: t("Release date"),
    						sortable: true
    					}),
    					column({
    						resizable: true,
    						id: "genreId",
    						header: t("Genre"),
    						renderer: async (v) => {
    							const g = await jmapds("Genre").single(v);
    							return g!.name;
    						}
    					}),
    					column({
    						resizable: false,
    						// sticky: true,
    						width: 32,
    						id: "btn",
    						renderer: (columnValue: any, record, td, table, rowIndex) => {

    							return btn({
    								icon: "more_vert", menu: menu({}, btn({
    									icon: "edit", text: t("Edit"), handler: async (_btn) => {
    										// TODO...
    									}
    								}), hr(), btn({
    									icon: "delete", text: t("Delete"), handler: async (btn) => {
    										// TODO...
    									}
    								}))
    							})
    						}
    					})
    				]
    			})
    			)
    		);

    		this.addCustomFields();

    		this.toolbar.items.add(
    			btn({
    				icon: "edit",
    				title: t("Edit"),
    				handler: (button, ev) => {
    					const dlg = new ArtistWindow();
    					void dlg.load(this.entity!.id);
    					dlg.show();
    				}
    			}),
    			 btn({
    				icon: "delete",
    				title: t("Delete"),
    				handler: () => {
    					jmapds("Artist").destroy(this.entity!.id).then(() => {
    						router.goto("music");
    					})
    				}
    			})
    		)
    		this.on("load", (pnl, entity) => {
    			this.title = entity.name
    			if (entity!.photo) {
    				pnl.avatarContainer.items.replace(img({
    					cls: "goui-avatar",
    					blobId: entity.photo,
    					title: entity.name
    				}));
    			} else {
    				pnl.avatarContainer.items.replace(avatar({cls: "goui-avatar", displayName: entity.name}));
    			}
    			this.albumsTable.store.loadData(entity.albums, false);
    		})
    	}

What happens here? The detail panel is defined as an extension to the built-in ``DetailPanel`` class  which expects to
load an entity of type ``Artist``. A JMAP data source is defined and in the background, the data is loaded with the
current ID.

Having done that, the panel is rendered with a title (the name of the artist), an avatar if available, and a table of
known albums. Additionally, a number of buttons is added to add, edit or delete albums or even entire artists.

There is still a few loose ends in this panel, but for now we move on to the final part of this tutorial...

The Dialog Windows
------------------

... which would be the dialog window. Let's create a new Typescript file named ``ArtistWindow.ts`` and put the following
code into it:

.. code:: typescript

    export class ArtistWindow extends FormWindow {
    	constructor() {
    		super("Artist");

    		this.title = t("Artist");

    		this.stateId = "artist-dialog";
    		this.maximizable = true;
    		this.resizable = true;
    		this.width = 640;

    		this.form.on("save", (form, data, isNew) => {
    			if (isNew) {
    				router.goto("artist/" + data.id);
    			}
    		})

    		this.generalTab.items.add(
    			fieldset({},
    				textfield({
    					name: "name",
    					label: t("Name"),
    					required: true
    				}),
    				checkbox({
    					name: "active",
    					label: t("Active"),
    					type: "switch"
    				}),
    				textarea({
    					name: "bio",
    					label: t("Biography")
    				})
    			)
    		)
    		this.addCustomFields();
    	}
    }

This is quite a simple form. It extends the built-in ``FormWindow`` class, that is part of the Group-Office core. It
expects the Artist entity store as a parameter. When the form is saved, the artist details are opened in the east panel.
If you defined any custom fields, they are to be rendered below the main form.

Before concluding this tutorial, the last dialog that needs to be built, is the album dialog. There is a challenge here:
since Albums are properties, they cannot be saved separately. Therefore, upon submitting, the full album list is to be
sent to the API, which will update add or delete albums as desired.

First, we update the detail panel to open an album window on clicking the add and edit buttons respectively and load the
artist and album data:

.. code:: typescript

    fieldset({legend: t("Albums")},
            tbar({}, "->", btn({
                icon: "add", cls: "primary", text: t("Add"), handler: () => {
                    const w = new AlbumWindow(this.entity!);
                    w.on("close", async () => {
                        this.load(this.entity!.id)
                    });
                    w.show();
                }
            })),

    /* (...) */
    column({
        resizable: false,
        width: 32,
        id: "btn",
        renderer: (columnValue: any, record, td, table, rowIndex) => {
            return btn({
                icon: "more_vert", menu: menu({}, btn({
                    icon: "edit", text: t("Edit"), handler: async (_btn) => {
                        const dlg = new AlbumWindow(this.entity!);
                        const album = table.store.get(rowIndex)!;
                        dlg.load(album);
                        dlg.show();
                    }
                })
            })
        }
    })

Next, create a new file named ``AlbumWindow.ts`` and copy or type the following code into it:

.. code:: typescript

    export class AlbumWindow extends Window {

    	private entity: Artist;
    	private albumId: EntityID | undefined;
    	private readonly form: Form;
    	constructor(artist: Artist) {
    		super();
    		this.entity = artist;
    		Object.assign(this, {
    				title: t("New album"),
    				width: 800,
    				height: 500,
    				modal: true,
    				resizable: false,
    				maximizable: false
    			}
    		);
    		this.form = form({
    			flex: 1,
    			cls: "vbox",
    			handler: (albumfrm) => {
    				const v = albumfrm.value;
    				v.artistId = this.entity.id;
    				if(this.albumId) {
    					const curr = this.entity.albums.find((a) => a.id === this.albumId);
    					Object.assign(curr!, v);
    				} else {
    					this.entity.albums.push(v as Album);
    				}
    				jmapds("Artist").update(this.entity.id, {albums: this.entity.albums})
    					.then((result) => {console.log(result);this.close();})
    					.catch((e) => Notifier.error(e))
    			}
    			},
    			fieldset({
    					cls: "flow scroll",
    					flex: 1
    				},

    				comp({cls: "vbox gap"},

    					textfield({
    						label: t("Title"),
    						name: "name",
    						required: true,
    					}),

    					datefield({
    						name: "releaseDate",
    						required: true,
    						label: t("Release date"),
    					}),

    					combobox({
    						name: "genreId",
    						label: t("Genre"),
    						required: true,
    						dataSource: jmapds("Genre"),
    					})
    				),

    			),
    			tbar({}, "->", btn({type: "submit", text: t("Save")}))
    		);

    		this.items.add(this.form);
    	}

    	public load(record: any) {
    		this.title = record.name;
    		this.albumId = record.id;
    		this.form.value = record;
    	}
    }

Some notable things about this script:

- We just extend the default goui Window class. We are not editing an entity, but rather one of its properties.
- The form has a combobox with that is based on the genre entity. Not bad for six lines of code.
- In the constructor the entire artist entity is passed. This is needed, since we need to pass all the albums to the API upon saving.
- In the save function, the current album is retrieved by its id if applicable. Otherwise, it is simply appended to the albums array.

One thing that still needs to be done, is the ability to delete an album. You can work the same way as with adding or
an album to an artist: update the full album list for an artist. However, just make sure that the album to be deleted is
not in the list anymore. In the final column of the artist table, we add another button:

.. code:: typescript

    btn({
        icon: "delete",
        text: t("Delete"),
        handler: async (btn) => {
            const a  = this.entity!.albums.filter(album => album.id !== record.id);
            jmapds("Artist").update(this.entity!.id, {albums: a});
        }
    })

Finally, make sure that the albums are listed in chronological order. In the onLoad function of the details, sort the
album list by release date:

.. code:: typescript

    this.on("load", (pnl, entity) => {
        /* (...) */
        entity.albums.sort((a: Album, b: Album) => {
            const ra: string = <string>a.releaseDate, rb: string = <string>b.releaseDate;

            return DateTime.createFromFormat(ra, "Y-m-d")!.compare(DateTime.createFromFormat(rb, "Y-m-d")!);
        });
        this.albumsTable.store.loadData(entity.albums, false);
    });

This concludes the first part of the series. :ref:`The next part <extend_goui_module>` will be dedicated to the Acl
Entity named reviews.