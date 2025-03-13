import matplotlib.pyplot as plt
import networkx as nx

# Creates Graph by filling it by 4 nodes, and with DiGraph object
G1 = nx.complete_graph(4)
# Adding planar layout to Graph
pos1 = nx.random_layout(G1)

# Drawing Graph
nx.draw(G1, pos1, with_labels=True)

# Creates Graph by filling it by 4 nodes, and with DiGraph object
G2 = nx.complete_graph(4)
# Adding planar layout to Graph
pos2 = nx.random_layout(G2)

# Drawing Graph
nx.draw(G2, pos2, with_labels=True)

# Printing Graph's important registers
print("Are isomorphic?", nx.is_isomorphic(G1, G2))
dh1 = nx.degree_histogram(G1)
dh2 = nx.degree_histogram(G2)
print("Have the same degree sequence?", dh1 == dh2)

# Shows Graph at screen
plt.show()