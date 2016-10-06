from __future__ import unicode_literals

import os
import random
import ipaddress as ip

ASes = []
f = open('ASes', 'r')
for line in f.readlines():
    ASes.append(line.rstrip())

# for filename in os.listdir(os.getcwd() + "/Prefix"):
# 	filename = filename.rstrip('\n')

for filename in ASes:
	print "Finding IP for ASN: " + filename
	output_file = open(os.getcwd() + "/IP/AS" + filename, 'a')
	input_file = open(os.getcwd() + "/Prefix/AS" + filename, 'r')
	for line in input_file.readlines():
		line = line.rstrip('\n')
		ipnet = ip.ip_network(line)

		hosts = list(ipnet.hosts())
		if len(hosts) > 2:
			output_file.write(str(hosts[random.randint(1, len(hosts)-1)])+"\n")
			output_file.write(str(hosts[random.randint(1, len(hosts)-1)])+"\n")
			output_file.write(str(hosts[random.randint(1, len(hosts)-1)])+"\n")



	output_file.close()
	input_file.close()

print "script completed :)"
