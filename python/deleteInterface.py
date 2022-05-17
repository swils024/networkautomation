import requests

# Self signed certs
requests.packages.urllib3.disable_warnings()

USER = 'developer'
PASS = 'C1sco12345'

intname = 'Loopback300'
url = 'https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface=' +intname

payload = {}
headers = {'Accept': 'application/yang-data+json'}
response = requests.request('DELETE',url, auth=(USER, PASS), 
            headers = headers, verify=False, data = payload)

# Print Results
print('Status Code:' + str(response.status_code))
print('Response Text:' +response.text)