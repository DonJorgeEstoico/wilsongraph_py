import matplotlib.pyplot as plt
import networkx as nx

def degree_sum(G1, G2):
    return sum(G1) == sum(G2)

# Creates Graph by filling it by 6 nodes, and with DiGraph object
G1 = nx.cycle_graph(6)
# Adding spring layout to Graph
pos1 = nx.spring_layout(G1)
# Drawing Graph
nx.draw(G1, pos1, with_labels=True, node_color="white", edgecolors="black", node_size=800)

# Creates Graph by filling it by 2, 6 nodes, and with DiGraph object
G2 = nx.full_rary_tree(2, 6)
# Adding spring layout to Graph
pos2 = nx.spring_layout(G2)
# Drawing Graph
nx.draw(G2, pos2, with_labels=True, node_color="lightblue", edgecolors="lightgreen", node_size=800)

# Printing Graph's important registers
print("Have the same degree sequence?", degree_sum(G1, G2))
print("Are isomorphic?", nx.is_isomorphic(G1, G2))

# Shows Graph at screen
plt.show()