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
print(nx.edge_connectivity(G))
t1= time.time() - t0
print("Time elapsed for edge connectivity: ", t1)


#%%
t0= time.time()
print(nx.node_connectivity(G))
t1= time.time() - t0
print("Time elapsed for node connectivity: ", t1)
t0= time.time()
print(nx.average_node_connectivity(G))
t1= time.time() - t0
print("Time elapsed for average node connectivity: ", t1)

#%%
t0= time.time()
print(nx.number_connected_components(G))
t1= time.time() - t0
print("Time elapsed for number_connected_components: ", t1)




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


#%%
#Doesn't work for me
ucgenler=nx.triangles(G).values()
number_of_triangles = sum(ucgenler)/3
print(number_of_triangles)

