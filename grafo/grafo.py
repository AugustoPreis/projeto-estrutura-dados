import networkx as nx
import matplotlib.pyplot as plt

grafo = nx.Graph()

num_nos = 20
predios = [f"Prédio {i + 1}" for i in range(num_nos)]
grafo.add_nodes_from(predios)

arestas = [
    ("Prédio 1", "Prédio 2", {'weight_dist': 50, 'weight_custo': 2000}),
    ("Prédio 1", "Prédio 3", {'weight_dist': 75, 'weight_custo': 2400}),
    ("Prédio 1", "Prédio 4", {'weight_dist': 40, 'weight_custo': 1600}),
    ("Prédio 2", "Prédio 3", {'weight_dist': 25, 'weight_custo': 1000}),
    ("Prédio 2", "Prédio 5", {'weight_dist': 60, 'weight_custo': 2200}),
    ("Prédio 3", "Prédio 6", {'weight_dist': 100, 'weight_custo': 3000}),
    ("Prédio 4", "Prédio 5", {'weight_dist': 90, 'weight_custo': 2800}),
    ("Prédio 4", "Prédio 7", {'weight_dist': 125, 'weight_custo': 3600}),
    ("Prédio 5", "Prédio 6", {'weight_dist': 35, 'weight_custo': 1400}),
    ("Prédio 5", "Prédio 8", {'weight_dist': 150, 'weight_custo': 4000}),
    ("Prédio 6", "Prédio 9", {'weight_dist': 110, 'weight_custo': 3200}),
    ("Prédio 7", "Prédio 8", {'weight_dist': 70, 'weight_custo': 2600}),
    ("Prédio 7", "Prédio 10", {'weight_dist': 80, 'weight_custo': 2800}),
    ("Prédio 8", "Prédio 9", {'weight_dist': 45, 'weight_custo': 1800}),
    ("Prédio 8", "Prédio 11", {'weight_dist': 100, 'weight_custo': 3000}),
    ("Prédio 9", "Prédio 12", {'weight_dist': 90, 'weight_custo': 2800}),
    ("Prédio 10", "Prédio 11", {'weight_dist': 60, 'weight_custo': 2200}),
    ("Prédio 10", "Prédio 13", {'weight_dist': 75, 'weight_custo': 2400}),
    ("Prédio 11", "Prédio 12", {'weight_dist': 125, 'weight_custo': 3600}),
    ("Prédio 11", "Prédio 14", {'weight_dist': 50, 'weight_custo': 2000}),
    ("Prédio 12", "Prédio 15", {'weight_dist': 100, 'weight_custo': 3000}),
    ("Prédio 13", "Prédio 14", {'weight_dist': 40, 'weight_custo': 1600}),
    ("Prédio 13", "Prédio 16", {'weight_dist': 110, 'weight_custo': 3200}),
    ("Prédio 14", "Prédio 15", {'weight_dist': 70, 'weight_custo': 2600}),
    ("Prédio 14", "Prédio 17", {'weight_dist': 50, 'weight_custo': 2000}),
    ("Prédio 15", "Prédio 18", {'weight_dist': 90, 'weight_custo': 2800}),
    ("Prédio 16", "Prédio 17", {'weight_dist': 60, 'weight_custo': 2200}),
    ("Prédio 16", "Prédio 19", {'weight_dist': 80, 'weight_custo': 2800}),
    ("Prédio 17", "Prédio 18", {'weight_dist': 50, 'weight_custo': 2000}),
    ("Prédio 17", "Prédio 20", {'weight_dist': 150, 'weight_custo': 4000}),
    ("Prédio 18", "Prédio 19", {'weight_dist': 100, 'weight_custo': 3000}),
    ("Prédio 19", "Prédio 20", {'weight_dist': 75, 'weight_custo': 2400}),
]

grafo.add_edges_from(arestas)

posicao = nx.spring_layout(grafo)
rotulos_dist = nx.get_edge_attributes(grafo, 'weight_dist')
rotulos_custo = nx.get_edge_attributes(grafo, 'weight_custo')

nx.draw_networkx_edge_labels(
    grafo, posicao, edge_labels=rotulos_dist, label_pos=0.3)
nx.draw_networkx_edge_labels(
    grafo, posicao, edge_labels=rotulos_custo, label_pos=0.7)

nx.draw(grafo, posicao, with_labels=True, font_weight='bold', node_size=700,
        node_color='skyblue', font_size=8, font_color='black', font_family='arial')

plt.show()
