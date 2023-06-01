'''This script reads a log of users running CRON jobs, and as an output it creates the dictionary of the usernames with count of how many times each username appears in our log. The script accepts a command line argument for the path to the log file.'''

import re
import sys

logfile = sys.argv[1]     # OR, logfile = 'syslog.txt'
usernames = {}

with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue             # return control back to the top of a loop when iterating through logs
    pattern = r"USER \((\w+)\)$"
    result = re.search (pattern, line)
    if result is None:
      continue
    name = result[1]
    usernames [name] = usernames.get(name, 0) + 1

print(usernames)

# execute the below command in the cwd of this script:
# python dictionary_of_username_from_log_file.py syslog.txt

# expected output:
# {'good_user': 1, 'naughty_user': 3}