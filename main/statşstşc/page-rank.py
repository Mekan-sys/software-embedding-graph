G = nx.Graph()

#Building graph
name = input("Pls enter name of the project: ")
f= open("../../graphs/"+name+"_auther_file.txt","r")
for x in f:
    y = x.split("#")
    G.add_node(y[0],type="auther")
    G.add_node(y[1],type="file")
    G.add_edge(*y)






G = nx.DiGraph(nx.path_graph(4))
pr = nx.pagerank(G, alpha=0.9)