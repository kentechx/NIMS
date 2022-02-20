import networkx as nx
import igraph
from cdlib import algorithms
import pyreadr


g = nx.karate_club_graph()
a = g.community_spinglass()
coms = algorithms.louvain(g, weight='weight', resolution=1., randomize=False)