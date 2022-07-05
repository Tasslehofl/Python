#!/bin/python

#This port scanner is not the best way to do port scanning.
#It is clunky, and slow.  
#But it is built by me in order to help me learn coding with Python.
#This code comes from Heath (TheCyberMentor) at TCM.

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])  #Translating hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
#NOTE: 
# By default, all ports on Kali are closed.  
# To test the port scanner, script, you can use:
# scanme.nmap.org
# This is a service provided by the nmap group and is perfectly legal to scan.	
	
#Adding a banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
#	for port in range(1,65535) #This is for a FULL-on port scanner.  This will take forever to scan.
	for port in range (50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)  #This is going to attempt to connect to a port, and will wait 1 second then move on.
		result = s.connect_ex((target,port))  #Returns an error indicator.  If a port is open, it will return a 0.  If it is not an open, it will give an error and give a 1
		print("Checking port {}".format(port))  #This prints to screen the actually scan in real time.
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")  #If the user wants to interrupt the scan
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.")  #If DNS fails, and the hostname cannot be resolved.
	sys.exit()
except socket.error:
	print("Couldn't connect to server.")  #If the connection to the address cannot me made, in general.
	sys.exit()


#FUTURE THOUGHTS:
# Threading - will allow multiple processes to run at once, reducing the time.
# When coding, try and think logically.  If you want something to happen, what happens if there's an error, or someone does something wrong, or types something in wrong?  Just try and work through all the issues.

