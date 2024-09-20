import networkx as nx
import matplotlib.pyplot as plt

def coloring_backtracking(G, num=None) -> dict:
    # Inicializa o dicionário de cores com indice -1
    K = {v:-1 for v in G.nodes()}

    if num is not None:
        colors = [x for x in range(num)]
    else:
        colors = [x for x in range(100)]

    # Inicio da recursão
    if coloring_backtracking_util(G, K, colors, 0):
        return K
    else:
        return None
    
def coloring_backtracking_util(G, K, colors, v):
    # Se todos os vértices foram coloridos, então a solução foi encontrada
    if v == len(K):
        return True
    
    # Para cada cor disponível, verifica se é segura
    for c in colors:
        if ifSafe(v, c, G, K):
            K[v] = c
            if coloring_backtracking_util(G, K, colors, v+1):
                return True
            K[v] = -1
    return False

def ifSafe(v, c, G, color):
    # Verifica se a cor c é segura para o vértice v
    for i in G.neighbors(v):
        if color[i] == c:
            return False
    return True


def plot_graph(G, K, color=None):
    pos = nx.spring_layout(G)
    if K is not None:
        if color is not None:
            nx.draw(G, node_color = K, with_labels=True, node_size=500)
        else:
            nx.draw(G, pos, with_labels=True, node_color=[K[v] for v in G.nodes()], cmap=plt.cm.rainbow, node_size=500)
        plt.show()
    else:
        print("Nenhuma solução de coloração encontrada.")

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([(0,1), (1,3), (0,3), (1,2), (2,3), (1,5), (4,5), (4,7), (7,6), (5,6), (3,7)])
    M = {}
    for v in G.nodes():
        M[v] = "#b8b8b8"
    plot_graph(G, M)

    input()

    K = coloring_backtracking(G,3)
    plot_graph(G, K)

    input()

    G.add_edges_from([(0,1), (0,2), (1,3), (0,3), (1,2), (2,3), (1,5), (4,5), (4,6), (4,7), (7,6), (5,6), (3,7)])
    M = {}
    for v in G.nodes():
        M[v] = "#b8b8b8"
    plot_graph(G, M)

    input()

    K = coloring_backtracking(G,3)
    plot_graph(G, K)

    input()

    K = coloring_backtracking(G)
    plot_graph(G, K)
