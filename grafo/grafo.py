import networkx as nx
import matplotlib.pyplot as plt

# Crie um grafo
grafo = nx.Graph()

# Adicione pelo menos 20 nós representando prédios
num_nos = 20
predios = [f"Prédio {i + 1}" for i in range(num_nos)]
grafo.add_nodes_from(predios)

# Adicione arestas com pesos (distâncias e custos de instalação)
arestas = [
    ("Prédio 1", "Prédio 2", {'weight_dist': 10, 'weight_custo': 100}),
    ("Prédio 1", "Prédio 3", {'weight_dist': 15, 'weight_custo': 120}),
    ("Prédio 1", "Prédio 4", {'weight_dist': 8, 'weight_custo': 80}),
    ("Prédio 2", "Prédio 3", {'weight_dist': 5, 'weight_custo': 50}),
    ("Prédio 2", "Prédio 5", {'weight_dist': 12, 'weight_custo': 110}),
    ("Prédio 3", "Prédio 6", {'weight_dist': 20, 'weight_custo': 150}),
    ("Prédio 4", "Prédio 5", {'weight_dist': 18, 'weight_custo': 140}),
    ("Prédio 4", "Prédio 7", {'weight_dist': 25, 'weight_custo': 180}),
    ("Prédio 5", "Prédio 6", {'weight_dist': 7, 'weight_custo': 70}),
    ("Prédio 5", "Prédio 8", {'weight_dist': 30, 'weight_custo': 200}),
    ("Prédio 6", "Prédio 9", {'weight_dist': 22, 'weight_custo': 160}),
    ("Prédio 7", "Prédio 8", {'weight_dist': 14, 'weight_custo': 130}),
    ("Prédio 7", "Prédio 10", {'weight_dist': 16, 'weight_custo': 140}),
    ("Prédio 8", "Prédio 9", {'weight_dist': 9, 'weight_custo': 90}),
    ("Prédio 8", "Prédio 11", {'weight_dist': 20, 'weight_custo': 150}),
    ("Prédio 9", "Prédio 12", {'weight_dist': 18, 'weight_custo': 140}),
    ("Prédio 10", "Prédio 11", {'weight_dist': 12, 'weight_custo': 110}),
    ("Prédio 10", "Prédio 13", {'weight_dist': 15, 'weight_custo': 120}),
    ("Prédio 11", "Prédio 12", {'weight_dist': 25, 'weight_custo': 180}),
    ("Prédio 11", "Prédio 14", {'weight_dist': 10, 'weight_custo': 100}),
    ("Prédio 12", "Prédio 15", {'weight_dist': 20, 'weight_custo': 150}),
    ("Prédio 13", "Prédio 14", {'weight_dist': 8, 'weight_custo': 80}),
    ("Prédio 13", "Prédio 16", {'weight_dist': 22, 'weight_custo': 160}),
    ("Prédio 14", "Prédio 15", {'weight_dist': 14, 'weight_custo': 130}),
    ("Prédio 14", "Prédio 17", {'weight_dist': 10, 'weight_custo': 100}),
    ("Prédio 15", "Prédio 18", {'weight_dist': 18, 'weight_custo': 140}),
    ("Prédio 16", "Prédio 17", {'weight_dist': 12, 'weight_custo': 110}),
    ("Prédio 16", "Prédio 19", {'weight_dist': 16, 'weight_custo': 140}),
    ("Prédio 17", "Prédio 18", {'weight_dist': 10, 'weight_custo': 100}),
    ("Prédio 17", "Prédio 20", {'weight_dist': 30, 'weight_custo': 200}),
    ("Prédio 18", "Prédio 19", {'weight_dist': 20, 'weight_custo': 150}),
    ("Prédio 19", "Prédio 20", {'weight_dist': 15, 'weight_custo': 120}),
]

grafo.add_edges_from(arestas)

# Desenhe o grafo
posicao = nx.spring_layout(grafo)
rotulos_dist = nx.get_edge_attributes(grafo, 'weight_dist')
rotulos_custo = nx.get_edge_attributes(grafo, 'weight_custo')

nx.draw_networkx_edge_labels(grafo, posicao, edge_labels=rotulos_dist, label_pos=0.3)
nx.draw_networkx_edge_labels(grafo, posicao, edge_labels=rotulos_custo, label_pos=0.7)

nx.draw(grafo, posicao, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black', font_family='arial')

# Exiba o gráfico
plt.show()
