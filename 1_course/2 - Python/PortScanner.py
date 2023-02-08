#!/bin/python3

import sys
import socket
from datetime import datetime

# RUN script with IP as argument #

if len(sys.argv) == 2:
    IP = socket.gethostbyname(sys.argv[1])  # translates hostname to IPv4 #
else:
    print("Invalid number of arguments \nRUN `python3 PortScanner.py <IP>`")

# add a pretty panner #
print("━" * 50)
print("Scanning Target : " + IP)
print("Time start : " + str(datetime.now()))
print("━" * 50)

try:

    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((IP, port))
        # print("Checking port {} ... ".format(port))

        if result == 0:
            print("Port {} is Opened!".format(port))
        s.close()

except  KeyboardInterrupt:
    print("\nExiting... ")
    sys.exit()

except socket.gaierror:
    print("Hostname couldn't be resolved!\nExiting... ")
    sys.exit()

except socket.error:
    print("Couldn't connect to server\nExiting... ")
    sys.exit()

####################################################################################################################
