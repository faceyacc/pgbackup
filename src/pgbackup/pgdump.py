import sys
import subprocess

# You need to pass in the URL of the database to know where to
# get the data.

try:
    def dump(url):
        """ Takes URL of database, uses subprocess to execute pg_dump comnmand
        to get data from database. """
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
except OSError as err:
    print(f"Error: {err}")
    sys.exit(1)


def dump_file_name(url, timestamp=None):
    """ Creates a file name for s3 bucket based on the name 
    of the database. """

    db_name = url.split('/')[-1]
    db_name = db_name.split('?')[0]
    if timestamp:
        return f'{db_name}-{timestamp}.sql'
    else:
        return f'{db_name}.sql'
