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
output = net_connect.send_command('show ip int br | json-pretty')
json_data = json.loads(output)
print('name:',json_data['TABLE_intf']['ROW_intf'][0]['intf-name'])
print('prefix:',json_data['TABLE_intf']['ROW_intf'][0]['prefix'])
print('proto-state:',json_data['TABLE_intf']['ROW_intf'][0]['proto-state'])
print('link-state:',json_data['TABLE_intf']['ROW_intf'][0]['link-state'])
print('admin-state:',json_data['TABLE_intf']['ROW_intf'][0]['admin-state'])