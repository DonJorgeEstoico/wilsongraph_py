import matplotlib.pyplot as plt
import networkx as nx

# Initializing Graph object
G = nx.Graph()
# Connecting nodes
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(5, 6)
G.add_edge(6, 7)
G.add_edge(7, 8)
G.add_edge(7, 9)
G.add_edge(9, 10)
G.add_edge(9, 12)
G.add_edge(9, 11)

# Explicit positions
pos = {
    1: (0, 1), 2: (1, 1), 3: (2, 1), 4: (3, 1), 5: (3, 0), 6: (4, 0), 
    7: (5, 1), 8: (6, 0), 9: (6, 1), 10: (7, 0), 11: (8, 1), 12: (8, 0)
    }

# Graph's drawing options
options = {
    "font_size": 16,
    "node_size": 500,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G, pos, **options)

# Axis margin so nodes are not "cutted"
ax = plt.gca()
ax.margins(0.01)
plt.axis("off")
plt.show()