import networkx as nx
import matplotlib.pyplot as plt

def coloring_griedy(G, num=None) -> dict:
    # inicializa o dicionário de cores com indice -1 
    # para mostrar que não foi colorido
    K = {v:-1 for v in G.nodes()} 
    
    # se num for None, então o número de cores é igual ao grau
    # do vértice de maior grau + 1
    if num is not None:
        colors = [x for x in range(num-1)]
    else:
        colors = [x for x in range(100)]

    for node in K:
        # inicializa a lista de cores disponíveis
        available = [True]*len(colors)
        for neighbor in G.neighbors(node):
            if K[neighbor] != -1:
                available[K[neighbor]] = False
        for color in range(len(colors)):
            if available[color]:
                K[node] = color
                break
    return K


def plot_graph(G, K):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=[K[v] for v in G.nodes()], cmap=plt.cm.rainbow, node_size=500)
    plt.show()

if __name__ == "__main__":
    G = nx.Graph()

    # v = str(input("Digite os vértices separados por vírgula: "))
    # v = v.split(',')
    # for i in v:
    #     G.add_node(i)
    #     a = str(input("A quais vértices o vértice " + i + " está conectado? "))
    #     a = a.split(',')
    #     for j in a:
    #         G.add_edge(i, j)
    # n = int(input("Digite o número de cores: "))
    # if n == 0:
    #     K = coloring_griedy(G)

    G.add_edges_from([(0,1), (0,2), (0,3), (2,3), (6,7), (5,7), (7,4), (2,4), (3,4), (4,5), (4,6), (5,6)])
    K = coloring_griedy(G,3)
    plot_graph(G, K)
