import matplotlib.pyplot as plt
import networkx as nx

# Graph's carbon molecules number
def number_of_carbonate(pos):
    n = 0
    for x in pos:
        # Sum each at the time if nodes are not carbon
        if pos[x][0] == pos[x][1]:
            n += 1
    return n

# Graph's hydrogen molecules number
def number_of_hydrogen(pos):
    n = 0
    for x in pos:
        # Sum each at the time if nodes are not hydrogen
        if pos[x][0] != pos[x][1]:
            n += 1
    return n

# Initializing Graph object
G = nx.Graph()
# Connecting nodes
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(1, 5)

# Explicit positions
pos = {1: (1, 1), 2: (0, 1), 3: (1, 0), 4: (1, 2), 5: (2, 1)}

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
print(f'C, {number_of_carbonate(pos)}, H, {number_of_hydrogen(pos)}')

# Axis margin so nodes are not "cutted"
ax = plt.gca()
ax.margins(0.1)
plt.axis("off")
plt.show()