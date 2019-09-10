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
