import matplotlib.pyplot as plt
import networkx as nx

# Inicializa el objeto Graph
G = nx.Graph()
# Conecta los nodos
G.add_edge(1, 2)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 6)
G.add_edge(6, 9)
G.add_edge(7, 9)
G.add_edge(8, 9)

# Posiciones explícitas
pos = {1: (0, 0), 2: (0, 1), 3: (1, 0), 4: (1, 1), 5: (2, 2), 6: (3, 1), 7: (4, 0), 8: (6, 0), 9: (5, 1)}

# Opciones de dibujo del grafo
options = {
    "font_size": 16,
    "node_size": 500,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G, pos, **options)

# Margenes para los ejes así los nodos no están cortados
ax = plt.gca()
ax.margins(0.01)
plt.axis("off")
plt.show()