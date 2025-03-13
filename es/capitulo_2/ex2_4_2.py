import matplotlib.pyplot as plt
import networkx as nx

def degree_sum(G1, G2):
    return sum(G1) == sum(G2)

# Crea el grafo con completarlo de a 6 nodos, y con el objeto DiGraph
G1 = nx.cycle_graph(6)
# Se le añade un layout spring al grafo
pos1 = nx.spring_layout(G1)

# Dibujando el grafo
nx.draw(G1, pos1, with_labels=True, node_color="white", edgecolors="black", node_size=800)

# Crea el grafo con completarlo de a 2, 6 nodos, y con el objeto DiGraph
G2 = nx.full_rary_tree(2, 6)
# Se le añade un layout spring al grafo
pos2 = nx.spring_layout(G2)

# Dibujando el grafo
nx.draw(G2, pos2, with_labels=True, node_color="lightblue", edgecolors="lightgreen", node_size=800)

# Imprimir registros importantes del grafo
print("¿Tienen la misma secuencia de grados?", degree_sum(G1, G2))
print("¿Son isomorfos?", nx.is_isomorphic(G1, G2))

# Mostrar en pantalla el grafo
plt.show()