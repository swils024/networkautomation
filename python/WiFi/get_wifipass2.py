# Enable the use of system commands and regular expressions
import subprocess
import re
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
if len(profile_names) != 0:
    for name in profile_names:
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
        password = re.search("Key Content            : (.*)\r", profile_info)
        if password == None:
            continue
        print("'" + name + "'\t", password[1])      
