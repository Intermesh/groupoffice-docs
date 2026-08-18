Manual for GroupOffice
======================

This is the source repository for the manual:

https://groupoffice.readthedocs.io/

Building these docs with Docker
-------------------------------

This image automatically builds the documentation and serves them on port 8004.
The docs will be built and rebuilt after making changes. You can view them in your
browser at:

http://localhost:8004/

Run:

```
docker-compose up -d
```

Building without docker
----------------------

sudo apt install python3-full
python3 -m venv venv

source venv/bin/activate
pip install -r requirements.txt
sphinx-build -b html . _build/html

