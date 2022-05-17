import requests
import json

# Self signed certs
requests.packages.urllib3.disable_warnings()

USER = 'developer'
PASS = 'C1sco12345'

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

int_number = 5

for x in range(int_number):
  ipaddr = '9.9.9.' + str(x)
  ifName = 'Loopback30' + str(x)
  print('Creating ' + ifName + ': ' +ipaddr)
  
  payload = json.dumps({
    "ietf-interfaces:interface": {
      "name": ifName,
      "description": "Added by SW",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": ipaddr,
            "netmask": "255.255.255.255"
          }
        ]
      }
    }
  })

  headers = {'Content-Type':'application/yang-data+json',
            'Accept': 'application/yang-data+json'}

  response = requests.request('POST', url, auth=(USER, PASS), 
            headers = headers, verify=False, data=payload)

  #Print Results
  print('Status Code:' + str(response.status_code))
  print('Response Text:' +response.text)