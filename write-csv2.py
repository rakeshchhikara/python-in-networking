import csv

with open('table.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    for x in range(1,501):
        writer.writerow([x, x * 2, x * 3, x * 4, x * 5, x * 6, x * 7, x * 8, x * 9, x * 10])
