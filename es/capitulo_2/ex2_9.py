import matplotlib.pyplot as plt
import networkx as nx

def same_degree(degree_list):
    # Extraer solo los grados de los nodos (segundo elemento de cada tupla)
    degrees = [deg for _, deg in degree_list]
    return all(deg == degrees[0] for deg in degrees) # Verificar si todos son iguales

# Crea el grafo con completarlo de a 2, 6 nodos, y con el objeto DiGraph
G = nx.full_rary_tree(2, 6)
# Se le añade un layout spring al grafo
pos = nx.spring_layout(G)

# Dibujando el grafo
nx.draw(G, pos, with_labels=True, node_color="lightblue", edgecolors="lightgreen", node_size=800)

# Imprimir registros importantes del grafo
listGDeg = list(G.degree())  # Convertir a lista explícitamente
print(f"Grados de cada nodo: {listGDeg}")
print("¿Tienen la misma secuencia de grados?", same_degree(listGDeg))

# Mostrar en pantalla el grafo
plt.show()