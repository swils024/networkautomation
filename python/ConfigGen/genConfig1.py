from configparser import ConfigParser
import datetime

def PrintToConsole(lines):
    for n in range(len(lines)):
        print(lines[n])

def WriteToFile(fileName, lines):
    with open(fileName, 'w') as file:
       file.writelines(s + '\n' for s in lines) 

config = ConfigParser()
config.read('config.ini')
context_IOSXE = config['IOSXE']
today = datetime.date.today()
dateStr = today.strftime('%Y-%m-%d')

lines = []
lines.append('configure terminal')
lines.append('hostname' + ' ' + context_IOSXE['Hostname'])
lines.append('interface'+ ' ' + context_IOSXE['Mgmt_Iface'])
lines.append('ip address'+ ' ' + context_IOSXE['Mgmt_IP']+ ' ' + context_IOSXE['Mgmt_Subnet'])
lines.append('exit')
lines.append('snmp-server'+ ' ' + context_IOSXE['SNMP_Netbrain'])
lines.append('snmp-server'+ ' ' + context_IOSXE['SNMP_BTMS'])


PrintToConsole(lines)
WriteToFile(context_IOSXE['Hostname']+'_'+ dateStr +'.txt', lines)