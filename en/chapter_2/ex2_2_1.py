import matplotlib.pyplot as plt
import networkx as nx

# Initializing Graph object
G = nx.Graph()
# Connecting nodes
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)

# Explicit positions
pos = {1: (0, 0), 2: (0, 2), 3: (2, 1), 4: (3, 1)}

# Graph's drawing options
options = {
    "font_size": 24,
    "node_size": 2000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}

nx.draw_networkx(G, pos, **options)
# Adding edge labels for Graph
edge_labels = {edge: f"{i}" for i, edge in enumerate(G.edges(), start=1)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# Axis margin so nodes are not "cutted"
ax = plt.gca()
ax.margins(0.1)
plt.axis("off")
plt.show()