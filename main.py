import networkx as nx
import numpy as np
import igraph
from cdlib import algorithms
import pyreadr
import pandas as pd

def read_graph(file) ->igraph.Graph:
    return igraph.read(file)

g = read_graph("a.lgl")
cluster = g.community_spinglass()
igraph.plot(cluster, mark_groups = True, bbox=(2000,2000), vertex_label=g.vs['name'])

