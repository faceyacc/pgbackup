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
