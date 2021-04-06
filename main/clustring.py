import networkx as nx

from modularity_maximization import partition
from modularity_maximization.utils import get_modularity

momo = nx.Graph(nx.read_pajek("auther_file.net"))
print(nx.info(momo))