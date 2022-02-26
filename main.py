import numpy as np
import random
import igraph
from cdlib import algorithms
import pyreadr
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

plot, ax = plt.subplots()

def read_graph(file) ->igraph.Graph:
    return igraph.read(file).as_undirected()

g = read_graph("homo.lgl")
g.knn()
nxg = g.to_networkx()
cluster = g.community_optimal_modularity()
a = g.betweenness()
random.seed(81)
igraph.plot(cluster,
            layout=g.layout_fruchterman_reingold(),
            # palette= igraph.GradientPalette("red", "midnightblue"),
            mark_groups=True, vertex_label=g.vs['name'], margin=(100, 100, 100, 100))



