#!/bin/python3

import sys
import socket
from datetime import datetime

#defining our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])  #Translate hostname to IPv4
else: 
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	
#Adding a banner
print("-" * 50)
print("Sanning Target : " + target)
print("Time Started : " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):   #change according to need
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()
	
except socket.gaierror:
	print("\nHostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("\nCould not connect to server.")
	sys.exit()
