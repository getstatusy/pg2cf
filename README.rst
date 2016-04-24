pg2cf
=====

Utility program for uploading PostgreSQL backups to RackSpace Cloud
Files

`Documentation <http://getstatusy.github.io/pg2cf/>`__

Installation
============

::

    pip install pg2cf

Usage
=====

1. Rename ``init.sh.example`` to ``init.sh``
2. Enter the required variables and source them ``source init.sh``
3. Install required python modules with
   ``pip install -r requirements.txt``
4. Execute the program ``./pg2cf.py``

Depending on where you set the LOG\_FILE in ``init.sh`` you can view the
logs of the application to make sure that everything is working with
``tail -f $LOG_FILE``

`Production Usage
Example <https://blog.statusy.co/easily-send-postgresql-backups-to-rackspace-cloud-files-with-pg2cf/>`__
