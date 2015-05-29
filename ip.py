#!/usr/bin/python
#Filename : test.py
#print 'Hello World'
from IPy import IP
ip_s = raw_input('Please input an IP or net-range: ')

ips = IP(ip_s)

if len(ips) > 1:
	print("net : %s" % ips.net())
	print("netmask: %s" % ips.netmask())
	print("broadcast: %s" % ips.broadcast())
else:
	print("reverse address %s" % ips.reverseNames())



