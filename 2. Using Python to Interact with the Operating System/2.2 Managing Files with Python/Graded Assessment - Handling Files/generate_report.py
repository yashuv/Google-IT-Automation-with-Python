# !/usr/bin/env python3
'''This script reads the CSV file and generate a report with the total number of people in each department'''

import csv

# receives a CSV file as a parameter and returns a list of dictionaries from that file
def read_employees(csv_file_location):
    employee_list = []

    # register a dialect 'empDialect'.(so that callers of the CSV module don't need to know the parameter settings in advance)
    # main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

    # DictReader creates an object that operates like a regular reader (an object that iterates over lines in the given CSV file)
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')

    for data in employee_file:
        employee_list.append(data)
    return employee_list


employee_list = read_employees('employees.csv')
print(employee_list)

# receives the list of dictionaries, i.e., employee_list as a parameter and return a dictionary of department:amount
def process_data(employee_list):
    department_list = []
    department_data = {}
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data


dictionary = process_data(employee_list)
print(dictionary)

# writes a dictionary of department:amount to a file.
def write_report(dictionary, report_file):
    with open(report_file, 'w+') as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()


write_report(dictionary, 'report.txt')

'''
Output of script in report.txt should generate:
Development:4
Human Resources:2
IT infrastructure:4
Marketing:2
Sales:3
User Experience Research:2
Vendor operations:2
'''