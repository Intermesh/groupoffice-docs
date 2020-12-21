File search
===========

With the file search module you can deep search the contents of files. This 
module in combination with custom fields and the quick edit pane makes the
perfect E-Discovery solution. 

Group-Office can index the following file types:

- Microsoft Office Documents
- Open Document format (Open Office, LibreOffice)
- Saved E-mails including attachments. It does not search an IMAP server.
- PDF
- Plain text
- Scanned images using OCR

Next to the regular search it's also possible to create complex queries with 
the advanced search.

.. figure:: /_static/using/file-search/file-search-module.png
   :width: 100%

   File search module


Indexing
--------

File uploads are not indexed straight away. A schedule task is defined that will 
run every night at 1:00 am. If you want to run it more often you can adjust 
the "Filesearch index" task at Start menu -> Manage system tasks.

If you want to index directly after upload. You can put this in :ref:`config.php <configuration>`::

   $config["filesearch_direct_index"] = true;

.. warning:: This may cause great delays on uploads. We don't recommend using 
   this setting.


.. note:: If indexing is not working you might need to install some 
   additional tools. See :ref:`the installation instructions <install-documents>`.


OCR
```

By default OCR is enabled for TIFF files only. You can enable JPEG, PNG and PDF too with this config option::

    $config['filesearch_ocr_extensions'] = ['tiff', 'tif', 'png', 'jpg', 'jpeg', 'pdf'];

Note that the index process will cause much more load and that OCR results from JPEG files are not that great.

You can also set the language for Tesseract with this option::

    $config['filesearch_language'] = 'nld';

Make sure that language is installed::

    apt install tesseract-ocr-nld
