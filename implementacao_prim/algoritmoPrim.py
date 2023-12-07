class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = []

    def adicionar_vertice(self, vertice):
        self.vertices.add(vertice)

    def adicionar_aresta(self, origem, destino, peso_distancia, peso_custo):
        self.arestas.append((origem, destino, peso_distancia, peso_custo))
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)

    def obter_arestas(self):
        return sorted(self.arestas, key=lambda x: x[2])

    def calcular_agm(self):
        agm = Grafo()
        vertice_inicial = list(self.vertices)[0]
        agm.adicionar_vertice(vertice_inicial)

        while len(agm.vertices) < len(self.vertices):
            arestas_possiveis = [aresta for aresta in self.arestas
                                 if ((aresta[0] in agm.vertices and aresta[1] not in agm.vertices) or
                                     (aresta[1] in agm.vertices and aresta[0] not in agm.vertices))]

            if not arestas_possiveis:
                break

            aresta_menor_peso = min(arestas_possiveis, key=lambda x: x[2])
            agm.adicionar_vertice(aresta_menor_peso[1])
            agm.adicionar_aresta(*aresta_menor_peso)

        return agm


grafo = Grafo()

num_nos = 20
predios = [f"Prédio {i + 1}" for i in range(num_nos)]
for predio in predios:
    grafo.adicionar_vertice(predio)

arestas = [
    ("Prédio 1", "Prédio 2", 50, 2000),
    ("Prédio 1", "Prédio 3", 75, 2400),
    ("Prédio 1", "Prédio 4", 40, 1600),
    ("Prédio 2", "Prédio 3", 25, 1000),
    ("Prédio 2", "Prédio 5", 60, 2200),
    ("Prédio 3", "Prédio 6", 100, 3000),
    ("Prédio 4", "Prédio 5", 90, 2800),
    ("Prédio 4", "Prédio 7", 125, 3600),
    ("Prédio 5", "Prédio 6", 35, 1400),
    ("Prédio 5", "Prédio 8", 150, 4000),
    ("Prédio 6", "Prédio 9", 110, 3200),
    ("Prédio 7", "Prédio 8", 70, 2600),
    ("Prédio 7", "Prédio 10", 80, 2800),
    ("Prédio 8", "Prédio 9", 45, 1800),
    ("Prédio 8", "Prédio 11", 100, 3000),
    ("Prédio 9", "Prédio 12", 90, 2800),
    ("Prédio 10", "Prédio 11", 60, 2200),
    ("Prédio 10", "Prédio 13", 75, 2400),
    ("Prédio 11", "Prédio 12", 125, 3600),
    ("Prédio 11", "Prédio 14", 50, 2000),
    ("Prédio 12", "Prédio 15", 100, 3000),
    ("Prédio 13", "Prédio 14", 40, 1600),
    ("Prédio 13", "Prédio 16", 110, 3200),
    ("Prédio 14", "Prédio 15", 70, 2600),
    ("Prédio 14", "Prédio 17", 50, 2000),
    ("Prédio 15", "Prédio 18", 90, 2800),
    ("Prédio 16", "Prédio 17", 60, 2200),
    ("Prédio 16", "Prédio 19", 80, 2800),
    ("Prédio 17", "Prédio 18", 50, 2000),
    ("Prédio 17", "Prédio 20", 150, 4000),
    ("Prédio 18", "Prédio 19", 100, 3000),
    ("Prédio 19", "Prédio 20", 75, 2400),
]

for aresta in arestas:
    grafo.adicionar_aresta(*aresta)

agm = grafo.calcular_agm()

print("Grafo Original:")
for aresta in grafo.obter_arestas():
    print(
        f"Aresta: {aresta[0]} - {aresta[1]}, Distância: {aresta[2]}, Custo: {aresta[3]}")

print("\nÁrvore Geradora Mínima:")
for aresta in agm.obter_arestas():
    print(
        f"Aresta: {aresta[0]} - {aresta[1]}, Distância: {aresta[2]}, Custo: {aresta[3]}")
