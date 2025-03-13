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
    # Generate graphs array
    all_graphs = []
    
    # Initializing Graph object
    G = nx.Graph()
    # Connecting nodes
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    all_graphs.append(G)
    
    # Initializing Graph object
    G = nx.Graph()
    # Connecting nodes
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    all_graphs.append(G)
    
    # Initializing Graph object
    G = nx.Graph()
    # Connecting nodes
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    all_graphs.append(G)
    
    # Initializing Graph object
    G = nx.Graph()
    # Connecting nodes
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    all_graphs.append(G)
    
    # Initializing Graph object
    G = nx.Graph()
    # Connecting nodes
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    all_graphs.append(G)
    
    # Initializing Graph object
    G = nx.Graph()
    # Connecting nodes
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
# Explicit positions
pos1 = {
    1: (0, 0), 2: (4, 0),
    3: (2, 1), 4: (2, 2)
    }
# Explicit positions
pos2 = {
    1: (0, 0), 2: (0, 1),
    3: (0, 2), 4: (0, 3)
    }
# Explicit positions
pos3 = {
    1: (0, 0), 2: (2, 0),
    3: (1, 1), 4: (1, 2)
    }
# Explicit positions
pos4 = {
    1: (0, 0), 2: (1, 0),
    3: (0, 1), 4: (1, 1)
    }
# Explicit positions
pos5 = {
    1: (0, 0), 2: (2, 0),
    3: (1, 1), 4: (1, 2)
    }

# Graph's drawing options
options = {
    "font_size": 14,
    "node_size": 400,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
print(f"{len(graphs)} graphs were generated.")

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
for i, G in enumerate(graphs[:min(len(graphs), 6)]): # Showing to 6 graphs
    # Showing graphs per 2 rows, 3 columns at screen
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
    # Printing Graph's important registers
    listGDeg = G.degree([1, 2, 3, 4])
    print("-----------------------------")
    print(f"Graph {i+1}")
    print(f"Nodes each graph: {listGDeg}")
    nv = number_of_vertex(listGDeg)
    print(f"Total vertex: {nv}")
    od = odd_degree(listGDeg)
    print(f"Graph's degree number is odd? {od}")
    if od:
        print(f"Vertex number of odd degree is even? {even_vertices(nv)}")
plt.tight_layout()
plt.show()