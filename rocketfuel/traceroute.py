#!/bin/python2

import os
import sys
import paramiko
import base64

from utils import create_file

#======= DO NOT CHANGE ==========
NODES_DIR = "Nodes" # Directory containing nodes
#================================

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def traceroute(asn, key, slicename, nodenum):
	directory = "Traceroutes"
	key = paramiko.RSAKey.from_private_key_file(key)
	paramiko.util.log_to_file("rocketfuel.log")
	create_file(directory + "/")
	ips = _get_ips(asn)
	nodes = _planet_lab_nodes(nodenum)
	try:
		_run(asn, key, slicename, nodes, ips)
	except Exception:
		pass

def _run(asn, key, user, nodes, ips):

	for node in nodes:
		try:
			output = open("Traceroutes/" + asn + "/" + asn + "#" + node, 'w')
			client.connect(hostname=node, username=user, pkey = key)
			for ip in ips:
				stdin, stdout, stderr = client.exec_command("sudo traceroute " + ip + ";")
				output.write(stdout.read())
			client.close()
		except:
			continue

def _planet_lab_nodes(nodenum):
	nodes = []
	directory = NODES_DIR
	if not os.path.exists(directory):
		sys.stdout.write("[" + ASN +"] " + "Planet lab nodes not found, make sure nodes are in Nodes directory\n")
	else:
		filename = NODES_DIR + "/nodes_" + nodenum
		f = open(filename, 'r')
		for line in f.readlines():
			line = line.rstrip()
			nodes.append(line)
		return nodes

		# for filename in os.listdir(directory):
		# 	# print "NEW NODES FILE FOUND"
		# 	nodes_group = list()
		# 	f = open(directory + "/" +filename, 'r')
		# 	for line in f.readlines():
		# 		line = line.rstrip('\n')
		# 		nodes_group.append(line)
		# 	nodes.append(nodes_group)


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

if __name__ == "__main__":
	if len(sys.argv) != 5:
		print "Error! Require 3 arguments i.e. asn, key, slicename, node no."
		sys.exit()

	traceroute(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
