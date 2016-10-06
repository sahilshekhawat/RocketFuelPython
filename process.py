#Find core routers after finding all IPs in AS and All Edge routers
import os
import operator
import subprocess

#ases = 	["AS10310", "AS12956", "AS16509", "AS20485", "AS2497", "AS2828", "AS3216", "AS37100", "AS4826", "AS6762", "AS701", "AS8359", "AS9002", "AS6453", "AS6461", "AS6939"]
ases = ["AS2914", "AS3257", "AS13030", "AS1239", "AS1273", "AS32787", "AS16735", "AS10026", "AS6830", "AS3491", "AS18881"]
#As = "AS6453"

#find core routers
for As in ases:

	print "Finding Core routers for AS: " + As
	all_ips = open(os.getcwd() + "/traceroutes/" + As + "/IP_in_" + As, 'r')
	edge_ips = open(os.getcwd() + "/traceroutes/" + As + "/" + As + "_Edge_routers", 'r')
	core_ips = open(os.getcwd() + "/traceroutes/" + As + "/" + As + "_Core_routers", 'a')

	all_ips_list = list()
	for line in all_ips.readlines():
	    all_ips_list.append(line)


	edge_ips_list = list()
	for line in edge_ips.readlines():
	    edge_ips_list.append(line)

	core_ips_list = list()
	for ip in all_ips_list:
	    if ip not in edge_ips_list:
	        core_ips_list.append(ip)

	for ip in core_ips_list:
	    core_ips.write(ip)

	all_ips.close()
	edge_ips.close()
	core_ips.close()


#find frequency
for As in ases:
#As = "AS10310"
	print "Finding IP Frequency for AS: " + As

	traceroute_path = open(os.getcwd() + "/traceroutes/" + As + "/" + As + "_path", 'r')
	edge_ips = open(os.getcwd() + "/traceroutes/" + As + "/" + As + "_Edge_routers", 'r')
	core_ips = open(os.getcwd() + "/traceroutes/" + As + "/" + As + "_Core_routers", 'r')
	all_ips = open(os.getcwd() + "/traceroutes/" + As + "/IP_in_" + As, 'r')
	edge_freq = open(os.getcwd() + "/traceroutes/" + As + "/" + As + "_Edge_freq", 'a')
	core_freq = open(os.getcwd() + "/traceroutes/" + As + "/" + As + "_Core_freq", 'a')
	all_freq = open(os.getcwd() + "/traceroutes/" + As + "/" + As + "_All_freq", 'a')
	comm_freq = open(os.getcwd() + "/traceroutes/" + As + "/" + As + "_Commulative_freq", 'a')



	edge_ips_list = dict()
	for line in edge_ips.readlines():
		line = line.rstrip()
		edge_ips_list[line] = 0


	core_ips_list = dict()
	for line in core_ips.readlines():
		line = line.rstrip()
		core_ips_list[line] = 0


	all_ips_list = dict()
	for line in all_ips.readlines():
		line = line.rstrip()
		all_ips_list[line] = 0

	for line in traceroute_path.readlines():
		ips = line.split()
		for ip in ips:
			ip = ip.rstrip()
			if ip in edge_ips_list.keys():
				edge_ips_list[ip] += 1
			elif ip in core_ips_list.keys():
				core_ips_list[ip] += 1

			if ip in all_ips_list.keys():
				all_ips_list[ip] += 1


	sorted_edge_ips = sorted(edge_ips_list.items(), key=operator.itemgetter(1), reverse=True)
	sorted_core_ips = sorted(core_ips_list.items(), key=operator.itemgetter(1), reverse=True)
	sorted_all_ips  = sorted(all_ips_list.items() , key=operator.itemgetter(1), reverse=True)
	#print sorted_all_ips

	fsum = 0
	for freq in sorted_edge_ips:
		fsum += freq[1]
		edge_freq.write(freq[0].rstrip() + "," + str(freq[1]) + "\n")

	print "Edge: " + str(fsum)

	fsum = 0
	for freq in sorted_core_ips:
		fsum += freq[1]
		core_freq.write(freq[0].rstrip() + "," + str(freq[1]) + "\n")

	print "Core: " + str(fsum)


	fsum = 0
	for freq in sorted_all_ips:
		fsum += freq[1]
		all_freq.write(freq[0].rstrip() + "," + str(freq[1]) + "\n")


	print "ALL: " + str(fsum)


	edge_freq.close()
	core_freq.close()
	all_freq.close()

	traceroute_path = open(os.getcwd() + "/traceroutes/" + As + "/" + As + "_path", 'r')
	paths = list()
	for line in traceroute_path.readlines():
		ips = [x.rstrip() for x in line.split()]
		paths.append(ips)

	paths_len = len(paths)
	print "Paths Len : " + str(paths_len)

	comm_len = 0.0
	for ip in sorted_all_ips:
		#print "Comm len: " + str(comm_len)
		for i in range(paths_len):
			if ip[0].rstrip() in paths[i]:
				paths[i] = []  #set to empty list for already checked path
				comm_len += 1.0

		comm_freq.write(ip[0] + "," + str(comm_len/paths_len) + "\n")

	#print paths
	#print all_ips_list


#results
# output_file = open("output", "a")

# for As in ases:
# 	print "Calculating results for AS: " + As

# 	prefix_fname = os.getcwd() + "/Prefix/" + As
# 	p = subprocess.Popen(['wc', '-l', prefix_fname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# 	result, err = p.communicate()
# 	if p.returncode != 0:
# 		raise IOError(err)
# 	prefixes = int(result.strip().split()[0])

# 	Edge_fname = os.getcwd() + "/traceroutes/" + As + "/" + As + "_Edge_routers"
# 	p = subprocess.Popen(['wc', '-l', Edge_fname], stdout=subprocess.PIPE,  stderr=subprocess.PIPE)
# 	result, err = p.communicate()
# 	if p.returncode != 0:
# 		raise IOError(err)
# 	Edge_router_count = int(result.strip().split()[0])


# 	Core_fname = os.getcwd() + "/traceroutes/" + As + "/" + As + "_Core_routers"
# 	p = subprocess.Popen(['wc', '-l', Core_fname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# 	result, err = p.communicate()
# 	if p.returncode != 0:
# 		raise IOError(err)
# 	Core_router_count = int(result.strip().split()[0])


# 	edge_router_file = open(Edge_fname, 'r')
# 	edge_router_list = list()
# 	for line in edge_router_file.readlines():
# 		line = line.rstrip()
# 		edge_router_list.append(line)

# 	core_router_file = open(Core_fname, 'r')
# 	core_router_list = list()
# 	for line in core_router_file.readlines():
# 		line = line.rstrip()
# 		core_router_list.append(line)


# 	comm_freq = open(os.getcwd() + "/traceroutes/" + As + "/" + As + "_Commulative_freq", 'r')
# 	edge_comm_count = 0
# 	core_comm_count = 0
# 	for line in comm_freq.readlines():
# 		ip,freq = [x.rstrip() for x in line.split(",")]
# 		if float(freq) < 0.9:
# 			if ip in edge_router_list:
# 				edge_comm_count += 1
# 			elif ip in core_router_list:
# 				core_comm_count += 1



# 	# print '{0:7} {1:10} {2:10} {3:4}'.format(As,str(edge_comm_count) +"/" + str(Edge_router_count),
# 	# 	                                   str(core_comm_count) + "/" + str(Core_router_count),
# 	# 	                                   prefixes)

# 	output_file.write("ASN,Edge_Routers,Core_Routers,Prefixes_Advertised")
# 	output_file.write('{0:7},{1:10},{2:10},{3:4}'.format(As,str(edge_comm_count) +"/" + str(Edge_router_count),
# 		                                   str(core_comm_count) + "/" + str(Core_router_count),
# 		                                   prefixes))


# output_file.close()
print "Done :)"
