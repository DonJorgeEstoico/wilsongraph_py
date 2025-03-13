import matplotlib.pyplot as plt
import networkx as nx

def number_of_vertex(G):
    n = 0
    for x in G:
        n += x[1]
    return n

# Initializing Graph object
G = nx.Graph()
# Connecting nodes
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 1)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(4, 5)

# Explicit positions
pos = {1: (0, 0), 2: (0, 1), 3: (1, 0), 4: (1, 1), 5: (2, 0.5)}

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

# Printing Graph's important registers
listGDeg = G.degree([1, 2, 3, 4, 5])
print("Total's vertex:", number_of_vertex(listGDeg))
print("Total's edges:", (G.number_of_edges()))
print("Degree's per node:", listGDeg)

# Axis margin so nodes are not "cutted"
ax = plt.gca()
ax.margins(0.1)
plt.axis("off")
plt.show()