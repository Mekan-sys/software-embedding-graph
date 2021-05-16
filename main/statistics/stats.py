# %%
import matplotlib.pyplot as plt
import networkx as nx
import time
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
print(nx.info(G))
#%%
print(nx.average_clustering(G)) 
print(nx.average_degree_connectivity(G))

#%%
t0= time.time()
print(nx.diameter(G))
t1= time.time() - t0
print("Time elapsed for diameter calculation: ", t1)

#%%
t0= time.time()
print(nx.average_shortest_path_length(G))
t1= time.time() - t0
print("Time elapsed for Average Shortest Path Calculation: ", t1)


#%%
t0= time.time()
print(nx.node_connectivity(G))
t1= time.time() - t0
print("Time elapsed for node connectivity: ", t1)

#%%
t0= time.time()
print(nx.edge_connectivity(G))
t1= time.time() - t0
print("Time elapsed for edge connectivity: ", t1)

t0= time.time()
print(nx.average_node_connectivity(G))
t1= time.time() - t0
print("Time elapsed for average node connectivity: ", t1)
#%%
#Approximations
from networkx.algorithms import approximation as approx
t0= time.time()
print(approx.node_connectivity(G))
t1= time.time() - t0
print("Time elapsed for average node connectivity approximation: ", t1)

t0= time.time()
print(approx.average_clustering(G))
t1= time.time() - t0
print("Time elapsed for average clustering approximation: ", t1)

#%%
#Page rank
import json
pr = nx.pagerank(G, alpha=0.9)
f= open(name+"_pagerank.txt","w")
json.dump(pr, f)


# %%
#Degree frequency
m=1
degree_freq = nx.degree_histogram(G)
degrees = range(len(degree_freq))
plt.figure(figsize=(12, 5)) 
plt.loglog(degrees[m:], degree_freq[m:],'go-') 
plt.xlabel('Degree')
plt.ylabel('Frequency')


#%%
#Distribution of Node Linkages (degree(log-log scale))
import numpy as np
def plot_degree_histogram(g, normalized=True):
    print("Creating histogram...")
    aux_y = nx.degree_histogram(g)
    
    aux_x = np.arange(0,len(aux_y)).tolist()
    
    n_nodes = g.number_of_nodes()
    
    if normalized:
        for i in range(len(aux_y)):
            aux_y[i] = aux_y[i]/n_nodes

    plt.title('\nDistribution Of Node Linkages (log-log scale)')
    plt.xlabel('Degree\n(log scale)')
    plt.ylabel('Number of Nodes\n(log scale)')
    plt.xscale("log")
    plt.yscale("log")
    plt.plot(aux_x, aux_y, 'o')

plot_degree_histogram(G)


# %%
#Degree distibution function of networkx
import collections
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color="b")

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

# draw graph in inset
plt.axes([0.4, 0.4, 0.5, 0.5])
Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
pos = nx.spring_layout(G)
plt.axis("off")
nx.draw_networkx_nodes(G, pos, node_size=1)
nx.draw_networkx_edges(G, pos, alpha=0.2)


# %%
#The diameter helps us understand how wide the graph is.
nx.diameter(G)
#for all the different degrees that occur in the graph, it gives the average of the average_neighbor_degree of all nodes with the same degree. 
#It is a measure of how connected nodes with certain degrees are.
##The k-mean degree connectivity is the average of the mean neighbor degrees of vertices of degree k.
nx.average_degree_connectivity(G)
sum(nx.average_degree_connectivity(G))
#The average shortest path length is the sum of path lengths d(u,v) between all pairs of nodes 
# (assuming the length is zero if v is not reachable from v) normalized by n*(n-1) where n is the number of nodes in G.
nx.average_shortest_path_length(G)


#%%
#Doesn't work for me
ucgenler=nx.triangles(G).values()
number_of_triangles = sum(ucgenler)/3
print(number_of_triangles)

