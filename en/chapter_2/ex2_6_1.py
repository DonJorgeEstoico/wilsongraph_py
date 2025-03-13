import networkx as nx

def generate_all_graphs():    
    # Generate graphs array
    all_graphs = []
    
    # Initializing Graph object
    G = nx.Graph()
    # Connecting nodes
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    all_graphs.append(G)
    
    # Initializing Graph object
    G2 = nx.Graph()
    # Connecting nodes
    G2.add_edge(1, 3)
    G2.add_edge(2, 3)
    G2.add_edge(3, 4)
    G2.add_edge(4, 5)
    all_graphs.append(G2)
    
    return all_graphs

graphs = generate_all_graphs()
# Explicit positions
pos1 = {
    1: (0, 0), 2: (2, 0),
    3: (4, 0), 4: (4, 2),
    5: (6, 0)
    }
# Explicit positions
pos2 = {
    1: (0, 0), 2: (4, 0),
    3: (2, 2), 4: (2, 4),
    5: (2, 6)
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

# Printing Graph's important registers
print("Are isomorphic?", nx.is_isomorphic(graphs[0], graphs[1]))
plt.figure(figsize=(10, 6))
for i, G in enumerate(graphs[:min(len(graphs), 2)]):  # Showing to 2 graphs
    # Showing graphs per 1 row, 2 columns at screen
    plt.subplot(1, 2, i + 1)
    if i == 0:
        nx.draw(G, pos1, **options, with_labels=True)
    else:
        nx.draw(G, pos2, **options, with_labels=True)
    plt.title(f"Graph {i+1}")
plt.tight_layout()
plt.show()