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

connection = ConnectHandler(**cisco_device)
print('Connected to device')

print(20 * '#')
print('Configuring device')

cmd = '''
interface loopback 10
ip add 99.1.1.10 255.255.255.255
!
int lo11
ip add 99.1.1.11 255.255.255.255
!
int lo12
ip add 99.1.1.12 255.255.255.255
'''
output = connection.send_config_set(cmd.split('\n'))
print(output)

print('Closing connection')
connection.disconnect()
