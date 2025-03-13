import matplotlib.pyplot as plt
import networkx as nx

# Crea el grafo con completarlo de a 4 nodos, y con el objeto DiGraph
G1 = nx.complete_graph(4)
# Se le añade un layout plano al grafo
pos1 = nx.random_layout(G1)

# Dibujando el grafo
nx.draw(G1, pos1, with_labels=True)

# Crea el grafo con completarlo de a 4 nodos, y con el objeto DiGraph
G2 = nx.complete_graph(4)
# Se le añade un layout plano al grafo
pos2 = nx.random_layout(G2)

# Dibujando el grafo
nx.draw(G2, pos2, with_labels=True)

# Imprimir registros importantes del grafo
print("¿Son isomorfos?", nx.is_isomorphic(G1, G2))
dh1 = nx.degree_histogram(G1)
dh2 = nx.degree_histogram(G2)
print("¿Tienen la misma secuencia de grados?", dh1 == dh2)

# Mostrar en pantalla el grafo
plt.show()