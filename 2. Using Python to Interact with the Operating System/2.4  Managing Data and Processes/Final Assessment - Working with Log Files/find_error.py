#!/usr/bin/env python3
import sys
import os
import re

# Search log file for user defined pattern
def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors

# Creates an output file that contains the error which matches the user defined pattern 
def file_output(returned_errors):
  with open(os.path.dirname(os.path.realpath(__file__)) + '\data\errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()

if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)

# execute the below command in the cwd of this script:
# python find_error.py data/fishy.log

# The output should create a errors_found.log inside data directory, that should contain the user defined pattern