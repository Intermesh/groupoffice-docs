Building a webclient module, part 2
===================================

.. warning:: This tutorial is deprecated. As we move away from ExtJS, we would advise you to use :ref:`GOUI <goui_module>` instead.

In which we build access control into the web client.

In :ref:`the server module tutorial <building-a-server-module>` we built one ``AclOwnerEntity`` model, being Review. The web
client was created in :ref:`the webclient tutorial <building-a-webclient-module>`, without the review part. This part of
the webclient tutorial covers the client-side part of working with access control lists.

For the sake of this tutorial, we made it possible for reviews to be shared with your fellow users, or being
hidden since nobody needs to know about your guilty pleasures. :-)

We will be creating a modal in which to add or edit reviews. Furthermore, there will be a window, in which
shared reviews are displayed. In order to be a bit flashy, we borrow some code from the comments module
and display the reviews in a somewhat playful manner.


Add the Review model to the store
---------------------------------

The first step is to make sure that reviews can be retrieved and managed through the store. In ``Module.js`` we add
a new entity named `Review`::

    entities: [
        // Rest of the entities
        {
            name: "Review",
            relations: {
                creator: {store: "User", fk:"createdBy"},
                modifier: {store: "User", fk: "modifiedBy"}
            }
        }
    ],

Please note that a useful relation would be the album relation. After all, a review is connected to one album.
Since we defined album as a `property` of artist, you will not be able to retrieve this relation from the store.

Artist Detail Panel
-------------------

Both modals should be called from the ``ArtistDetail.js`` file (which renders the artist detail panel) and there
should be a way to distinguish between albums with or without reviews.

In order to achieve this, we update the ``InitComponent`` like this:

.. code-block:: javascript

	initComponent: function () {
		this.tbar = this.initToolbar();
		// Render a 'new review' modal
		this.addReviewModal = function (v) {
			var dlg = new go.modules.tutorial.music.ReviewDialog();
			dlg.setValues({albumId:v.id});
			dlg.show();
		};
		// Render all reviews for the current album in a window (which is offered as a modal)
		this.showReviewsModal = function(v) {
			var dlg  = new go.modules.tutorial.music.ReviewsModal();
			dlg.store.setFilter('albumId', {albumId: v.id});
			dlg.store.load();
			dlg.show();
		};
		Ext.apply(this, {
			// all items are updated automatically if they have a "tpl" (Ext.XTemplate) property or an "onLoad" function. The panel is passed as argument.
			items: [
				//Artist name component
				{
					cls: 'content',
					xtype: 'box',
					tpl: '<h3>{name}</h3>'
				},
				//Render the avatar
				{
					xtype: "box",
					cls: "content",
					tpl: new Ext.XTemplate('<div class="go-detail-view-avatar">\
						<div class="avatar" style="{[this.getStyle(values.photo)]}"></div></div>',
						{
							getStyle: function (photoBlobId) {
								return photoBlobId ? 'background-image: url(' + go.Jmap.downloadUrl(photoBlobId) + ')"' : "";
							}
						})
				},
				// Albums component, render number of reviews
				{
					collapsible: true,
					title: t("Albums"),
					xtype: "panel",
					listeners: {
						scope: this,
						afterrender: function(box) {
							box.getEl().on('click', function(e){
								//don't execute when user selects text
								if(window.getSelection().toString().length > 0) {
									return;
								}
								var container = box.getEl().dom.childNodes[1],
									item = e.getTarget("a", box.getEl()),
									i = Array.prototype.indexOf.call(container.getElementsByTagName("a"), item);
								if(i >=0) {
									var album = go.util.Object.convertMapToArray(this.data.albums,'id')[i];
									if(album.reviews.length > 0) {
										this.showReviewsModal(album);
									} else {
										this.addReviewModal(album);
									}
								}
							}, this);
						}
					},
					tpl: new Ext.XTemplate('<div class="icons">\
                          <tpl for="go.util.Object.values(values.albums)">\
                          <p class="s6"><tpl if="xindex == 1"><i class="icon label">album</i></tpl>\
                          <span>{name}</span>\
                          <label>{[go.util.Format.date(values.releaseDate)]} - <tpl for="genre"> {name} </tpl> {[this.displayNumReviews(values.reviews)]}</label>\
                          </p>\
                          </tpl>\
                          </div>',
						{
							displayNumReviews: function(v){
								v = v || null;
								if(v === null) {
									return "";
								} else if(v.length == 0) {
									return "- <a class='normal-link'>" + t("Write a Review")+ "</a>";
								} else {
									return "- <a class='normal-link'>" +v.length+" " + t("Reviews")+ "</a>"
								}
							}
						})
				}
			]
		});
		go.modules.tutorial.music.ArtistDetail.superclass.initComponent.call(this);
		this.addCustomFields();
	},

Study the code. The following things were added:

1. A link was added to the album overview items. Dependent on the number of known reviews, the link text is altered
2. If there are no reviews, a Review modal will be opened in which you can add a new review
3. Otherwise, a window is opened which displays current reviews.

.. figure:: /_static/developer/building-a-webclient-module-part-2/artist-panel.png
   :width: 400px

Review modal
------------

The next step is adding a modal, in which to enter a review. Please note that an ``albumId`` is supplied from the
``addReviewModal`` method::

    dlg.setValues({albumId:v.id});

Create a new javascript file, name it ``ReviewDialog.js`` and enter the following code:

.. code-block:: javascript

    go.modules.tutorial.music.ReviewDialog = Ext.extend(go.form.Dialog, {
        stateId: 'album-review',
        title: t("Review"),
        entityStore: "Review",
        width: dp(800),
        height: dp(600),
        maximizable: false,
        collapsible: false,
        modal: true,

        initFormItems: function () {

            this.addPanel(new go.permissions.SharePanel());

            var items = [{
                xtype: 'fieldset',
                anchor: "100% 100%",
                items: [{
                        xtype: 'textfield',
                        name: 'title',
                        fieldLabel: t("Title"),
                        anchor: '100%',
                        allowBlank: false
                    },
                    {
                        xtype: 'radiogroup',
                        fieldLabel: t("Rating"),
                        name: "rating",
                        value: null,
                        items: [
                            {boxLabel: t("It stinks"), inputValue: 1},
                            {boxLabel: t("Meh"), inputValue: 2},
                            {boxLabel: t("It's OK"), inputValue: 3},
                            {boxLabel: t("It's pretty good"), inputValue: 4},
                            {boxLabel: t("A stroke of genius"), inputValue: 5}
                        ]
                    },
                    {
                        xtype: 'xhtmleditor',
                        name: 'body',
                        fieldLabel: "",
                        hideLabel: true,
                        anchor: '0 -90',
                        allowBlank: false,
                        listeners: {
                            scope: this,
                            ctrlenter: function() {
                                this.submit();
                            }
                        }
                    }]
            }
            ];

            return items;
        },

        onLoad : function(entityValues) {
            this.supr().onLoad.call(this, entityValues);
        }
    });

...and add the line::

    ReviewDialog.js

to the bottom of your ``scripts.txt`` file.

The code is pretty straightforward, but please note a few things:

* The ``albumId`` field does not need to be defined, since the ``albumId`` value is already passed from the ``artistDetail`` panel;
* Permission management is added by the following line::

    this.addPanel(new go.permissions.SharePanel());

That's it. We can now add our own review to the selected album:


.. figure:: /_static/developer/building-a-webclient-module-part-2/review-modal-1.png
   :width: 800px

.. figure:: /_static/developer/building-a-webclient-module-part-2/review-modal-2.png
   :width: 800px

Reviews screen
--------------

In the reviews screen, a number of things need to be checked:

1. A user may enter only one review for a certain album.
2. It must be possible to read, edit or delete other reviews, depending on the ACL settings entered by the creator.
3. Upon adding or deleting a review, the Artist store is to be reloaded. Please note that we have already implemented in the Review model.

A new javascript file is to be created and added to the ``scripts.txt`` file. We name it ``ReviewsModal.js``.

.. code-block:: javascript

    go.modules.tutorial.music.ReviewsModal = Ext.extend(go.Window, {
        stateId: 'album-reviews',
        title: t("Reviews"),
        width: dp(1000),
        height: dp(800),
        maximizable: true,
        collapsible: false,
        modal: true,
        stateful: true,
        layout: 'fit',
        initComponent: function () {
            this.tools = [{
                id: "add",
                handler: function () {
                    var dlg = new go.modules.tutorial.music.ReviewDialog();
                    dlg.setValues({albumId: this.albumid});
                    dlg.show();
                }
            }];

            this.store = new go.data.Store({
                fields: [
                    'id',
                    'title',
                    'body',
                    'rating',
                    'albumTitle',
                    'createdBy',
                    {name: 'creator', type: "relation"},
                    'albumId', 'aclId', "permissionLevel"
                ],
                entityStore: "Review"
            });

            // Use a Group Office store that is connected with an go.data.EntityStore for automatic updates.
            this.store.on('load', function (store, records, options) {
                this.updateView();
                this.updateTitle();
                this.toggleAddBtn();
            }, this);

            this.store.on('remove', function () {
                this.updateView();
                this.toggleAddBtn();
            }, this);

            this.on('destroy', function () {
                this.store.destroy();
            }, this);

            this.on("expand", function () {
                this.updateView();
            }, this);

            // Add a simple context menu. Make sure that the correct permissions are set
            this.contextMenu = new Ext.menu.Menu({
                items: [{
                    iconCls: 'ic-delete',
                    text: t("Delete"),
                    handler: function () {

                        Ext.MessageBox.confirm(t("Confirm delete"), t("Are you sure you want to delete this item?"), function (btn) {
                            if (btn !== "yes") {
                                return;
                            }
                            go.Db.store("Review").set({destroy: [this.contextMenu.record.id]});
                        }, this);

                    },
                    scope: this
                }, {
                    iconCls: 'ic-edit',
                    text: t("Edit"),
                    handler: function () {
                        var dlg = new go.modules.tutorial.music.ReviewDialog();
                        dlg.load(this.contextMenu.record.id).show();
                    },
                    scope: this
                }]
            });

            var cntrClass = Ext.extend(Ext.Container, {
                initComponent: function () {
                    Ext.Container.superclass.initComponent.call(this);
                    Ext.applyIf(this, go.panels.ScrollLoader);
                    this.initScrollLoader();
                },
                store: this.store,
                scrollUp: true
            });

            this.items = [
                this.commentsContainer = new cntrClass({
                    region: 'center',
                    autoScroll: true
                })
            ];

            go.modules.tutorial.music.ReviewsModal.superclass.initComponent.call(this);
        },

        updateView: function () {
            this.commentsContainer.removeAll();
            this.store.each(function (r) {
                var mineCls = r.get("createdBy") == go.User.id ? 'mine' : '';
                var readMore = new go.detail.ReadMore({
                    cls: mineCls
                });
                var creator = r.get("creator");
                if (!creator) {
                    creator = {
                        displayName: t("Unknown user")
                    };
                }
                var avatar = {
                    xtype: 'box',
                    autoEl: {
                        tag: 'span', 'ext:qtip': t('{author} wrote: ')
                            .replace('{author}', creator.displayName)
                    },
                    cls: 'photo ' + mineCls
                };
                if (creator.avatarId) {
                    avatar.style = 'background-image: url(' + go.Jmap.thumbUrl(creator.avatarId, {
                        w: 40,
                        h: 40,
                        zc: 1
                    }) + ');background-color: transparent;';
                } else {
                    avatar.html = go.util.initials(creator.displayName);
                    avatar.style = 'background-image: none';
                }
                readMore.setText(this.getReviewText(r));

                this.commentsContainer.add({
                    xtype: "container",
                    cls: 'go-messages',
                    items: [{
                        xtype: 'container',
                        label: t("Creator"),
                        items: [avatar, readMore]
                    }]
                });
                // Add a context menu, make permissions dependent on ACL
                readMore.on('render', function (me) {
                    me.getEl().on("contextmenu", function (e, target, obj) {
                        e.stopEvent();

                        if (r.data.permissionLevel >= go.permissionLevels.write) {
                            this.contextMenu.record = r;
                            this.contextMenu.showAt(e.xy);
                        }

                    }, this);
                }, this);
            }, this);

            this.doLayout();
            var height = 7; // padding on composer
            this.commentsContainer.items.each(function (item, i) {
                height += item.getOuterSize().height;
            });
        },

        // Update window title by adding the album title
        updateTitle: function () {
            var r = this.store.getAt(0), title = this.title;
            if (typeof (r) !== "undefined") {
                this.setTitle(t("Reviews")+"&nbsp;" + t('for') + "&nbsp;" +
                    Ext.util.Format.htmlEncode(r.get('albumTitle')));
            } else {
                this.setTitle(t("Reviews"));
            }
        },

        // Check whether current user had added a review. If they have, hide the add button.
        toggleAddBtn: function () {
            if (this.store.query('createdBy', go.User.id).getCount() > 0) {
                this.tools.add.hide();
            } else {
                var r = this.store.getAt(0);
                if (typeof (r) !== "undefined") {
                    this.tools.add.albumid = r.get("albumId");
                }
            }
        },

        // Render the review text in a nice fashion
        getReviewText: function (r) {
            var s = "<h4>" + r.get("title") + " </h4><div style='font-size=12px;'>";
            for (var ii = 1; ii <= 5; ii++) {
                s += "<i class='icon'>star" + (r.get('rating') < ii ? "_border" : "") + "</i>";
            }
            s += "</div><p class='s6'>" + Ext.util.Format.htmlDecode(r.get('body')) + "</p>";
            return s;
        }
    });


In this file, a number of things happen:

1. The modal is based on the (relatively empty) ``go.Window`` class. A number of sane default settings is preconfigured.
2. In the initComponent function, a new store is defined. Please note that the ``aclId`` and ``permissionLevel`` fields are being retrieved. We will need these later.
3. A context menu is added.
4. Each review is being rendered in a container class. We borrowed the layout from the 'comments' module to make it look nice
5. For each review, the permission level is matched with the user's permissions. If applicable, the user can use the context menu.


.. figure:: /_static/developer/building-a-webclient-module-part-2/reviews.png
   :width: 400px

The End
-------

This concludes our webclient tutorial. There is one thing left to say: have fun coding your own GroupOffice modules!