from netmiko import ConnectHandler
from pprint import pprint

# Specify device information
device = {
    'device_type': 'cisco_ios',
    'ip': 'xx.xx.xx.xx',
    'username': 'test',
    'password': 'cisco',
    'secret': 'test',
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
