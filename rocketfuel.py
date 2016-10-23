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
import click

import find
import run
# from choose_ips_from_prefixes import choose_ips_from_prefixes
# from find_traceroute_path import find_traceroute_path
# from run_traceroute import run_traceroute

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
@click.argument('AS_number')
def analyse(as_number):
	"""Analyse traceroute output."""
	# remove AS from the AS number if exists
	asn = as_number
	if asn[:2].upper() == "AS":
		asn = asn[2:]

	print "NOTE: MAKE SURE YOU HAVE ALREADY RUN 'rocketfuel start' OR HAVE TRACEROUTE RESULTS."
	

@cli.command()
@click.argument('AS_number')
def start(as_number):
	"""start traceroutes to ASes from Planet Lab nodes."""
	# remove AS from the AS number if exists
	asn = as_number
	if asn[:2].upper() == "AS":
		asn = asn[2:]

	#Get all advertised prefixes for the AS.
	find.prefix(asn)
	#Randomly get some ips from each advertised prefixes.
	find.ip_from_prefix(asn)
	#Finally, run the traceroute
	run.traceroute()