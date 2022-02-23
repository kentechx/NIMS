import networkx as nx
import numpy as np
import igraph
from cdlib import algorithms
import pyreadr
import pandas as pd

def read_graph(file) ->igraph.Graph:
    return igraph.read(file)

g = read_graph("a.lgl")
m = []
names = g.vs['name']
for i in range(4):
    clusters = g.community_spinglass().membership
    clusters = np.array(clusters)
    for i in np.unique(clusters):
        idx = np.where(clusters==i)[0]
        m.append([names[k] for k in idx])

pass

