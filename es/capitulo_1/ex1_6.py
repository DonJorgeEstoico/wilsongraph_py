import matplotlib.pyplot as plt
import networkx as nx

# Inicializa el objeto Graph
G = nx.Graph()
# Conecta los nodos
G.add_edge(2, 4)
G.add_edge(4, 1)
G.add_edge(1, 3)
G.add_edge(3, 5)

# Posiciones explícitas
pos = {1: (0, 0), 2: (0, 2), 3: (2, 0), 4: (2, 2), 5: (4, 2)}

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