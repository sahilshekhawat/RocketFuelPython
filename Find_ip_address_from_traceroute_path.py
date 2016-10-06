import os

workingDir = os.getcwd()

#Ases = ["AS6461", "AS6453", "AS6939", "AS10310", "AS12956", "AS16509", "AS20485", "AS2497", "AS2828", "AS3216", "AS37100", "AS4826", "AS6762", "AS701", "AS8359", "AS9002"]
#Ases = ["AS209", "AS3549", "AS4134", "AS4323", "AS4837", "AS7018"]
Ases = ["AS2914", "AS3257", "AS13030", "AS1239", "AS1273", "AS32787", "AS16735", "AS10026", "AS6830", "AS3491", "AS18881"]
for As in Ases:
	print "Running for AS: " + As
#As = "AS10310"
	tpath = open(workingDir + "/traceroutes/" + As + "/" + As + "_path", 'r')
	uips = open(workingDir + "/traceroutes/" + As + "/" + As + "_unique_IPs", 'a')

	uips_dict = list()
	for line in tpath.readlines():
		line = line.rstrip()
		tmp = line.split(" ")
		for ip in tmp:
			ip = ip.rstrip()
			if ip not in uips_dict:
				uips_dict.append(ip)


	for ip in uips_dict:
		uips.write(ip + "\n")

	tpath.close()
	uips.close()