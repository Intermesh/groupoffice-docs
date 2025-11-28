Manual upgrade from the Tarball
-------------------------------

.. note:: In version 6.8 we've switched from Ioncube to `SourceGuardian <https://www.sourceguardian.com/loaders.html>`_.
    Please make sure that's installed if you're using the professional version.

We strongly recommend that you use our Debian packages or Docker instead of the
tarball. But if you really want use it then follow these steps:

1. Grab the version to install from https://github.com/Intermesh/groupoffice/releases
   Remember to upgrade to each 6.x major release step by step. Grab older releases from: https://sourceforge.net/projects/group-office/files/
2. Make sure your system meets the :ref:`system-requirements`.
3. Make sure you're on the latest minor release of your current version (For example 6.2.112 or 6.3.76).
4. When running 6.2 make sure you've installed the "customfields" and "search" modules as they 
   will become part of the Group-Office core.
5. Make sure to install the latest license key from your group-office.com account in the
   contracts section (https://www.group-office.com/account#account/contracts) if you run
   the professional version. This can be done via the browser GUI in the main menu -> register or via CLI::

      sudo -u www-data php ./cli.php core/System/setLicense --key=<YOURKEY>

6. If you are coming from version 5.0 or lower. Then you must install the projects2 module in 6.2 to migrate your existing data. This can't be done in a later version!
7. Move away your old source files to a backup location.
   
   .. warning:: Do not copy the new files over the existing. This will result in a broken system.
      
8. Put the new files at the right location.
9. If exists copy your old :ref:`config.php <configuration>` and license file to the new
   files. It is good practice to keep these files one directory higher then the 
   Group-Office source so you have a complete clean code base.
10. If you have any :ref:`studio-generated <studio>` modules, copy these into the ``go/modules`` folder. Please note that if you don't, the studio-generated modules will be entirely disabled.
11. Visit http://yourdomain/install/ and follow instructions.
12. Check if you have the right cron job in place::

      * * * * * www-data php <YOURDOCUMENTROOT>/cron.php

.. note:: If you're upgrading from 6.2 to 6.3 or higher and you are running the CGI version of PHP then you need to add a rewrite rule to add the "Authorization" header. Read more at :ref:`cgi-authorization`.

Registering a license
`````````````````````

When upgrading from 6.4 to 6.5, you may run into a licensing issue.

Since 6.5, it is possible to install or reinstall a license from within Group Office itself, so you do not need to
download the license file anymore. Make sure that you are logged as an administrator, click on the menu and select
'Register'.

.. figure:: /_static/upgrade/registration.png

   Registration screen

Click the 'Get license now' button, log in to the Group Office website, find your license key and paste it in the text box.

Update script
`````````````

I've written a simple bash script that downloads the latest PHP 7.1+ version of Group-Office and replaces all code in the
given directory.

You can run it like this::

    ./update_groupoffice.sh <DIR_OF GROUPOFFICE>

That will automatically download the latest version. If you're on an older major release you will have to supply the version manually::

   ./update_groupoffice.sh <DIR_OF GROUPOFFICE> <VERSION>


.. warning:: Please backup before using!

.. code::

    #!/bin/bash
    set -e

    if [ -z "$1" ]
      then
        echo "Please supply the target directory"
        exit 1;
    fi

    TARGET=$1

    if [ ! -d "$TARGET" ]; then
        echo "$TARGET doesn't exist!"
        exit 1;
    fi

    if [ ! -f "$TARGET/version.php" ]; then

        echo "$TARGET is not a Group-Office directory!"
        exit 1
    fi

    get_latest_release() {
      curl --silent "https://api.github.com/repos/intermesh/groupoffice/releases/latest" | # Get latest release from GitHub api
        grep '"tag_name":' |                                            # Get tag line
        sed -E 's/.*"v([^"]+)".*/\1/'                                    # Pluck JSON value
    }

    if [ -z "$2" ]
      then
        VERSION=`get_latest_release`
    else
        VERSION=$2;
    fi

    read -r -p "Are you sure you want to update directory '$TARGET' to Group-Office version '$VERSION'? [y/N]" response;
    if [[ "$response" != "y"  ]]; then
        exit 0
    fi

    rm -rf goupdate
    mkdir -p goupdate
    cd goupdate

    wget https://github.com/Intermesh/groupoffice/releases/download/v$VERSION/groupoffice-$VERSION.tar.gz
    tar zxf groupoffice-$VERSION.tar.gz

    GO=`ls -d */ | grep groupoffice`
    echo "Source dir: $GO"

    cd $GO

    for f in *; do
        rm -rf ../../$TARGET/$f
        cp -a $f ../../$TARGET
    done

    cd ../../





