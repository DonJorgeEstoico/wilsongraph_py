import itertools
import networkx as nx

def generate_all_graphs(n):
    # Genera todos los pares de vértices (posibles aristas)
    vertices = list(range(n))
    possible_edges = list(itertools.combinations(vertices, 2))
    print(f"Aristas posibles en nodos: {possible_edges}")
    print(f"Aristas posibles en nodos: {len(possible_edges)}")
    
    # Número total de grafos posibles
    total_graphs = 2 ** len(possible_edges)
    print(f"Número total de grafos posibles para {n} vértices: {total_graphs}")
    
    # Genera todos los subconjuntos de aristas
    all_graphs = []
    # Genera todas las combinaciones binarias para incluir o excluir cada arista
    for edge_subset in itertools.product([0, 1], repeat=len(possible_edges)):
        # Crear el grafo
        G = nx.Graph()
        # Añade los pares de vértices
        G.add_nodes_from(vertices)
        for edge, include in zip(possible_edges, edge_subset):
            if include:  # Si el bit es 1, incluir la arista
                G.add_edge(*edge)
        # Añadiendo todos los grafos creados
        all_graphs.append(G)
    
    return all_graphs

# Prueba con n = 3
n = 3
graphs = generate_all_graphs(n)
print(f"Se generaron {len(graphs)} grafos.")

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
for i, G in enumerate(graphs[:min(len(graphs), 2)]): # Enseña hasta 2 grafos
    # Enseña grafos por 1 fila, 2 columnas en pantalla
    plt.subplot(1, 2, i + 1)
    nx.draw(G, with_labels=True)
    plt.title(f"Grafo {i+1}")
plt.tight_layout()
plt.show()
