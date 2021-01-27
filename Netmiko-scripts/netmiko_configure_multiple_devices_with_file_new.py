import csv           # Import csv module to handle csv file
from netmiko import ConnectHandler        # Import ConnectHandler Class of netmiko library


# Create an Empty List

list = list()

# open csv file and read it as dictionary.

with open('devices_detail.csv') as f:
    reader = csv.DictReader(f, delimiter=',')

    for row in reader:             # Use for loop to append dictionary rows to the earlier created empty list.
        list.append(row)

#print(list)
#print(type(list))


for device in list:
       connection = ConnectHandler(**device)

       print('Entering the enable mode ...')
       connection.enable()                       # To enter enable mode. Not required if user has privilage level 15 or so

       file = input('Enter File name: ')
       output = connection.send_config_from_file(file)         #Send configuration from txt file
       print(output)

       print('Closing Connection')
       connection.disconnect()

       print(100 * '#')
