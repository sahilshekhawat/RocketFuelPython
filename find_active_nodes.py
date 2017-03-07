import sys
import socket
from paramiko import *

# Change following variables =========
USERNAME = "iiitd_anshika"				# Planet lab slice name
KEY_FILENAME = "planetLab_privateKey"	# Key name
NODES = "NODES"							# File which contains all nodes
NODES_ACTIVE = "NODES_ACTIVE"			# Output file
# ====================================


f = open(NODES, "r")
client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())

nodes = []
for node in f.readlines():
	nodes.append(node)

# for node in nodes:
node = sys.argv[1]
node = node.rstrip()
print "=>Node: " + node
try:
	output = open("output/" + node, "w+")
	for dest_node in nodes:
		client.connect(node, username=USERNAME, key_filename=KEY_FILENAME, timeout=20)
		stdin, stdout, stderr = client.exec_command('traceroute ' + dest_node)
		if(stdout):
			for l in stdout.readlines():
				output.write(l)
			# output.write(stdout.readlines())
   		client.close()
   		output.write("\n")

	output.close()
	# output.write(node + "\n")
except (BadHostKeyException, AuthenticationException, 
		SSHException, socket.error, EOFError) as e:
	print "   Error: " + str(e)

# output.close()
