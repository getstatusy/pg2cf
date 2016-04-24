#!/usr/bin/env python

"""
pg2cf - Performs PostgresSQL dumps and stashes them away in CloudFiles

The MIT License (MIT)
Copyright (c) 2016 Lev Lazinskiy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import sys
import subprocess
import time
import logging
import cloudfiles

# Database Information
DB_USER = os.environ.get('DB_USER')
DB_NAME = os.environ.get('DB_NAME')
BACKUP_PATH = os.environ.get('BACKUP_PATH')
BACKUP_PREFIX = os.environ.get('BACKUP_PREFIX')

# Rackspace Information
USERNAME = os.environ.get('CF_USERNAME')
API_KEY = os.environ.get('CF_API_KEY')
CONTAINER_NAME = os.environ.get('CF_BACKUP_CONTAINER')

# Application Settings
LOG_FILE = os.environ.get('LOG_FILE')


logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)


def main():
    """
    Backup Database and Upload it to Rackspace Cloudfiles
    """
    try:
        backup = do_backup()
        send_backup(backup[0], backup[1])
        logging.info("Backup Completed")
    except Exception as e:
        logging.error(e)
        sys.exit(1)


def get_conn():
    """
    Return new RackSpace CloudFiles Connection
    """
    try:
        conn = cloudfiles.get_connection(USERNAME, API_KEY)
    except Exception as e:
        logging.error(e)
        sys.exit(1)
    return conn


def get_container(conn):
    """
    Returns Backup container
    """
    try:
        container = conn.get_container(CONTAINER_NAME)
    except Exception as e:
        logging.error(e)
        sys.exit(1)
    return container


def send_backup(filename, file):
    """
    Send Backup to CloudFiles
    """
    try:
        backup_container = get_container(get_conn())
        new_backup = backup_container.create_object(file)
        new_backup.content_type = "application/x-compressed-tar"
        logging.info("Uploading {0} to Rackspace".format(filename))
        new_backup.load_from_filename(filename)
    except Exception as e:
        logging.error(e)
        sys.exit(1)


def delete_backup(filename):
    """
    Delete Backup from Cloudfiles
    """
    try:
        backup_container = get_container(get_conn())
        backup_container.delete_object(filename)
    except Exception as e:
        logging.error(e)
        sys.exit(1)


def do_backup():
    """
    Perform the Database Backup
    """
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = '{0}_{1}.sql'.format(BACKUP_PREFIX, timestamp)
    destination = '{0}/{1}'.format(BACKUP_PATH, filename)
    logging.info('Backing up {0} to {1}'.format(DB_NAME, destination))
    try:
        ps = subprocess.Popen(
            ['pg_dump', '-U', DB_USER, DB_NAME, '-f', destination],
            stdout=subprocess.PIPE
        )
        output = ps.communicate()[0]
        for line in output.splitlines():
            logging.info(line)
    except Exception as e:
        logging.error(e)
        sys.exit(1)
    return destination, filename

if __name__ == '__main__':
    main()
