pg2cf
=====

Utility program for uploading PostgreSQL backups to RackSpace Cloud
Files

`Documentation <http://getstatusy.github.io/pg2cf/>`__

Installation
------------

::

    pip install pg2cf

Configuration
-------------

1. Rename ``init.sh.example`` to ``init.sh``
2. Enter the variables into ``init.sh`` the purpose of each variable is
   described below:

+------------------+---------------------------------------------------------+
| Variable         | Purpose                                                 |
+==================+=========================================================+
| DB\_USER         | Database user that has access to the database that you  |
|                  | wish to backup                                          |
+------------------+---------------------------------------------------------+
| DB\_NAME         | The name of the database that you wish to perform       |
|                  | backups on                                              |
+------------------+---------------------------------------------------------+
| BACKUP\_PATH     | Location on your local filesystem where we will store   |
|                  | backups                                                 |
+------------------+---------------------------------------------------------+
| BACKUP\_PREFIX   | The prefix to attach to backup files                    |
+------------------+---------------------------------------------------------+
| CF\_USERNAME     | CloudFiles username                                     |
+------------------+---------------------------------------------------------+
| CF\_API\_KEY     | Cloudfiles API Key                                      |
+------------------+---------------------------------------------------------+
| CF\_BACKUP\_CONT | Container where the backup will be sent to on           |
| AINER            | CloudFiles                                              |
+------------------+---------------------------------------------------------+
| LOG\_FILE        | Location of the log file where pg2cf will log to        |
+------------------+---------------------------------------------------------+
| DAYS\_TO\_KEEP\_ | How many days to keep backups around on the local       |
| LOCAL            | server                                                  |
+------------------+---------------------------------------------------------+
| DAYS\_TO\_KEEP\_ | How many days to keep backups around on the remote      |
| REMOTE           | server                                                  |
+------------------+---------------------------------------------------------+

Usage
-----

1. Source the Environment Variables ``source init.sh``
2. Execute the program ``pg2cf``

Depending on where you set the LOG\_FILE in ``init.sh`` you can view the
logs of the application to make sure that everything is working with
``tail -f $LOG_FILE``

`Production Usage
Example <https://blog.statusy.co/easily-send-postgresql-backups-to-rackspace-cloud-files-with-pg2cf/>`__
