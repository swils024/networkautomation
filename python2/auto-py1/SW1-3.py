#!/usr/bin/env python
import getpass
import telnetlib

user = raw_input("User: ")
password = getpass.getpass()

f = open('myswitches')

for line in f:
    print "Configuring node: " + (line)
    tn = telnetlib.Telnet(line)
    tn.read_until("Username: ")
    tn.write(user + "\n")

    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("conf t\n")

    for n in range(2,21):
        tn.write("vlan " + str(n) +"\n")
        tn.write("name pyLoop_VLAN_" + str(n) + "\n")
        tn.write("exit\n")

    tn.write("end\n")
    tn.write("wr\n")
    tn.write("exit\n")
    print tn.read_all()
f.close()
