import csv

users = [{"Name":"Syam","Age":56,"City":"Kathmandu"}, {"Name":"Jason","Age":35,"City":"NYC"}]
keys = ["Name", "Age", "City"]

with open('users.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)