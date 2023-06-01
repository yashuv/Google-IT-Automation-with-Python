import csv

header = ['Name','Age','City']
rows = [["James",30,"UK"],["Rose",30,"USA"]]

with open('details.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(header)
  writer.writerows(rows)