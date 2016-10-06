import os


servers = ["anshika@192.168.2.26", "anshika@192.168.2.27", "anshika@192.168.2.28",
          "anshika@192.168.2.34", "anshika@192.168.2.36", "devashish@192.168.2.74",
          "devashish@192.168.2.75"]

ASes = []
f = open('ASes', 'r')
for line in f.readlines():
    ASes.append(line.rstrip())


for s in servers:
	print "Server: " + s
	s = s + ":~/RocketFuel/IP/"
	for a in ASes:
		print "AS: " + a
		a = "./IP/AS" + a
		print "Command: " + "scp " + a + " " + s
		os.system("scp " + a + " " + s)
