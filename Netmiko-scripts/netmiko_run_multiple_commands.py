from netmiko import ConnectHandler
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '10.66.76.74',
       'username': 'admin',
       'password': 'c1sc0',
       'port': 2202,             # optional, default 22
       'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }
connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable()

# this method receives a list of commands to send to the device
# in enters automatically into global config mode and exists automatically at the end
# commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco']
# output = connection.send_config_set(commands)
# print(output)

## VARIATIONS
## 1.
# cmd = 'ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.io'
# output = connection.send_config_set(cmd.split(';'))
# print(output)
#
# ## 2.
cmd = '''ip ssh version 2
access-list 1 permit any
ip domain-name net-auto.io
'''
output = connection.send_config_set(cmd.split('\n'))
print(output)

print(20 * '#')

# in enters automatically into global config mode and exit automatically at the end
print(connection.find_prompt())

wr_mem = connection.send_command('write memory')
print(wr_mem)


print('Closing connection')
connection.disconnect()