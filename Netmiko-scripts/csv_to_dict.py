import csv

list = list()
with open('devices_detail.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        list.append(row)

print(list)
print(type(list))