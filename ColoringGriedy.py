import networkx as nx
import matplotlib.pyplot as plt

def coloring_griedy(G, num=None) -> dict:
    # Inicializa o dicionário de cores com indice -1 
    # O indice -1 indica que o nó ainda não foi colorido
    K = {v:-1 for v in G.nodes()} 
    
    # Se o número de cores for especificado, então
    # cria uma lista de cores com o número de cores especificado
    if num is not None:
        colors = [x for x in range(num)]
    # Se o número de cores não for especificado, então
    # cria uma lista de cores com 100 cores
    else:
        colors = [x for x in range(100)]

    for node in K:
        # Inicializa a lista de cores disponíveis
        # o indice i da lista indica se a cor i está disponível
        available = [True]*len(colors)

        # Para cada vizinho do nó, se ele já foi colorido, então
        # a cor dele não está disponível
        for neighbor in G.neighbors(node):
            if K[neighbor] != -1:
                available[K[neighbor]] = False

        # Atribui a menor cor disponível ao nó
        for color in range(len(colors)):
            if available[color]:
                K[node] = color
                break

        # Se não houver nenhuma cor disponível e o nó ainda não foi colorido
        # então não existe solução de coloração
        if all([n == False in available for n in available]):
            if K[node] == -1:
                return None
    # Retorna o dicionário de cores com a solução de coloração
    return K


def plot_graph(G, K):
    if K is None:
        print("Nenhuma solução de coloração encontrada.")
        return
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=[K[v] for v in G.nodes()], cmap=plt.cm.rainbow, node_size=500)
    plt.show()

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([(0,1), (1,3), (0,3), (1,2), (2,3), (1,5), (4,5), (4,7), (7,6), (5,6), (3,7)])
    M = {}
    for v in G.nodes():
        M[v] = "#b8b8b8"
    plot_graph(G, M)

    input()

    K = coloring_griedy(G,3)
    plot_graph(G, K)

    input()

    G.add_edges_from([(0,1), (0,2), (1,3), (0,3), (1,2), (2,3), (1,5), (4,5), (4,6), (4,7), (7,6), (5,6), (3,7)])
    M = {}
    for v in G.nodes():
        M[v] = "#b8b8b8"
    plot_graph(G, M)

    input()
    
    K = coloring_griedy(G,3)
    plot_graph(G, K)

    input()

    K = coloring_griedy(G)
    plot_graph(G, K)


