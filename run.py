"""
A Python implementation of RocketFuel topology engine.					
Copyright (C) 2016 Sahil Shekhawat <sahilshekhawat01@gmail.com> 		
																			
This program is free software: you can redistribute it and/or modify	
it under the terms of the GNU General Public License as published by	
the Free Software Foundation, either version 3 of the License, org  	
(at your option) any later version.									
																		
This program is distributed in the hope that it will be useful,			
but WITHOUT ANY WARRANTY; without even the implied warranty of			
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the			
GNU General Public License for more details.							
																		
You should have received a copy of the GNU General Public licenses 		
along with this program.  If not, see <http://www.gnu.org/licenses/>.	

Type ``rocketfuel license`` to see this message.
"""

import os
import sys
import daemon
import paramiko
import base64

from utils import create_file

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def traceroute(asn, key, user):
	directory = "Traceroutes"
	key = paramiko.RSAKey.from_private_key_file(key)
	create_file(directory + "/")
	ips = _get_ips(asn)
	nodes = _planet_lab_nodes()
	#ips = ["google.com", "fb.com"]
	#nodes = ["planetlab01.cs.washington.edu"]
	sys.stdout.write("Running traceroute commands as a daemon... Bye, until I have all those results ;)")
	try:
		for node in nodes:
			with daemon.DaemonContext(working_directory=os.getcwd()):
				_run(asn, key, user, node, ips)
	except Exception:
		sys.stdout.write("ERROR! skipping\n")

def _run(asn, key, user, node, ips):
	output = open("Traceroutes/" + asn + "#" + node, 'w+')
	#sys.stdout.write("Done!\n")
	#for host in node:
	client.connect(hostname=node, username=user, pkey = key)
	for ip in ips:
		stdin, stdout, stderr = client.exec_command("sudo traceroute " + ip + ";")
		output.write(stdout.read())
	client.close()

def _get_ips(asn):
	ips = list()
	filename = "IP/AS" + asn
	if not os.path.exists(filename):
	    sys.stdout.write("[" + ASN +"] " + "IPs not found, make sure IP addresses are in ./IP/AS" + asn + "\n")
	else:
		f = open(filename, 'r')
		for line in f.readlines():
			line = line.rstrip('\n')
			ips.append(line)
		f.close()
	return ips

def _planet_lab_nodes():
	nodes = []
	directory = "Nodes"
	if not os.path.exists(directory):
		sys.stdout.write("[" + ASN +"] " + "Planet lab nodes not found, make sure nodes are in Nodes directory\n")
	else:
		for filename in os.listdir(directory):
			f = open(directory + "/" +filename, 'r')
			for line in f.readlines():
				line = line.rstrip('\n')
				nodes.append(line)
	return nodes
