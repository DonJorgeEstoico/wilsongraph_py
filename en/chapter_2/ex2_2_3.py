import matplotlib.pyplot as plt
import networkx as nx

# Creates Graph by filling it by 4 nodes, and with DiGraph object
G = nx.complete_graph(4, create_using=nx.DiGraph)
# Adding planar layout to Graph
pos = nx.planar_layout(G)

# Drawing Graph
nx.draw(G, pos, with_labels=True)

# Adding extra edges meaning the "loop"
edgelist = [(3, 3)]
G.add_edges_from(edgelist)

# Drawing edges newly added with a specific format
nx.draw_networkx_edges(G, pos, edgelist=edgelist, arrowstyle="<|-", style="dashed")

# Show Graph at screen
plt.show()