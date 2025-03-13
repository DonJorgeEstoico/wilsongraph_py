import matplotlib.pyplot as plt
import networkx as nx

# Número de moléculas de carbono en el grafo
def number_of_carbonate(pos):
    n = 0
    for x in pos:
        # Sumar uno cada vez si los nodos no son de carbono
        if pos[x][0] == pos[x][1]:
            n += 1
    return n

# Número de moléculas de hidrógeno en el grafo
def number_of_hydrogen(pos):
    n = 0
    for x in pos:
        # Sumar uno cada vez si los nodos no son de hidrógeno
        if pos[x][0] != pos[x][1]:
            n += 1
    return n

# Inicializa el objeto Graph
G = nx.Graph()
# Conectando los nodos
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(1, 5)

# Posiciones explícitas
pos = {1: (1, 1), 2: (0, 1), 3: (1, 0), 4: (1, 2), 5: (2, 1)}

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
print(f'C, {number_of_carbonate(pos)}, H, {number_of_hydrogen(pos)}')

# Margenes para los ejes así los nodos no están cortados
ax = plt.gca()
ax.margins(0.1)
plt.axis("off")
plt.show()