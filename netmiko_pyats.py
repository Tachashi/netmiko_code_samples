from netmiko import ConnectHandler
from pprint import pprint

# Specify device information
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.201',
    'username': 'test3',
    'password': 'cisco',
    'secret': 'test3',
} 

# Connect to the device
net_connect = ConnectHandler(**device)

# Enter enable password
net_connect.enable()

# Send show command
output = net_connect.send_command('show interfaces', use_genie=True)
pprint(output)

# Disconnect
net_connect.disconnect()
