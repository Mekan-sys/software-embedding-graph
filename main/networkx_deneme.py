import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import time

#from modularity_maximization import partition
#from modularity_maximization.utils import get_modularity

import community as community_louvain


G = nx.Graph()

#Building graph
name = input("Pls enter name of the file: ")
f= open(name+"_auther_file.txt","r")
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

""" comm_dict = partition(G)
for comm in set(comm_dict.values()):
    print("Community %d"%comm)
    print(', '.join([node for node in comm_dict if comm_dict[node] == comm]))
 
print('Modularity of such partition for tensorflow is %.3f' % get_modularity(G, comm_dict))
"""
t0= time.time()
#first compute the best partition
partition = community_louvain.best_partition(G)
print(partition)
t1= time.time() - t0
print("Time elapsed for partition: ", t1)

# draw the graph
t0= time.time()
pos = nx.spring_layout(G)
t1= time.time() - t0
print("Time elapsed for drawing the graph: ", t1)

# color the nodes according to their partition
t0= time.time()
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                       cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()
t1= time.time() - t0
print("Time elapsed for coloring the graph: ", t1)