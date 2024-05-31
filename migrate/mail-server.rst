Migrate email server
====================

Move your IMAP accounts to a new email server
---------------------------------------------

To move your email to a new mail server you'll need to install the new server with all the existing accounts and copy the mailboxes.

Since this task is often at hand we had to find an efficient way to do this quickly so we wrote a script that would:

1. Create all the existing mailboxes on the new server.
2. Sync all the mail from the old server to the new one.
3. Create Users that have access to the mailboxes.

For this you will need:

- Group Office
- `ImapSync <https://github.com/imapsync/imapsync>`_
- The script at the bottom of this article


ImapSync may need some dependency packages, you will find the install instructions for your OS here:
https://imapsync.lamiral.info/#install

Setup your new mail server with Group Office
--------------------------------------------

The new email server needs to be installed first.
We have created a package for Debian/Ubuntu that would install and configure a Postfix + Dovecot mail server (almost) automatically

See our documentation page for a link to these deb packages that would install and configure Group Office, Postfix (MTA/SMTP) and Dovecot (MDA/IMAP)
:ref:`mailserver`

When Group Office and the Mail server are installed open it in the browser and install the Postfixadmin module by going to
**Main menu (top right corner) -> System settings -> Modules -> Install** than choice **Postfix Admin**. This module lets you configure mailboxes.
But don't create them yet. This will be done automatically in the next step.

Create mailboxes on the new server
----------------------------------

First you'll need to create a list of the existing mailboxes on the current mail server you want to migrate.
You'll need to following details:

- Email
- Password
- Display name

The above information will be used to create mailboxes on the new server (with the same username and password)
and then fetch the mail from the old server. If you don't know the password you'll have to change it because
you won't be able to read the mailboxes without it.

Put the mailbox information into a mailboxes.csv file like this.

.. code:: csv

    michael@group-office.com,S3cRetPassWD,Michael de Hart
    merijn@group-office.com,S3cRetPassWD,Merijn Schering
    wesley@group-office.com,S3cRetPassWD,Joachim van de Hatert



Running the mailbox migration script
------------------------------------

After creating the CSV file that contains the information for the mailboxes,
the script at the **bottom** of this article will do the rest of the work.

Run it on the command line (not in the browser)

.. code:: bash

    $ php syncmail.php

The script will need to know the path to your mailboxes.csv file. It is in the same directory press enter.
Otherwise enter the path to this file first. It the file is found it will show you a list of mailboxes
it is going to migrate and asks you the following question:

.. code:: bash

    Do you want to create to following mailboxes? [y/N]:

Type ``y`` and press enter

This won't take long and the following question will be asked:

.. code:: bash

    Fill mailboxes from another imap host? [y/N]:

Before you continue, confirm the mailboxes are created on your new mail server by logging in to Group Office and open the Postfix admin module you've installed in Step 1

Type ``y`` and press enter

ImapSync will need to know the target and source server address to fetch from and copy to. You'll be prompted for this information:

.. code:: bash

    Enter IMAP host to fetch from: mail.oldserver.com
    Port number [143]:
    Enter IMAP host to copy to: [localhost]:
    Port number [143]:

When ImapSync is installed correctly the script will start syncing all the created mailboxes (this could take a while)

Creating Group Office user accounts for each mailbox (optional)
---------------------------------------------------------------

The last part the script takes care of is creating Group Office users that may access these mailboxes. If this is already setup our you would rather do this manually just hit 'n'

.. code:: bash

    Do you want to add users with these mail accounts in this Group Office installation [y/N]:

When entering ``y`` the script will create Group Office users accounts. The username will be what is before the @ of the mailbox and the password will be the same.

.. code:: php

    <?php
    /*
     * The MIT License (MIT)
     *
     * Copyright (c) 2014 Intermesh BV
     *
     * Permission is hereby granted, free of charge, to any person obtaining a copy
     * of this software and associated documentation files (the "Software"), to deal
     * in the Software without restriction, including without limitation the rights
     * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
     * copies of the Software, and to permit persons to whom the Software is
     * furnished to do so, subject to the following conditions:
     *
     * The above copyright notice and this permission notice shall be included in
     * all copies or substantial portions of the Software.
     *
     * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
     * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
     * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
     * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
     * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
     * THE SOFTWARE.
     */

    /**
     * Script askes the following questions:
     *
     * - Do you want to create to following mailboxes? [y/N]:
     * - Fill mailboxes from another imap host? [y/N]:
     * - Do you want to add users with these mailaccounts in this GroupOffice installation [y/N]:
     *
     * RUN ON CLI AS ROOT !!
     * YOU MOST LIKELY WANT TO CHANGE THE PATH TO GO AND CONFIG.PHP
     *
     * CSV should look like this:
     * email,password,firstname,middlename,lastname\n
     *
     * @author Michael de Hart
     * @copyright Copyright Intermesh BV.
     */

    define('NOLOG', true); // stop groupoffice from logging.

    $handle = fopen("php://stdin", "r");

    $conf_path = '/etc/groupoffice/config.php';
    $path = '/usr/share/groupoffice/';

    while (!is_file($path . 'GO.php')) {
        echo "Could not find GO.php in '$path'\n"
            . "Enter the path to your Group-Office installation to continue: ";
        $path = trim(fgets($handle));
        $conf_path = $path . 'config.php';
    }
    define('GO_CONFIG_FILE', $conf_path);
    require_once($path . 'GO.php');


    use go\core\model\User;
    use GO\Email\Model\Account;
    use GO\Postfixadmin\Model\Domain;
    use GO\Postfixadmin\Model\Mailbox;

    GO::session()->runAsRoot();

    $syncer = new ImapSync();
    $syncer->start();

    class ImapSync
    {

        protected $imap_sync = '/usr/bin/imapsync'; //binary
        protected $domain = 'mydomain.com';
        protected $quota = 512 * 1024; //quota in kb = (512MB)

        protected $source = [
            'host' => '',
            'port' => '143',
        ];
        protected $target = [
            'host' => 'localhost',
            'port' => '143',
            'smtp_host' => 'localhost',
            'smtp_port' => '25',
        ];
        // CSV Config
        protected $csv = [
            'path' => 'mailboxes.csv',
            'delimiter' => ",",
            'enclosure' => '"'
        ];
        // Column configuration for Mailbox CSV file
        protected $col = [
            'email' => 0,
            'password' => 1,
            'displayName' => 2,
        ];

        protected $log_file = 'imapsync';
        private $records = [];

        public function start()
        {

            try {
                $handle = fopen("php://stdin", "r");

                echo "This script will create mailboxes and users based on a CSV file?\n"
                    . "Enter the path to the CSV file to continue: [" . $this->csv['path'] . "]: ";
                $line = trim(fgets($handle));
                if (!empty($line)) {
                    $this->csv['path'] = $line;
                }
                $this->records = $this->loadCsv();

                if (GO::modules()->isInstalled('postfixadmin')) {
                    echo implode("\n", array_keys($this->records)) . "\n" .
                        "Do you want to create to following mailboxes? [y/N]: ";
                    $line = fgets($handle);
                    if (trim($line) == 'y') {
                        echo "\nCreating mailboxes...\n";
                        $this->createMailBoxes();
                    }

                    echo "Fill mailboxes from another imap host? [y/N]: ";
                    $line = fgets($handle);
                    if (trim($line) == 'y') {
                        $this->configureSync($handle);
                        echo "\nSyncing IMAP mailboxes...\n";
                        foreach ($this->records as $record) {
                            $this->syncImap($record);
                        }
                    }
                }

                echo "Do you want to add users with these mailaccounts in this GroupOffice installation [y/N]: ";
                $line = trim(fgets($handle));
                if ($line == 'y') {
                    echo "\nEnter SMTP host for the accounts [" . $this->target['smtp_host'] . "]: ";
                    $line = trim(fgets($handle));
                    if (!empty($line))
                        $this->target['smtp_host'] = $line;
                    echo "\nPort number [" . $this->target['smtp_port'] . "]: ";
                    $line = trim(fgets($handle));
                    if (!empty($line))
                        $this->target['smtp_port'] = $line;
                    echo "\nCreating users and accounts...\n";
                    $this->createUsersWithMailAccounts();
                }
                echo "All done!\n";
            } catch (Exception $e) {
                echo $e->getMessage() . "\n  at " . $e->getFile() . ":" . $e->getLine() . "\n";
            }
        }

        private function configureSync($handle)
        {
            echo "\nEnter IMAP host to fetch from: ";
            $line = trim(fgets($handle));
            if (!empty($line))
                $this->source['host'] = $line;
            echo "\nPort number [" . $this->source['port'] . "]: ";
            $line = trim(fgets($handle));
            if (!empty($line))
                $this->source['port'] = $line;
            echo "\nEnter IMAP host to copy to [" . $this->target['host'] . "]: ";
            $line = trim(fgets($handle));
            if (!empty($line))
                $this->target['host'] = $line;
            echo "\nPort number [" . $this->target['port'] . "]: ";
            $line = trim(fgets($handle));
            if (!empty($line))
                $this->target['port'] = $line;
        }

        //Read CSV file to an array
        private function loadCsv()
        {
            $records = array();
            $fp = @fopen($this->csv['path'], "r");
            if (!$fp)
                die("Can't find: " . $this->csv['path'] . "\n");
            while ($record = fgetcsv($fp, 4096, $this->csv['delimiter'], $this->csv['enclosure'])) {
                $assocRecord = array();
                foreach ($this->col as $key => $number)
                    $assocRecord[$key] = $record[$number];
                $records[$assocRecord['email']] = $assocRecord;
            }
            //Get domain from last email account
            if (isset($records[0])) {
                $parts = explode('@', $records[0]['email'], 2);
                $this->domain = end($parts);
            }
            return $records;
        }

        //Fetch all Mail and copy to new IMAP server using ImapSync
        private function syncImap($record)
        {
            echo "Syncing " . $record['email'] . "...\n\n";
            $cmd = $this->imap_sync . ' --syncinternaldates --authmech1 LOGIN --authmech2 LOGIN ' .
                '--host1="' . $this->source['host'] . '" --user1="' . $record['email'] . '" --password1="' . $record['password'] . '" ' .
                '--host2="' . $this->target['host'] . '" --user2="' . $record['email'] . '" --password2="' . $record['password'] . '" ' .
                '--subscribe --allowsizemismatch --nofoldersizes ' .
                '--sep1 / --sep2 . --regextrans2 "s,/,_,g"'; // --folder "INBOX"
            if (!empty($this->log_file))
                $cmd .= ' > ' . __DIR__ . '/' . $this->log_file . '_' . date('Y-m-d\ H:i:s') . '.log';
            system($cmd);
        }

        // Create GroupOffice Mailboxes
        private function createMailBoxes()
        {
            $domain = Domain::model()->findSingleByAttribute('domain', $this->domain);
            if (empty($domain)) {
                $domain = new Domain();
                $domain->transport = 'virtual';
                $domain->active = '1';
                $domain->domain = $this->domain;
                $domain->default_quota = $this->quota;
                $domain->user_id = 1;
                if (!$domain->save()) {
                    throw new Exception('Error while saving domain: ' . $this->domain . "\n" . implode("\n", $domain->getValidationErrors()));
                }
            }
            foreach ($this->records as $record) {
                $username = current(explode("@", $record['email']));
                $mailbox = Mailbox::model()->findSingleByAttribute('username', $username);
                if (!$mailbox) {
                    $mailbox = new Mailbox();
                    $mailbox->domain_id = $domain->id;
                    $mailbox->username = $record['email']; //$username;
                    $mailbox->quota = $domain->default_quota;
                }
                $mailbox->name = $record['email'];
                $mailbox->password = $record['password'];
                echo "Saving mailbox " . $mailbox->username . " with quota " . ($mailbox->quota / 1024) . " MB...\n";
                if (!$mailbox->save()) {
                    throw new Exception('Error while saving mailbox: ' . $record['email'] . "\n" . implode("\n", $mailbox->getValidationErrors()));
                }
            }
            echo "All mailboxes are created, time to fetch from source mail host...\n";
        }

        private function createUsersWithMailAccounts()
        {
            foreach ($this->records as $record) {
                $parts = explode("@", $record['email']);
                $username = $parts[0];

                // Check if the user exists in Group-Office and if it doesn't create it.
                $user = User::find()->where(['username' => $username])->single();
                if (!$user) {
                    $user = new User();
                    $user->username = $username;
                    $user->displayName = $record['displayName'];
                    $user->recoveryEmail = $record['email'];
                    $user->email = $record['email'];
                    $user->enabled = 1;
                }
                $user->setPassword($record['password']);
                if (!$user->save()) {
                    throw new Exception('Error while saving user: ' . $username . "\n" . print_r($user->getValidationErrors(), true));
                }

                // Create an e-mail account for the user
                $account = Account::model()->findSingleByAttributes([
                    'username' => $record['email'],
                    'user_id' => $user->id
                ]);
                if (!$account) {
                    $account = new Account();
                    $account->user_id = $user->id;
                    $account->mbroot = '';
                    $account->type = 'imap';
                    $account->imap_encryption = $this->target['port'] == 143 ? '' : ($this->target['port'] == 993 ? 'ssl' : 'tls');
                    $account->smtp_encryption = $this->target['port'] == 25 ? '' : ($this->target['port'] == 465 ? 'ssl' : 'tls');;
                    $account->smtp_username = '';
                    $account->smtp_password = '';
                    $createAlias = [$user->email, $user->displayName];
                }
                $account->host = $this->target['host'];
                $account->port = $this->target['port'];
                $account->smtp_host = $this->target['smtp_host'];
                $account->smtp_port = $this->target['smtp_port'];
                $account->username = $record['email'];
                $account->password = $record['password'];
                if (!$account->save())
                    throw new Exception('Error while saving account: ' . $username . "\n" . implode("\n", $account->getValidationErrors()));

                if (isset($createAlias)) {
                    $account->addAlias(...$createAlias);
                }
                echo $username . "\n";
            }
        }
    }