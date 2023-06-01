#!/usr/bin/env python3

import re
import csv
import operator

errors = dict()
per_user = dict()
logfile = "syslog.log"

with open(logfile, 'r') as log_file:
    for log in log_file:
        result = re.search(r"(ERROR|INFO) ([\w\' ]+|[\w\[\]#\ ]+) (\(\w+\)|\(\w+\.\w+\))$", log)
        # print(result)
        # print(result.groups())
        if result is None:
            continue
        if result.groups()[0] == "INFO":
            type = result.groups()[0]
            msg = result.groups()[1]
            name = result.groups()[2][1:-1]
            if name in per_user:
                user = per_user[name]
                user[type] += 1
            else:
                per_user[name] = {'INFO':1, 'ERROR':0}
        if result.groups()[0] == 'ERROR':
            type = result.groups()[0]
            msg = result.groups()[1]
            name = result.groups()[2][1:-1]
            errors[msg] = errors.get(msg, 0) + 1
            if name in per_user:
                user = per_user[name]
                user[type] += 1
            else:
                per_user[name] = {'INFO':0, 'ERROR':1}

sorted_errorMsg = sorted(errors.items(), key = operator.itemgetter(1), reverse=True)
sorted_perUser = sorted(per_user.items())
sorted_errorMsg.insert(0, ("Error", "Count"))
sorted_perUser.insert(0, ("Username", "INFO", "ERROR"))
# print(sorted_errorMsg)
# print(sorted_perUser)

with open("error_message.csv", 'w') as errors_file:
    for data in sorted_errorMsg:
        errors_file.write("{},{}\n".format(data[0], data[1]))
    print("Write Successful!")
 
with open("user_statistics.csv", 'w') as users_file:
    for data in sorted_perUser:
        if isinstance(data[1], dict):
            users_file.write("{},{},{}\n".format(data[0], data[1].get("INFO"), data[1].get("ERROR")))
        else:
            users_file.write("{},{},{}\n".format(data[0],data[1], data[2]))
    print("Write Successful!")
    
# After successful execution of above program:
#To convert the error_message.csv into HTML file run the following command in terminal:

# python csv_to_html.py error_message.csv <html-filename>.html
# Replace <html-filename> with the name of your choice.
# eg: python csv_to_html.py error_message.csv errors_msg.html

# To convert user_statistics.csv into HTML file, run the following command in terminal:
# python csv_to_html.py user_statistics.csv <html-filename>.html
# eg: python csv_to_html.py user_statistics.csv user_stats.html