#Import ConnectHandler class from Netmiko liberary. Note, not complete netmiko liberary imported

from netmiko import ConnectHandler

# reading the devices ip address from a file into a List (each ip on its own line)
# with open('Devices.txt') as f:
#        devices = f.read().splitlines()
#
# print(type(devices))
# print(devices)

with open('Ports.txt') as f:
       ports = f.read().splitlines()

port_list = list()                 # This creates an empty list i.e. [] . Not to mention () are used for tuple but this commands create list not tuple
#print(type(port_list))
#print(port_list)
#exit(1)

# Create a dict for device details

for port in ports:
       cisco_device = {
              'device_type': 'cisco_ios',
              'host': '10.66.76.74',
              'username': 'admin',
              'password': 'c1sc0',
              'port': port,
              'secret': 'c1sc0',
              'verbose': True
       }
       port_list.append(cisco_device)

print(type(port_list))             # This is Tuple of dictonary items
print(port_list)
#exit(1)

for port_num in port_list:
       connection = ConnectHandler(**port_num)

       file = input(f'Enter a configuration file (use a valid path) for {port_num["port"]}:')
       output = connection.send_config_from_file(file)
       print(output)



       print('Closing connection')
       connection.disconnect()

       print(30 * '#')
