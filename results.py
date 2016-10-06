import os
import subprocess

ases = 	["AS10310", "AS12956", "AS16509", "AS20485", "AS2497", "AS2828", "AS3216", "AS37100", "AS4826", "AS6762", "AS701", "AS8359", "AS9002", "AS6453", "AS6461", "AS6939", "AS12389"]

output_file = open("output.csv", "a")
output_file.write("ASN,Edge_Routers,Core_Routers,Prefixes_Advertised\n")

for As in os.listdir(os.getcwd() + "/traceroutes"):
	As = As.rstrip('\n')
# for As in ases:
	prefix_fname = os.getcwd() + "/Prefix/" + As
	p = subprocess.Popen(['wc', '-l', prefix_fname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	result, err = p.communicate()
	if p.returncode != 0:
		raise IOError(err)
	prefixes = int(result.strip().split()[0])

	Edge_fname = os.getcwd() + "/traceroutes/" + As + "/" + As + "_Edge_routers"
	p = subprocess.Popen(['wc', '-l', Edge_fname], stdout=subprocess.PIPE,  stderr=subprocess.PIPE)
	result, err = p.communicate()
	if p.returncode != 0:
		raise IOError(err)
	Edge_router_count = int(result.strip().split()[0])


	Core_fname = os.getcwd() + "/traceroutes/" + As + "/" + As + "_Core_routers"
	p = subprocess.Popen(['wc', '-l', Core_fname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	result, err = p.communicate()
	if p.returncode != 0:
		raise IOError(err)
	Core_router_count = int(result.strip().split()[0])


	edge_router_file = open(Edge_fname, 'r')
	edge_router_list = list()
	for line in edge_router_file.readlines():
		line = line.rstrip()
		edge_router_list.append(line)

	core_router_file = open(Core_fname, 'r')
	core_router_list = list()
	for line in core_router_file.readlines():
		line = line.rstrip()
		core_router_list.append(line)


	try:
		comm_freq = open(os.getcwd() + "/traceroutes/" + As + "/" + As + "_Commulative_freq", 'r')
		edge_comm_count = 0
		core_comm_count = 0
		for line in comm_freq.readlines():
			ip,freq = [x.rstrip() for x in line.split(",")]
			if float(freq) < 0.9:
				if ip in edge_router_list:
					edge_comm_count += 1
				elif ip in core_router_list:
					core_comm_count += 1



		print '{0},{1},{2},{3}'.format(As,str(edge_comm_count) +"/" + str(Edge_router_count),
			                                   str(core_comm_count) + "/" + str(Core_router_count),
			                                   prefixes)

		output_file.write('{0},{1},{2},{3}\n'.format(As,str(edge_comm_count) +"/" + str(Edge_router_count),
			                                   str(core_comm_count) + "/" + str(Core_router_count),
			                                   prefixes))


	except IOError:
		continue