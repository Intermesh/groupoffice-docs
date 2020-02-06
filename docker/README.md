Building these docs with Docker
===============================

This image automatically builds the documentation and serves them on port 8000.
The docs will be built and rebuilt after making changes. You can view them in your
browser at:

http://localhost:8000/

Docker compose
--------------
The easiest way is to start this docker with::

    docker-compose up -d

Manual
------

You can also do it without docker-compose:

Pull the image for sphinx-doc::

    docker pull keimlink/sphinx-doc

Build the autobuild image::

    docker build -t sphinx-autobuild sphinx-autobuild

Then run it::

    docker run -it -p 8000:8000 --rm -v "$(pwd)/../":/home/python/docs sphinx-autobuild
    
