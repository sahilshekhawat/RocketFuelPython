def find_traceroute_path():
	ASes = []
	f = open('ASes', 'r')
	for line in f.readlines():
	    ASes.append(line.rstrip())

	print "Checking Traceroute results"

	
	print "Found!"
	print "Combining Traceroute results into a single file"
	combined_file = open("./traceroutes/" + AS + "/" + AS + "_ALL", "w+")
	for AS in ASes:
		single_file = open("./traceroutes/" + AS + "/" + AS)

