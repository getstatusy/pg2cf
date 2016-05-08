# pg2cf

Utility program for uploading PostgreSQL backups to RackSpace Cloud
Files

[Documentation](http://getstatusy.github.io/pg2cf/)

## Installation

    pip install pg2cf

## Configuration

1. Rename `init.sh.example` to `init.sh`
2. Enter the variables into `init.sh` the purpose of each variable is described below:

| Variable            | Purpose                                                               |
|:--------------------|:----------------------------------------------------------------------|
| DB_USER             | Database user that has access to the database that you wish to backup |
| DB_NAME             | The name of the database that you wish to perform backups on          |
| BACKUP_PATH         | Location on your local filesystem where we will store backups         |
| BACKUP_PREFIX       | The prefix to attach to backup files                                  |
| CF_USERNAME         | CloudFiles username                                                   |
| CF_API_KEY          | Cloudfiles API Key                                                    |
| CF_BACKUP_CONTAINER | Container where the backup will be sent to on CloudFiles              |
| LOG_FILE            | Location of the log file where pg2cf will log to                      |
| DAYS_TO_KEEP_LOCAL  | How many days to keep backups around on the local server              |
| DAYS_TO_KEEP_REMOTE | How many days to keep backups around on the remote server             |

## Usage

1.  Source the Environment Variables `source init.sh`
2.  Execute the program `pg2cf`

Depending on where you set the LOG\_FILE in `init.sh` you can view the
logs of the application to make sure that everything is working with
`tail -f $LOG_FILE`

[Production Usage
Example](https://blog.statusy.co/easily-send-postgresql-backups-to-rackspace-cloud-files-with-pg2cf/)
