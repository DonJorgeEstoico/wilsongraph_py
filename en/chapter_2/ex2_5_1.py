import itertools
import networkx as nx

def generate_all_graphs(n):
    # Generates all vertex's even (possible edges)
    vertices = list(range(n))
    possible_edges = list(itertools.combinations(vertices, 2))
    
    # Total number of possible graphs
    total_graphs = 2 ** len(possible_edges)
    print(f"Total number of possible graphs for {n} vertex: {total_graphs}")
    
    # Generate all edges subgroups
    all_graphs = []
    # Generate all binary combinations to include or exclude every edge
    for edge_subset in itertools.product([0, 1], repeat=len(possible_edges)):
        # Creates Graph
        G = nx.Graph()
        # Adding vertex's even
        G.add_nodes_from(vertices)
        for edge, include in zip(possible_edges, edge_subset):
            if include: # If bit is 1, include edge
                G.add_edge(*edge)
        # Adding all created graphs
        all_graphs.append(G)
    
    return all_graphs

# Testing with n = 3
n = 3
graphs = generate_all_graphs(n)
print(f"{len(graphs)} graphs were generated.")

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
for i, G in enumerate(graphs[:min(len(graphs), 8)]): # Shows to 8 graphs
    # Showing graphs per 2 rows, 4 columns at screen
    plt.subplot(2, 4, i + 1)
    nx.draw(G, with_labels=True)
    plt.title(f"Graph {i+1}")
plt.tight_layout()
plt.show()
