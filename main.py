import numpy as np
import seaborn as sns
import trimesh
import random
import igraph
import sklearn
from cdlib import algorithms
import pyreadr
import holoviews as hv
from holoviews import opts
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_excel("src/adj1.xls", index_col=0).fillna(0).astype(int)
adj_mat = df.to_numpy()
names = list(range(1, 8))
g = igraph.Graph.Adjacency(adj_mat, mode='undirected')
g.vs['name'] = names

G = g.to_networkx()
nx.draw(G, pos=nx.spectral_layout(G))


# colors
c = sns.color_palette(n_colors=20)[12]
g.vs['color'] = [(*c, 1) for j in range(g.vcount())]


random.seed(80)
igraph.plot(g,
            layout=g.layout_fruchterman_reingold(),
            vertex_label=g.vs['name'], margin=(100, 100, 100, 100), bbox=(300, 300),
            #palette= igraph.drawing.colors.ClusterColoringPalette('#d5ebe1', '#ea5514', 5),
         )