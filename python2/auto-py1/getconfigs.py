#!/usr/bin/env python
import getpass
import telnetlib

user = raw_input("User: ")
password = getpass.getpass()
f = open('myswitches')
for line in f:
    print "Getting config from node: " + (line)
    tn = telnetlib.Telnet(line.strip())
    tn.read_until("Username: ")
    tn.write(user + "\n")

    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("terminal length 0\n")
    tn.write("show run\n")
    tn.write("exit\n")
    preamble = tn.read_until("bytes")
    config = tn.read_all()
    file = open("configs/running_" + line.strip() + ".cfg", "w")
    file.write(config)
    file.close()
    tn.write("end\n")
    tn.write("exit\n")
f.close()
