import matplotlib.pyplot as plt
import networkx as nx

# Crea el grafo con completarlo de a 4 nodos, y con el objeto DiGraph
G = nx.complete_graph(4, create_using=nx.DiGraph)
# Se le añade un layout plano al grafo
pos = nx.planar_layout(G)

# Dibujando el grafo
nx.draw(G, pos, with_labels=True)

# Añadimos las aristas extras siendo el bucle
edgelist = [(3, 3)]
G.add_edges_from(edgelist)

# Dibujando las aristas recién añadidas con un formato específico
nx.draw_networkx_edges(G, pos, edgelist=edgelist, arrowstyle="<|-", style="dashed")

# Mostrar en pantalla el grafo
plt.show()