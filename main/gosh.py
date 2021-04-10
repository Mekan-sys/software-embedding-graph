import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import time

#from modularity_maximization import partition
#from modularity_maximization.utils import get_modularity

#Building graph
name = input("Pls enter name of the file: ")
f= open("../graphs/"+name+"_auther_file.txt","r")


auther_dict = {}
file_dict = {}
index = 0
for x in f:
    line = x.split("#")
    if(line[0] not in auther_dict):
        auther_dict[line[0]] = index
        index=index+1

    if(line[1] not in file_dict):
        file_dict[line[1]] = index
        index=index+1
f.close()

G = nx.Graph()
f = open("../graphs/"+name+"_auther_file.txt","r")
g = open("../graphs/"+name+"_gosh_auther_file.txt","w")
idea=0
for z in f:
    line = z.split("#")
#    G.add_node(auther_dict.get(line[0]),type="auther")
#    G.add_node(file_dict.get(line[1]),type="file")
    auther = auther_dict[line[0]]
    file = file_dict[line[1]]
    g.write(str(auther) + "  " + str(file) + "\n")
f.close()
g.close()

print(nx.info(G))