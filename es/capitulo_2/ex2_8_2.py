import matplotlib.pyplot as plt
import networkx as nx

def number_of_vertex(G):
    n = 0
    for x in G:
        n += x[1]
    return n

# Crea el grafo vacío con el objeto DiGraph, con seis nodos
G = nx.empty_graph(6, create_using=nx.Graph())

# Añadiendo aristas (con bucles)
G.add_edges_from([
    (2, 1),
    (3, 0),
    (4, 3), (4, 2), (4, 1),
    (5, 4), (5, 2), (5, 3), (5, 1), (5, 0)
])

# Dibujando el grafo
nx.draw(G, with_labels=True, arrows=True)

# Imprimir registros importantes del grafo
listGDeg = G.degree([0, 1, 2, 3, 4, 5])
print(f"Grados de cada nodo (con bucles): {listGDeg}")
print("Un corolario inmediato del lema del apretón de manos es que en cualquier gráfico el número de vértices de grado impar es par.")
print(f"Número de vertices: {number_of_vertex(listGDeg)}")
print(f"¿El número de vertices de grados impares es par?: {number_of_vertex(listGDeg) % 2 == 0}")
# Mostrar en pantalla el grafo
plt.show()
