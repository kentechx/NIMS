import numpy as np
import trimesh
import random
import igraph
import sklearn
from cdlib import algorithms
import pyreadr
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

plot, ax = plt.subplots()

def read_graph(file) ->igraph.Graph:
    return igraph.read(file).as_undirected()

g = read_graph("src/exa_homo.lgl")
g.knn()
nxg = g.to_networkx()
cluster = g.community_optimal_modularity()
a = g.betweenness()
random.seed(81)
# igraph.plot(cluster,
#             layout=g.layout_reingold_tilford(),
#             # palette= igraph.GradientPalette("red", "midnightblue"),
#             mark_groups=True, vertex_label=g.vs['name'], margin=(100, 100, 100, 100))
igraph.drawing.colors.GradientPalette()
igraph.drawing.colors.Palette()


from bokeh.io import output_file, show
from bokeh.plotting import figure, from_networkx
from bokeh.io import output_file, show
from bokeh.models import (BoxSelectTool, Circle, EdgesAndLinkedNodes, HoverTool,
                          MultiLine, NodesAndLinkedEdges, Plot, Range1d, TapTool)
from bokeh.palettes import Spectral4
from bokeh.plotting import from_networkx

G = g.to_networkx()

plot = Plot(width=400, height=400,
            x_range=Range1d(-1.1,1.1), y_range=Range1d(-1.1,1.1))
plot.title.text = "Graph Interaction Demonstration"

plot.add_tools(HoverTool(tooltips=None), TapTool(), BoxSelectTool())
plot.add_tools()

graph_renderer = from_networkx(G, nx.circular_layout, scale=1, center=(0,0))

graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
graph_renderer.node_renderer.selection_glyph = Circle(size=15, fill_color=Spectral4[2])
graph_renderer.node_renderer.hover_glyph = Circle(size=15, fill_color=Spectral4[1])

graph_renderer.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=5)
graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[2], line_width=5)
graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=5)

graph_renderer.selection_policy = NodesAndLinkedEdges()
graph_renderer.inspection_policy = EdgesAndLinkedNodes()

plot.renderers.append(graph_renderer)

# output_file("interactive_graphs.html")
show(plot)
