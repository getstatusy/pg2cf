# pg2cf

Utility program for uploading PostgreSQL backups to RackSpace Cloud Files

# Usage

1. Rename `init.sh.example` to `init.sh`
2. Enter the required variables and source them `source init.sh`
3. Install required python modules with `pip install -r requirements.txt`
4. Make the program executable with `chmod +x pg2cf.py`
5. Execute the program `./pg2cf.py`

Depending on where you set the LOG_FILE in `init.sh` you can view the logs of the application to make sure that everything is working with `tail -f $LOG_FILE`
