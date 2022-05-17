import getpass
import telnetlib

HOST = "192.168.122.42"
tn = telnetlib.Telnet(HOST)

user = raw_input("User: ")
password = getpass.getpass()

tn.read_until("Username: ")
tn.write(user + "\n")

if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write(password + "\n")
tn.write("conf t\n")
tn.write("int loop 0\n")
tn.write("ip add 1.1.1.1 255.255.255.255\n")
tn.write("exit\n")
tn.write("router ospf 1\n")
tn.write("network 0.0.0.0 0.0.0.0 area 0\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()