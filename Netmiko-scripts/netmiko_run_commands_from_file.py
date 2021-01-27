#Import ConnectHandler class from Netmiko liberary. Note, not complete netmiko liberary imported

from netmiko import ConnectHandler

# Create a dict for device details

cisco_device = {
       'device_type': 'cisco_ios',
       'host': '10.66.76.74',
       'username': 'admin',
       'password': 'c1sc0',
       'port': 2202,
       'secret': 'c1sc0',
       'verbose': True
}

print(cisco_device)
exit(1)

connection = ConnectHandler(**cisco_device)
print('Connected to device')

print(20 * '#' + '\n')
print('Configuring device from File')

output = connection.send_config_from_file('create_new_loopback_interfaces.txt')
print(output)

print('Task Completed')


print('Closing connection')
connection.disconnect()
