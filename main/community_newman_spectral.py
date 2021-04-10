#Build a graph and find its best partition then plot it with colors
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import time

from modularity_maximization import partition
from modularity_maximization.utils import get_modularity

G = nx.Graph()

#Building graph
name = input("Pls enter name of the project: ")
f= open("../graphs/"+name+"_auther_file.txt","r")
for x in f:
    y = x.split("#")
    G.add_node(y[0],type="auther")
    G.add_node(y[1],type="file")
    G.add_edge(*y)

#nx.write_pajek(G,"auther_file.net")
print(nx.info(G))
#plt.subplot(121)
#nx.draw(G, with_labels=True, font_weight='bold')
#plt.show()
t0= time.time()
comm_dict = partition(G)
t1= time.time() - t0
print("Time elapsed for partition: ", t1)
t0= time.time()
for comm in set(comm_dict.values()):
    print("Community %d"%comm)
    print(', '.join([node for node in comm_dict if comm_dict[node] == comm]))
t1= time.time() - t0
print("Time elapsed for drawing the graph: ", t1)
t0= time.time()
print('Modularity of such partition is %.3f' % get_modularity(G, comm_dict))
t1= time.time() - t0
print("Time elapsed for Modularity calculation: ", t1)