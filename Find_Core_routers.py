#Find core routers after finding all IPs in AS and All Edge routers
import os

#ases = 	["AS10310", "AS12956", "AS16509", "AS20485", "AS2497", "AS2828", "AS3216", "AS37100", "AS4826", "AS6762", "AS701", "AS8359", "AS9002", "AS6453", "AS6461", "AS6939"]
ases = ["AS12389"]
#As = "AS6453"

for As in ases:

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
