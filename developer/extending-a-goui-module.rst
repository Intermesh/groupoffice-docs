.. _extend_goui_module:

Extending a GOUI webclient module
=================================

In which we build access control into the web client.

In :ref:`the server module tutorial <server_module>` we built one ``AclOwnerEntity`` model, being Review. The web
client was created in :ref:`the webclient tutorial <goui_module>`, without the review part. This part of
the webclient tutorial covers the client-side part of working with access control lists.

For the sake of this tutorial, we made it possible for reviews to be shared with your fellow users, or being
hidden since nobody needs to know about your guilty pleasures. :-)

We will be creating a modal in which to add or edit reviews. Furthermore, there will be a window, in which
shared reviews are displayed. In order to be a bit flashy, we display the reviews in a somewhat playful manner.

Some specifications
-------------------

Reviews are coupled to individual albums. Therefore, it makes sense to manage them on the level of the album. We already
have a number of possible actions for albums hidden behind the meatball menu at the end of each row. We need to add
a button to add a review. It would also be nice to see existing reviews for the selected album.

It would also make sense to disable (or entirely hide) the buttons if (a) the user already added their review and (b)
when there are no reviews yet. That is, if there are no reviews, it is not needed to display them. Therefore, we hide
the 'Show reviews' button.

Add a new entity
----------------

In the ``entities`` array of the register function, add a new entity named 'Review'. Also, make sure that there is a
model named ``Review`` in the models subdirectory:

.. code:: php

    <?php
    final class Review extends AclOwnerEntity
    {
    	/** @var int */
    	public int $id;
    	/** @var int */
    	public $aclId;
    	/** @var int */
    	public int $createdBy;
    	/** @var int */
    	public int $albumId;
    	/** @var int */
    	public int $modifiedBy;
    	/** @var int */
    	public int $rating;
    	/** @var string */
    	public string $title;
    	/** @var string */
    	public string  $body;
    	/** @var string */
    	public string $albumtitle;

    	protected static function defineMapping(): Mapping
    	{
    		return parent::defineMapping()
    			->addTable('tutorial_music_review')
    			->addQuery((new Query())->select('a.name AS albumtitle')
    				->join('tutorial_music_album', 'a', 'a.id=tutorial_music_review.albumId'));
    	}




In the ``ArtistDetail`` class, add two buttons to the menu at the end of each album row:

.. code:: typescript


        btn({
            icon: "reviews",
            text: t("Show reviews"),
            hidden: !record.reviews.length,
            handler: (btn) => {
                const w = new ReviewsWindow(record);
                w.show();
            }
        }),
        btn({
            icon: "rate_review",
            text: hasReviewed ? t ("Update review"): t("Write review"),
            handler: (_btn) => {
                const w = new ReviewWindow(record);
                if(hasReviewed) {
                    w.load(reviewId);
                }
                w.show();
            }
        }),

In the same renderer function, we also need to make sure that the system knows which reviews are written by the current
user. A quick hack (but inefficient implementation) would be to check all reviews for the album and see whether the
creator is the current user.

.. code:: typescript

    const user = await client.getUser();
    let hasReviewed = false, reviewId = undefined;
    for(const currId of record.reviews) {
        const curr = await jmapds("Review").single(currId);
        if (curr!.createdBy == user!.id) {
            hasReviewed = true;
            reviewId = curr!.id;
            break;
        }
    }

Add or Edit a Review
--------------------

Now we create a new file named ``ReviewWindow``. As we edit an entity, we can use the built-in ``FormWindow``. We make
sure to pass the data of the current album to the window, as we can dynamically create a title and pass the albumId in
the form.

.. code:: typescript

    export class ReviewWindow extends FormWindow {

    	private readonly data: Album;
    	constructor(data: Album) {
    		super("Review");
    		this.data = data;
    		this.title = t("Review") + ": " + data.name;

    		this.stateId = "add-review-dialog";
    		this.maximizable = true;
    		this.resizable = true;
    		this.modal = true;
    		this.width = 640;

    		this.form.on("save", (form, data, isNew) => {
    			router.goto("artist/" + this.data.artistId);
    		});

    		this.generalTab.items.add(
    			fieldset({},
    				textfield({
    					name: "title",
    					label: t("Title"),
    					required: true
    				}),
    				numberfield({
    					hidden: true,
    					value: parseInt(this.data.id),
    					required: true,
    					name: "albumId"
    				}),
    				select({
    					label: t("Rating"),
    					name: "rating",
    					required: true,
    					options: [
    						{
    							value: 1,
    							name: t("1 star")
    						},
    						{
    							value: 2,
    							name: t("2 stars")
    						},
    						{
    							value: 3,
    							name: t("3 stars")
    						},
    						{
    							value: 4,
    							name: t("4 stars")
    						},
    						{
    							value: 5,
    							name: t("5 stars")
    						},

    					]
    				}),
    				textarea({
    					required: true,
    					name: "body",
    					label: t("Your review")
    				})
    			)
    		)

    		this.addSharePanel();
    	}
    }

The line ``this.addSharePanel();`` makes sure that the ``AclOwnerEntity`` can actually be shared among users. When
opening the review window, an extra tab is displayed that allows you to configure which users and groups have access
to your record.

Display all reviews
-------------------

Now that one can add, edit or share a review, all that remains, is to list them. As long as a user has access to the
music module, all reviews for the currently selected album are retrieved as long as the user has access to them. All
we need to do, is open a new window in which reviews are opened. Create a new file named `ReviewsWindow` and type or
paste the following code:

.. code:: typescript

    export class ReviewsWindow extends Window {

    	constructor(data: Album) {
    		super();
    		this.title = `${t("Reviews")} ${t("for")}: ${data.name}`;

    		this.stateId = "reviews-dialog";
    		this.maximizable = true;
    		this.resizable = true;
    		this.modal = true;
    		this.width = 640;
    		this.height = 768;
    		this.cls = "vbox gap";

    		const scrollCmp = comp({cls: "scroll", flex: 1});

    		jmapds("Review").get(data.reviews).then(async (result) => {
    			for (const review of result.list) {
    				const user = await jmapds("User").single(review!.createdBy);
    				const avatarCnt = comp({
    						cls: "go-detail-view-avatar pad",
    						itemId: "avatar-container"
    					});
    				if(user!.avatarId) {
    					avatarCnt.items.replace(
    						img({
    							cls: "goui-avatar",
    							blobId: user!.avatarId,
    							title: user!.displayName
    						})
    					);
    				} else {
    					avatarCnt.items.replace(avatar({cls: "goui-avatar", displayName: user!.name}));
    				}

    				scrollCmp.items.add(comp({cls: "card pad"},
    					comp({cls: "hbox",},avatarCnt,
    						comp({cls: "vbox"},
    							h3(review!.title),
    							h4(t("By")+ " " +user!.displayName),
    						)),
    					this.addRating(review.rating),
    					comp({cls: "border-bottom", html: review!.body})
    				));
    			}
    		}).finally(() => {
    			this.items.add(scrollCmp, tbar({}, "->", btn({
    				icon: "close",
    				text: t("Close"),
    				handler: () => this.close()
    			})))
    		});

    	}

    	private addRating(rating: 1 | 2 | 3 | 4 | 5): Component {
    		const cmp = comp({cls: "hbox"});
    		for (let r = 1; r <= rating; r++) {
    			cmp.items.add(comp({cls: "icon", tagName: "i", text: "star"}))
    		}
    		return cmp;
    	}
    }

The code is pretty simple. In the constructor, the album data is already passed. We know the ideas of the reviews,
so we retrieve them from the data store. As the data store knows who has access, we do not have to bother with that.
When these are loaded, a new card is rendered for each review. Having done that, a bottom toolbar is rendered with a
button to close the reviews. In order to create some eye-candy, the ratings are displayed with stars (one is bad, five
is good). Finally, the user is displayed with their avatar (if available).

Conclusion
----------

That's it. You have just created a Group-Office module in our lightweight GOUI framework. You have been taught the
concepts of Entities and Properties, you learnt how to make certain entities shareable and you have learnt how to create
a fancy frontend with relatively little code.