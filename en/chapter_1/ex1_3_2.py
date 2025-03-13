import matplotlib.pyplot as plt
import networkx as nx

# Graph's carbon molecules number
def number_of_carbonate(G):
    n = 0
    for x in G:
        # Sum each at the time if nodes are not carbon
        if x[1] == 4:
            n += 1
    return n

# Graph's hydrogen molecules number
def number_of_hydrogen(G):
    n = 0
    for x in G:
        # Sum each at the time if nodes are not hydrogen
        if x[1] == 1:
            n += 1
    return n

# Initializing Graph object
G = nx.Graph()
# Connecting nodes
G.add_edge(1, 2)
G.add_edge(1, 4)
G.add_edge(1, 6)
G.add_edge(1, 9)
G.add_edge(2, 3)
G.add_edge(2, 7)
G.add_edge(2, 10)
G.add_edge(3, 5)
G.add_edge(3, 8)
G.add_edge(3, 11)

# Explicit positions
pos = {
        1: (1, 1), 2: (2, 1), 3: (3, 1), 4: (0, 1), 5: (4, 1), 
        6: (1, 0), 7: (2, 0), 8: (3, 0),
        9: (1, 2), 10: (2, 2), 11: (3, 2),
    }

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
listGDeg = G.degree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(f'C, {number_of_carbonate(listGDeg)}, H, {number_of_hydrogen(listGDeg)}')

# Axis margin so nodes are not "cutted"
ax = plt.gca()
ax.margins(0.1)
plt.axis("off")
plt.show()