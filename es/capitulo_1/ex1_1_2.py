import matplotlib.pyplot as plt
import networkx as nx

def number_of_vertex(G):
    n = 0
    for x in G:
        n += x[1]
    return n

# Inicializa el objeto Graph
G = nx.Graph()
# Conectando los nodos
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(2, 5)
G.add_edge(4, 5)
G.add_edge(5, 6)

# Posiciones explícitas
pos = {1: (0, 1), 2: (0, 0), 3: (1, 1), 4: (1, 0), 5: (2, 1), 6: (2, 0)}

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

# Imprimir registros importantes del grafo
listGDeg = G.degree([1, 2, 3, 4, 5, 6])
print("Vertices totales:", number_of_vertex(listGDeg))
print("Aristas totales:", (G.number_of_edges()))
print("Nodos con sus grados:", listGDeg)

# Margenes para los ejes así los nodos no están cortados
ax = plt.gca()
ax.margins(0.1)
plt.axis("off")
plt.show()