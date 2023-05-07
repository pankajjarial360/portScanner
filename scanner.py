#!/bin/python

import sys
import socket
from datetime import datetime



# Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])	#Translate hostname to IPv4
else: 
	print("Invalid amount of arguments")
	print("sysntax: python3 scanner.py <ip>")
	
# Add - pretty banner......

print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range (1,10000):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))	#returns an error indicator
		print("checking port {}".format(port))
		if result ==0:
			print ("Port {} is open ".format(port))
			s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.error:
	print("Couln't connet to server.")
	sys.exit()

