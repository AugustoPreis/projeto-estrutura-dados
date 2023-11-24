import random
import networkx as nx
import matplotlib.pyplot as plt

class CampusGraph:

  #Cria um grafo com os nós e arestas informados pelo usuário
  def __init__(self, nodes, edges):
    self.graph = nx.Graph()

    if (nodes > 0):
      self.graph.add_nodes_from(range(nodes))

    if (edges > 0):
      for _ in range(edges):
        node1 = random.randint(0, nodes - 1)
        node2 = random.randint(0, nodes - 1)

        while (node1 == node2 or self.graph.has_edge(node1, node2)):
          node2 = random.randint(0, nodes - 1)

        distance = random.randint(1, edges)
        cost = random.randint(edges, edges * 10)

        self.graph.add_edge(node1, node2, weight = distance, cost = cost)

  # Mostra o grafo em tela
  def draw(self):
    pos = nx.spring_layout(self.graph)

    nx.draw(
      self.graph,
      pos,
      with_labels = True,
      font_weight = 'bold',
      node_size = 700,
      node_color = 'skyblue',
      font_color = 'black',
    )
    labels = nx.get_edge_attributes(self.graph, 'weight')
    nx.draw_networkx_edge_labels(self.graph, pos, edge_labels = labels)
    plt.show()