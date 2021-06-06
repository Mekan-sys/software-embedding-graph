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
# %%
import networkx.algorithms.community as nxcomm
bipartition=nxcomm.kernighan_lin_bisection(G)
print(nxcomm.modularity(G,bipartition))
greedymodularity=nxcomm.greedy_modularity_communities(G)
print(nxcomm.modularity(G,greedymodularity))
# %%
t0= time.time()
girvan_newmana=nxcomm.girvan_newman(G)
t1= time.time() - t0
print("Time elapsed for girvan_newman  calculation: ", t1)
print(girvan_newmana)
# %%
nxcomm.modularity(G,partition)