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
G.add_edge(2, 3)
G.add_edge(2, 5)
G.add_edge(4, 5)
G.add_edge(5, 6)

# Explicit positions
pos = {1: (0, 1), 2: (0, 0), 3: (1, 1), 4: (1, 0), 5: (2, 1), 6: (2, 0)}

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
listGDeg = G.degree([1, 2, 3, 4, 5, 6])
print("Total's vertex:", number_of_vertex(listGDeg))
print("Total's edges:", (G.number_of_edges()))
print("Degree's per node:", listGDeg)

# Margenes para los ejes así los nodos no están cortados
# Axis margin so nodes are not "cutted"
ax = plt.gca()
ax.margins(0.1)
plt.axis("off")
plt.show()