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
#quit(1)

line_space = '''
!
!
'''

for device in list:
       connection = ConnectHandler(**device)

       print(f'{line_space}Entering the enable mode ...{line_space}')
       connection.enable()              # To enter enable mode. Not required if user has privilage level 15 or so

       prompt = connection.find_prompt()
       hostname = prompt[0:-1]

        # This is f string format mehtod to use placeholder and values. Other option could be .format fuction
       file = f'{hostname}.txt'
       print(f'sending configuration from file {file} {line_space}')

       #file = input(f'Enter Configuration file name and valid path for {device["host"]} {device["port"]}: ')
       output = connection.send_config_from_file(file)         #Send configuration from txt file
       print(output)

       print(f'{line_space}Closing Connection to {device["host"]} {device["port"]}')
       connection.disconnect()

       print(100 * '#')
