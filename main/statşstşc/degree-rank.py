import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#Building graph
name = input("Pls enter name of the project: ")
f= open("../../graphs/"+name+"_auther_file.txt","r")
for x in f:
    y = x.split("#")
    G.add_node(y[0],type="auther")
    G.add_node(y[1],type="file")
    G.add_edge(*y)

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
dmax = max(degree_sequence)

plt.loglog(degree_sequence, "b-", marker="o")
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")

# draw graph in inset
plt.axes([0.45, 0.45, 0.45, 0.45])
Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
pos = nx.spring_layout(Gcc)
plt.axis("off")
nx.draw_networkx_nodes(Gcc, pos, node_size=20)
nx.draw_networkx_edges(Gcc, pos, alpha=0.4)
plt.show()