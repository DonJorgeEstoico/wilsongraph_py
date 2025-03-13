import matplotlib.pyplot as plt
import networkx as nx

# Inicializa el objeto MultiGraph
G = nx.MultiGraph()
# Conectando los nodos
G.add_edges_from([(1, 2), (2, 1)])
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)

# Posiciones explícitas
pos = {1: (0, 0), 2: (0, 2), 3: (2, 1), 4: (3, 1)}

# Opciones de dibujo del grafo
options = {
    "font_size": 24,
    "node_size": 2000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}

# Añadiendo etiquetas de aristas para el grafo
edge_labels = {edge: f"{i}" for i, edge in enumerate(G.edges(keys=True), start=1)}
nx.draw_networkx_nodes(G, pos, node_color = 'b', node_size = 250, alpha = 1)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# Margenes para los ejes así los nodos no están cortados
ax = plt.gca()
ax.margins(0.1)
plt.axis("off")
plt.show()