import matplotlib.pyplot as plt
import networkx as nx

def number_of_vertex(G):
    n = 0
    for x in G:
        n += x[1]
    return n

# Creates empty Graph with DiGraph object, with six nodes
G = nx.empty_graph(6, create_using=nx.Graph())

# Adding edges (with loops)
G.add_edges_from([
    (2, 1),
    (3, 0),
    (4, 3), (4, 2), (4, 1),
    (5, 4), (5, 2), (5, 3), (5, 1), (5, 0)
])

# Drawing Graph
nx.draw(G, with_labels=True, arrows=True)

# Printing Graph's important registers
listGDeg = G.degree([0, 1, 2, 3, 4, 5])
print(f"Nodes of each graph (with loops): {listGDeg}")
print("An imme- diate corollary of the handshaking lemma is that in any graph the number of vertices of odd degree is even.")
print(f"Total vertex: {number_of_vertex(listGDeg)}")
print(f"Vertex number of odd degree is even?: {number_of_vertex(listGDeg) % 2 == 0}")
# Shows Graph at screen
plt.show()