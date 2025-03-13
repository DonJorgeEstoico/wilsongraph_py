import matplotlib.pyplot as plt
import networkx as nx

# Initializing Graph object
G1 = nx.Graph()
# Connecting nodes
G1.add_edge(1, 2)
G1.add_edge(1, 3)
G1.add_edge(1, 6)
G1.add_edge(2, 9)
G1.add_edge(2, 4)
G1.add_edge(3, 8)
G1.add_edge(3, 7)
G1.add_edge(4, 5)
G1.add_edge(4, 8)
G1.add_edge(5, 6)
G1.add_edge(5, 7)
G1.add_edge(6, 10)
G1.add_edge(7, 9)
G1.add_edge(8, 10)
G1.add_edge(9, 10)

# Explicit positions
pos1 = {
    1: (1.5, 1.8), 2: (2, 0),
    3: (2.2, 1.4), 4: (2.5, 0.4),
    5: (3, 2), 6: (3, 2.8),
    7: (3.5, 0.4), 8: (3.8, 1.4),
    9: (4, 0), 10: (4.5, 1.8)
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
G2.add_edge(1, 3)
G2.add_edge(1, 6)
G2.add_edge(2, 7)
G2.add_edge(2, 8)
G2.add_edge(3, 4)
G2.add_edge(3, 9)
G2.add_edge(4, 5)
G2.add_edge(4, 8)
G2.add_edge(5, 7)
G2.add_edge(6, 10)
G2.add_edge(7, 9)
G2.add_edge(8, 10)
G2.add_edge(9, 10)

# Explicit positions
pos2 = { #x:5-9.5,y:0-2
    1: (5, 1.4), 
    2: (5.5, 3), 3: (5.5, 0), 
    4: (6, 2),
    5: (7, 1.7), 6: (7, 1), 
    7: (8, 2),
    8: (8.5, 3), 9: (8.5, 0), 
    10: (9, 1.4), 
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
print("G1 edges:", sorted(G1.edges()))
print("G2 edges:", sorted(G2.edges()))

# Axis margin so nodes are not "cutted"
ax = plt.gca()
ax.margins(0.01)
plt.axis("off")
plt.show()