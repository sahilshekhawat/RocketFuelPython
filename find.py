from __future__ import unicode_literals
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

import re
import os
import sys
import random
import requests
import ipaddress as ip
from bs4 import BeautifulSoup

from utils import create_file

def prefix(asn):
	# ASes = []
	# f = open('ASes', 'r')
	# for line in f.readlines():
	#	 ASes.append(line.rstrip())

	# for asn in ASes:
	# asn = asn.rstrip('\n')
	as_base = 'AS'
	ASN = as_base + asn
	url_base = 'http://ipinfo.io/'
	
	sys.stdout.write("[" + ASN +"] " + "Getting prefixes...")
	sys.stdout.flush()
	
	filename = "Prefix/" + ASN
	create_file(filename)
	output = open(filename, "w")

	page = requests.get(url_base+ASN)
	html_doc = page.content
	soup = BeautifulSoup(html_doc, 'html.parser')
	for link in soup.find_all('a'):
		if asn in link.get('href'):
			auxstring = '/'+as_base+asn+'/'
			line = re.sub(auxstring, '', link.get('href'))
			printstring = line+'\n'
			if 'AS' not in printstring:
				output.write(printstring)
	
	sys.stdout.write(" Done!\n")
	sys.stdout.write("[" + ASN +"] " + "Prefixes are in file: ./" + filename + "\n")

def ip_from_prefix(asn):
	as_base = 'AS'
	ASN = as_base + asn
	sys.stdout.write("[" + ASN +"] " + "Getting ip addresses from advertised prefixes...")
	sys.stdout.flush()

	filename = "IP/" + ASN
	create_file(filename)
	output_file = open(os.getcwd() + "/" + filename, 'a')
	input_file = open(os.getcwd() + "/Prefix/AS" + asn, 'r')
	for line in input_file.readlines():
		line = line.rstrip('\n')
		ipnet = ip.ip_network(unicode(line))

		hosts = list(ipnet.hosts())
		if len(hosts) > 2:
			output_file.write(str(hosts[random.randint(1, len(hosts)-1)])+"\n")
			output_file.write(str(hosts[random.randint(1, len(hosts)-1)])+"\n")
			output_file.write(str(hosts[random.randint(1, len(hosts)-1)])+"\n")

	output_file.close()
	input_file.close()

	sys.stdout.write(" Done!\n")
	sys.stdout.write("[" + ASN +"] " + "IPs are in file: ./" + filename + "\n")

