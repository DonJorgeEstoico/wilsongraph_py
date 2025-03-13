import networkx as nx

def number_of_vertex(G):
    n = 0
    for x in G:
        n += x[1]
    return n

def odd_degree(G):
    n = 0
    for x in G:
        if x[1] % 2 == 1:
            n += 1
    return n == len(G)

def even_vertices(n):
    return n % 2 == 0

def generate_all_graphs():    
    # Genera un arreglo de grafos
    all_graphs = []
    
    # Inicializa el objeto Graph
    G = nx.Graph()
    # Conectando los nodos
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    all_graphs.append(G)
    
    # Inicializa el objeto Graph
    G = nx.Graph()
    # Conectando los nodos
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    all_graphs.append(G)
    
    # Inicializa el objeto Graph
    G = nx.Graph()
    # Conectando los nodos
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    all_graphs.append(G)
    
    # Inicializa el objeto Graph
    G = nx.Graph()
    # Conectando los nodos
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    all_graphs.append(G)
    
    # Inicializa el objeto Graph
    G = nx.Graph()
    # Conectando los nodos
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    all_graphs.append(G)
    
    # Inicializa el objeto Graph
    G = nx.Graph()
    # Conectando los nodos
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    all_graphs.append(G)
    
    return all_graphs

graphs = generate_all_graphs()
# Posiciones explícitas
pos1 = {
    1: (0, 0), 2: (4, 0),
    3: (2, 1), 4: (2, 2)
    }
# Posiciones explícitas
pos2 = {
    1: (0, 0), 2: (0, 1),
    3: (0, 2), 4: (0, 3)
    }
# Posiciones explícitas
pos3 = {
    1: (0, 0), 2: (2, 0),
    3: (1, 1), 4: (1, 2)
    }
# Posiciones explícitas
pos4 = {
    1: (0, 0), 2: (1, 0),
    3: (0, 1), 4: (1, 1)
    }
# Posiciones explícitas
pos5 = {
    1: (0, 0), 2: (2, 0),
    3: (1, 1), 4: (1, 2)
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

plt.figure(figsize=(10, 6))
for i, G in enumerate(graphs[:min(len(graphs), 6)]):  # Muestra hasta 6 grafos
    # Enseña grafos por 2 filas, 3 columnas en pantalla
    plt.subplot(2, 3, i + 1)
    if i == 0:
        nx.draw(G, pos1, **options, with_labels=True)
    elif i == 1:
        nx.draw(G, pos2, **options, with_labels=True)
    elif i == 2:
        nx.draw(G, pos3, **options, with_labels=True)
    elif i == 5:
        nx.draw(G, pos5, **options, with_labels=True)
    else:
        nx.draw(G, pos4, **options, with_labels=True)
    plt.title(f"Grafo {i+1}")
    # Imprimir registros importantes del grafo
    listGDeg = G.degree([1, 2, 3, 4])
    print("-----------------------------")
    print(f"Grafo {i+1}")
    print(f"Grados de cada nodo: {listGDeg}")
    nv = number_of_vertex(listGDeg)
    print(f"Vertices totales: {nv}")
    od = odd_degree(listGDeg)
    print(f"¿El número de grados del grafo es impar? {od}")
    if od:
        print(f"¿El número de vertices de grados impar es par? {even_vertices(nv)}")
plt.tight_layout()
plt.show()