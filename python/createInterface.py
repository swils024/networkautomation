import requests
import json

# Self signed certs
requests.packages.urllib3.disable_warnings()

USER = 'developer'
PASS = 'C1sco12345'

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback300",
    "description": "Added by SW",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "3.3.3.3",
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

# Print Results
print('Status Code:' + str(response.status_code))
print('Response Text:' +response.text)