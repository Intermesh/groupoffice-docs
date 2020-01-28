Building these docs with Docker
===============================

I used this image:

https://github.com/keimlink/docker-sphinx-doc

Pull it::

    docker pull keimlink/sphinx-doc

Build out autobuild image::

    docker build -t sphinx-autobuild sphinx-autobuild

Then run it::

    docker run -it -p 8000:8000 --rm -v "$(pwd)/../":/home/python/docs sphinx-autobuild
    
The docs will be built and rebuilt after making changes. You can view them in your browser at:

http://localhost:8000/