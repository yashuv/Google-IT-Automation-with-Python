import csv

with open('user_record.csv') as csv_file: 
    reader = csv.DictReader(csv_file) 
    for row in reader:
        print(row['Name'], row['Age'], row['City'])