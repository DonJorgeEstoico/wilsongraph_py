import matplotlib.pyplot as plt
import networkx as nx

# Inicializa el objeto Graph
G1 = nx.Graph()
# Conectando los nodos
G1.add_edge(1, 2)
G1.add_edge(1, 7)
G1.add_edge(2, 8)
G1.add_edge(2, 4)
G1.add_edge(3, 4)
G1.add_edge(3, 5)
G1.add_edge(4, 6)
G1.add_edge(5, 6)
G1.add_edge(5, 7)
G1.add_edge(7, 8)

# Posiciones explícitas
pos1 = {
    1: (0, 0), 2: (0, 3),
    3: (1, 1), 4: (1, 2),
    5: (2, 1), 6: (2, 2),
    7: (3, 0), 8: (3, 3),
    }

# Opciones de dibujo del grafo
options1 = {
    "font_size": 14,
    "node_size": 500,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G1, pos1, **options1)

#----------------------------------------------------
# Inicializa el objeto Graph
G2 = nx.Graph()
# Conectando los nodos
G2.add_edge(1, 2)
G2.add_edge(1, 7)
G2.add_edge(2, 8)
G2.add_edge(2, 4)
G2.add_edge(3, 4)
G2.add_edge(3, 5)
G2.add_edge(4, 6)
G2.add_edge(5, 6)
G2.add_edge(6, 8)
G2.add_edge(7, 8)

# Posiciones explícitas
pos2 = {
    1: (5, 0), 2: (5, 3),
    3: (6, 1), 4: (6, 2),
    5: (7, 1), 6: (7, 2),
    7: (8, 0), 8: (8, 3),
    }

# Opciones de dibujo del grafo
options2 = {
    "font_size": 14,
    "node_size": 500,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G2, pos2, **options2)

# Imprimir registros importantes del grafo
print("¿Son isomorfos?", nx.is_isomorphic(G1, G2))

# Margenes para los ejes así los nodos no están cortados
ax = plt.gca()
ax.margins(0.01)
plt.axis("off")
plt.show()