#%%
#Build a graph and find its best partition then plot it with colors
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import time

#from modularity_maximization import partition
#from modularity_maximization.utils import get_modularity

import community as community_louvain


G = nx.Graph()

#Building graph
name = input("Pls enter name of the graph: ")
loc = input("Pls enter location of the graph: ")
G = nx.Graph(name=name)
f= open(loc,"r")
for x in f:
    y = x.split(" ")
    G.add_node(y[0])
    G.add_node(y[1])
    G.add_edge(*y)
f.close()
print(nx.info(G))
#nx.write_pajek(G,"auther_file.net")
#plt.subplot(121)
#nx.draw(G, with_labels=True, font_weight='bold')
#plt.show()
t0= time.time()
#first compute the best partition
partition = community_louvain.best_partition(G)
t1= time.time() - t0
#f= open("../partitions/"+name+"_auther_file.txt","w")
#f.write(partition)
print("Time elapsed for partition: ", t1)



#%%
# draw the graph
t0= time.time()
pos = nx.spring_layout(G)
t1= time.time() - t0
print("Time elapsed for drawing the graph: ", t1)

# color the nodes according to their partition
t0= time.time()
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=10,
                       cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
t1= time.time() - t0
print("Time elapsed for coloring the graph: ", t1)

plt.show()

# %%
