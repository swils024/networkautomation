from netmiko import ConnectHandler
import json
nx_os = {
    'device_type':'cisco_ios',
    'ip': 'sbx-nxos-mgmt.cisco.com',
    'username': 'admin',
    'password': 'Admin_1234!',
    'port': 8181
}
net_connect = ConnectHandler(**nx_os)
output = net_connect.send_command('show ip int br | json')
json_data = json.loads(output)
int_number = len(json_data['TABLE_intf']['ROW_intf'])

for x in range(int_number):
    print('\n')
    print('name:',json_data['TABLE_intf']['ROW_intf'][x]['intf-name'])
    print('prefix:',json_data['TABLE_intf']['ROW_intf'][x]['prefix'])
    print('proto-state:',json_data['TABLE_intf']['ROW_intf'][x]['proto-state'])
    print('link-state:',json_data['TABLE_intf']['ROW_intf'][x]['link-state'])
    print('admin-state:',json_data['TABLE_intf']['ROW_intf'][x]['admin-state'])   

print('\nNumber of interfaces:',int_number)