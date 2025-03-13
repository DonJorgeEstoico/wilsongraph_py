import matplotlib.pyplot as plt
import networkx as nx

# Inicializa el objeto Graph
G = nx.Graph()
# Conectando los nodos
G.add_edge(1, 2)
G.add_edge(2, 6)
G.add_edge(2, 5)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(4, 5)

# Posiciones explícitas
pos = {1: (0, 2), 2: (2, 2), 3: (4, 4), 4: (4, 0), 5: (6, 2), 6: (2, 0)}

# Opciones de dibujo del grafo
options = {
    "font_size": 24,
    "node_size": 2000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G, pos, **options)

# Margenes para los ejes así los nodos no están cortados
ax = plt.gca()
ax.margins(0.1)
plt.axis("off")
plt.show()