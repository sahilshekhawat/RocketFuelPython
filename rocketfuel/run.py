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
import paramiko
import base64
import subprocess

from utils import create_file

#======= DO NOT CHANGE ==========
NODES_DIR = "Nodes" # Directory containing nodes
MAX_PROCESSES = 50  # No. of processes you want to run.
#================================

def traceroute(asn, key, slicename):
	print "Running traceroute commands as a daemon...^_^"
	f = open("pid_file", 'w+')
	for i in xrange(MAX_PROCESSES):
		p = subprocess.Popen(["python", "./rocketfuel/traceroute.py", asn, key, slicename, str(i)], shell=False)
		f.write(str(p.pid))
		f.write("\n")

	print "Bye, until I have all those results ;)"
	sys.exit(0)

def planet_lab_auth(api_server, auth):
	sys.stdout.write("Verifying planet lab account info...\n")

	try:
		if api_server.AuthCheck(auth) == 1:
			sys.stdout.write("...Verified!\n")			
			return True
	except:
		sys.stdout.write( "Error!")
		return False
