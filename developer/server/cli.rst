.. _cli:

Command Line Interface
======================

Group Office also has a Command Line Interface. To implement this do the following:

1. Create a controller that extends the abstract CLI controller in your module:

   .. code:: php

      <?php

      namespace go\modules\community\music\controller;

      use go\core\cli\Controller;

      class CliDemo extends Controller {
        public function hello($name = "World") {
          echo "Hello $name!\n";
        }
      }


2. Run::

      docker-compose exec --user www-data groupoffice php /usr/local/share/groupoffice/cli.php community/music/clidemo/hello --name=Merijn


3. This should output::

      Hello Merijn!


.. note:: Command line methods always run as the administrator user.