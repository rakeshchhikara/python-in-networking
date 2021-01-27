import csv

with open('people.csv', 'a', newline='') as f:
    csvfile = csv.writer(f)
    csvdata = (5,"Rakesh","India")
    csvfile.writerow(csvdata)
