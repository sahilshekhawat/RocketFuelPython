import os

def run_traceroute():
	ASes = []
	f = open('ASes', 'r')
	for line in f.readlines():
	    ASes.append(line.rstrip())

	for AS in ASes:
		os.popen("bash ./run.sh " + AS)