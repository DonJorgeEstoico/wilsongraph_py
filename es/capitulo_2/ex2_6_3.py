import networkx as nx

def generate_all_graphs():    
    # Genera un arreglo de grafos
    all_graphs = []
    
    # Inicializa el objeto Graph
    G = nx.Graph()
    # Conectando los nodos
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(1, 5)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(2, 5)
    G.add_edge(3, 4)
    G.add_edge(4, 5)
    all_graphs.append(G)
    
    # Inicializa el objeto Graph
    G = nx.Graph()
    # Conecta los nodos
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(2, 5)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    G.add_edge(4, 5)
    all_graphs.append(G)
    
    return all_graphs

graphs = generate_all_graphs()
# Posiciones explícitas
pos1 = {
    1: (0, 0), 2: (4, 0),
    3: (2, 0.5), 4: (2, 1), 5: (2, 1.5)
    }
# Posiciones explícitas
pos2 = {
    1: (0, 1.5), 2: (0.2, 0),
    3: (2, 2.3),
    4: (3.8, 0), 5: (4, 1.5),
    }

# Opciones de dibujo del grafo
options = {
    "font_size": 14,
    "node_size": 400,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
print(f"Se generaron {len(graphs)} grafos.")

import matplotlib.pyplot as plt

# Imprimir registros importantes del grafo
print("¿Son isomorfos?", nx.is_isomorphic(graphs[0], graphs[1]))
plt.figure(figsize=(10, 6))
for i, G in enumerate(graphs[:min(len(graphs), 2)]): # Muestra hasta 2 grafos
    # Enseña grafos por 1 fila, 2 columnas en pantalla
    plt.subplot(1, 2, i + 1)
    if i == 0:
        nx.draw(G, pos1, **options, with_labels=True)
    else:
        nx.draw(G, pos2, **options, with_labels=True)
    plt.title(f"Grafo {i+1}")
plt.tight_layout()
plt.show()