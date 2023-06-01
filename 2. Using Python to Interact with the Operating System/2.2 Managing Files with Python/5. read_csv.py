import csv

with open('user_record.csv', 'r') as f:
  reader = csv.reader(f)
  header = next(reader)
  for row in reader:
    name, age, city = row
    print("Name: {}, Age: {}, City: {}".format(name,age,city))