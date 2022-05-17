# Run on Cisco on-box python shell sbx-nxos-mgmt.cisco.com
from cli import *
cmd1 = 'show ip int brief | json-pretty'
output1 = cli(cmd1)
json_data = cli(cmd1)
json_final = json.loads(json_data)
type(json_data)
type(json_final)
print(output1)
print(json_final["TABLE_intf"]["ROW_intf"][0]["prefix"])
print(json_final["TABLE_intf"]["ROW_intf"][0]["intf-name"])