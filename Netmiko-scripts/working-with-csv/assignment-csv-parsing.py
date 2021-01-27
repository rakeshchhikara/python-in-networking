import csv
import json

my_list = list()
with open('devices.txt') as f:
    reader = csv.reader(f, delimiter = ':')
    for row in reader:
        my_list.append(row)
    print(my_list)

