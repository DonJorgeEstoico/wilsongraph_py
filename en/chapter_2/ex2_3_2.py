import matplotlib.pyplot as plt
import networkx as nx

# Initializing Graph object
G1 = nx.Graph()
# Connecting nodes
G1.add_edge(1, 2)
G1.add_edge(1, 7)
G1.add_edge(2, 8)
G1.add_edge(2, 4)
G1.add_edge(3, 4)
G1.add_edge(3, 5)
G1.add_edge(4, 6)
G1.add_edge(5, 6)
G1.add_edge(5, 7)
G1.add_edge(7, 8)

# Explicit positions
pos1 = {
    1: (0, 0), 2: (0, 3),
    3: (1, 1), 4: (1, 2),
    5: (2, 1), 6: (2, 2),
    7: (3, 0), 8: (3, 3),
    }

# Graph's drawing options
options1 = {
    "font_size": 14,
    "node_size": 500,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G1, pos1, **options1)

#----------------------------------------------------
# Initializing Graph object
G2 = nx.Graph()
# Connecting nodes
G2.add_edge(1, 2)
G2.add_edge(1, 7)
G2.add_edge(2, 8)
G2.add_edge(2, 4)
G2.add_edge(3, 4)
G2.add_edge(3, 5)
G2.add_edge(4, 6)
G2.add_edge(5, 6)
G2.add_edge(6, 8)
G2.add_edge(7, 8)

# Explicit positions
pos2 = {
    1: (5, 0), 2: (5, 3),
    3: (6, 1), 4: (6, 2),
    5: (7, 1), 6: (7, 2),
    7: (8, 0), 8: (8, 3),
    }

# Graph's drawing options
options2 = {
    "font_size": 14,
    "node_size": 500,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G2, pos2, **options2)

# Printing Graph's important registers
print("Are isomorphic?", nx.is_isomorphic(G1, G2))

# Axis margin so nodes are not "cutted"
ax = plt.gca()
ax.margins(0.01)
plt.axis("off")
plt.show()