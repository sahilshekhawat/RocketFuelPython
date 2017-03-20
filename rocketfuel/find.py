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
import subprocess
import ipaddress as ip
from bs4 import BeautifulSoup
from sets import Set

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
	output_file = open(os.getcwd() + "/" + filename, 'w')
	input_file = open(os.getcwd() + "/Prefix/AS" + asn, 'r')

	# Regex taken from http://blog.markhatton.co.uk/2011/03/15/regular-expressions-for-ip-addresses-cidr-ranges-and-hostnames/
	cidr_regex = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))$")

	for line in input_file.readlines():

		is_ipv4_cidr_range = cidr_regex.match(line)

		if is_ipv4_cidr_range:
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

def user_slice(api_server, auth, slice_name):
    """ FIND USER SLICE """
    print "Finding Nodes in the slice..."
    try:
        slice_data = api_server.GetSlices(auth, {}, ['name','node_ids'])
        given_slice = None
        for x, y in enumerate(slice_data):
        	if y.get('name') == slice_name:
        		given_slice = y

        if given_slice == None:
        	print "Couldn't find any slice with given name"
        	sys.exit()

        nodes_ids = given_slice.get('node_ids')
        node_details = api_server.GetNodes(auth, {'node_id': nodes_ids}, ['hostname'])

    except:
    	raise

    # if it doesn't goes into except, it goes into else.. :)
    else:
    	# extracting only hostname from node_details
        node_list = [x.get('hostname') for x in node_details]
        print "Found all Nodes :)"
        return node_list

def traceroute_path(asn):
	print "Extracting ip paths from raw traceroute results..."
	input_file = open("Traceroutes/" + asn + "_ALL", 'r')
	output_file = open("Traceroutes/" + asn + "_path", 'w')
	regex_pattern = re.compile("\((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\)")
 
	line = input_file.readline()
	while line != "":
		# print line
		# line = line.rstrip()
		if "traceroute" in line:
			path = ""
			# print line
			
			line = input_file.readline()
			original_line = line
			line = line.rstrip()
			while line != "" and not "traceroute" in line:
				regex_match = re.search(regex_pattern, line)
				# print regex_match
				if regex_match:
					ip_addr = regex_match.group(0)
					# print ip_addr
					ip_addr = str(ip_addr)[1:-1]
					if path == "":
						path = ip_addr
					else:
						path += " " + ip_addr

				line = input_file.readline()
				original_line = line
				line = line.rstrip()

			path += "\n"
			output_file.write(path)
			line = original_line

		else:
			line = input_file.readline()
			# output_file.write(path)
			# output_file.write("\n")

def unique_ips(asn):
	print "Finding unique IP addresses from IP paths..."
	input_file = open("Traceroutes/" + asn + "_path", 'r')
	output_file = open("Traceroutes/" + asn + "_unique_IPs", 'w')

	uips_dict = list()
	for line in input_file.readlines():
		line = line.rstrip()
		tmp = line.split(" ")
		for ip in tmp:
			ip = ip.rstrip()
			if ip not in uips_dict:
				uips_dict.append(ip)


	for ip in uips_dict:
		output_file.write(ip + "\n")

	input_file.close()
	output_file.close()

def ip_to_as_mapping(asn):
	# netcat whois.cymru.com 43
	input_file = open("Traceroutes/" + asn + "_unique_IPs", 'r')
	output_file = open("Traceroutes/" + asn + "_ip_to_AS_results", 'w')

	for line in input_file.readlines():
		line = line.rstrip()
		line += ".origin.asn.cymru.com"
		output = subprocess.Popen(['whois', '-h' , 'whois.cymru.com', line], stdout=subprocess.PIPE).communicate()[0]
		output_file.write(output)

	output_file.close()
	input_file.close()

def ip_in_given_as(asn):

	input_file = open("Traceroutes/" + asn + "_ip_to_AS_results", 'r')
	output_file = open("Traceroutes/" + asn + "_IPs", 'w')

	for line in input_file.readlines():
		line = line.rstrip()
		if line[:2] != "AS":
			line = line.split("|")
			if asn[:2] == "AS":
				asn = asn[2:]

			if line[0].rstrip() == asn:
				output_file.write(line[1].rstrip() + "\n")

	output_file.close()
	input_file.close()

def edge_routers(asn):
	ip_file = open("Traceroutes/" + asn + "_IPs", 'r')
	path_file = open("Traceroutes/" + asn + "_path", 'r')
	output_file = open("Traceroutes/" + asn + "_edge_routers", 'w')

	ip_list = Set()
	edge_routers = Set()
	for line in ip_file.readlines():
		line = line.rstrip()
		ip_list.add(line)

	for line in path_file.readlines():
		line = line.rstrip()
		line = line.split(" ")

		found_previous_edge = False
		for i in xrange(len(line)):
			node = line[i]
			node = node.rstrip()
			if node in ip_list:  # nodes belonging to particular given AS
				if not found_previous_edge:
					found_previous_edge = True
					edge_routers.add(node)

			elif found_previous_edge:
				if i - 1 >= 0:
					found_previous_edge = False
					node = line[i-1].rstrip()
					edge_routers.add(node)

	for ip in edge_routers:
		output_file.write(ip + "\n")

	ip_file.close()
	path_file.close()
	output_file.close()
