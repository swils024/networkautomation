import getpass
import telnetlib

HOST = "192.168.122.100"
tn = telnetlib.Telnet(HOST)

user = raw_input("User: ")
password = getpass.getpass()

tn.read_until("Username: ")
tn.write(user + "\n")

if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")


tn.write("conf t\n")
tn.write("vlan 2\n")
tn.write("name Python_VLAN_2\n")
tn.write("exit\n")
tn.write("vlan 3\n")
tn.write("name Python_VLAN_3\n")
tn.write("exit\n")
tn.write("vlan 4\n")
tn.write("name Python_VLAN_4\n")
tn.write("exit\n")
tn.write("vlan 5\n")
tn.write("name Python_VLAN_5\n")
tn.write("exit\n")
tn.write("vlan 6\n")
tn.write("name Python_VLAN_6\n")
tn.write("exit\n")
tn.write("vlan 7\n")
tn.write("name Python_VLAN_7\n")
tn.write("exit\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()