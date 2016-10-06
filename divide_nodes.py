import os


allnodes = open(os.getcwd() + "/planet_lab_nodes_final", 'r')
lineno = 0
fileno = 1
output_file = open(os.getcwd() + "/Nodes/" + str(fileno) + "Nodes", 'a')
for line in allnodes.readlines():
    # line = line.rstrip('\n')
    if lineno == 20:
        lineno = 0
        fileno += 1
        output_file.close()
        output_file = open(os.getcwd() + "/Nodes/" + str(fileno) + "Nodes", 'a')

    output_file.write(line)
    lineno += 1

output_file.close()
print "Done :)"
