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

import sys
import os
import click
from xmlrpclib import ServerProxy

import find
import run
# from choose_ips_from_prefixes import choose_ips_from_prefixes
# from find_traceroute_path import find_traceroute_path
# from run_traceroute import run_traceroute

#======= DO NOT CHANGE ==========
NODES_DIR = "Nodes" # Directory containing nodes
MAX_PROCESSES = 50  # No. of processes you want to run.
#================================


@click.group()
def cli():
	pass

@cli.command()
def license():
	"""shows license"""
	print """
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

@cli.command()
@click.option('--asn', prompt='AS number to analyse', help="AS number to analyse")
def analyse(asn):
	"""Analyse traceroute output."""
	# remove AS from the AS number if exists
	if asn[:2].upper() != "AS":
		asn = "AS" + asn

	print "NOTE: MAKE SURE YOU HAVE ALREADY RUN 'rocketfuel start' OR HAVE TRACEROUTE RESULTS in 'Traceroutes' directory."

	# run.combine_traceroute_results(asn)
	#find.traceroute_path(asn)
	# find.unique_ips(asn)
	# find.ip_to_as_mapping(asn)
	# find.ip_in_given_as(asn)
	# find.edge_routers(asn)
	# find.core_routers(asn)
	

@cli.command()
@click.option('--ases', prompt='ASes file path', help="File containing list of ASes")
@click.option('--username', prompt='Planet lab account username', help="slice name associated with account")
@click.option('--password', prompt='Planet lab account password', help="slice name associated with account")
@click.option('--slicename', prompt='slice name associated with your account', help="slice name associated with account")
@click.option('--key', prompt='private key file path', help="private key file path to ssh into planet lab nodes.\nVisit https://www.planet-lab.org/ to add you private key")
def start(ases, username, password, key, slicename):

	if key is None:
		print "Private key is required to ssh into Planet lab nodes.\n\
		type 'rocketfuel start --help' for more info"
	if username is None:
		print "Username is required to login into Planet lab account.\n\
		type 'rocketfuel start --help' for more info"
	if password is None:
		print "Need password to login into Planet lab account"
	if slicename is None:
		print "No slice name passed"

	# getting nodes
	auth = dict()
	auth['Username'] = username
	auth['AuthString'] = password
	auth['AuthMethod'] = "password"

	try:
		api_server = ServerProxy('https://www.planet-lab.org/PLCAPI/')
		if run.planet_lab_auth(api_server, auth):
			node_list = find.user_slice(api_server, auth, slicename)

			if not os.path.exists(NODES_DIR):
				os.mkdir(NODES_DIR)

			# Separating nodes into 50 parts which will run concurrently
			node_index = 0
			node_limit = len(node_list)/MAX_PROCESSES
			for i in xrange(0, MAX_PROCESSES):
				fnodes = open(NODES_DIR + "/nodes_" + str(i), 'w')
				nodes_added = 0
				while nodes_added < node_limit:
					fnodes.write(node_list[node_index] + "\n")
					node_index += 1
					nodes_added += 1
				fnodes.close()

		else:
			sys.exit()
	except KeyboardInterrupt:
		sys.exit()
	except:
		raise

	"""start traceroutes to ASes from Planet Lab nodes."""
	# remove AS from the AS number if exists

	f = open(ases, 'r')
	for line in f.readlines():
		line = line.rstrip()
		asn = line

		if asn[:2].upper() != "AS":
			asn = "AS" + asn

		#Get all advertised prefixes for the AS.
		find.prefix(asn)
		#Randomly get some ips from each advertised prefixes.
		find.ip_from_prefix(asn)
		#Finally, run the traceroute
		run.traceroute(asn, key, slicename)
