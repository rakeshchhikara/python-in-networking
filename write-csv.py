# This program is on how to write CSV file

# Import csv module. This is standard module with python i.e no need to install seperatly

import csv

with open('people.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    csvdata = ('Name', 'CEC', 'Shift')
    writer.writerow(csvdata)
    csvdata = ('Rakesh', 'rakeshk6', 'EMEA')
    writer.writerow(csvdata)
    csvdata = ('Ashwani', 'ashthapa', 'EMEA')
    writer.writerow(csvdata)

with open('numbers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for x in range(1,1001):
        writer.writerow([x, x**2, x**3, x**4])
