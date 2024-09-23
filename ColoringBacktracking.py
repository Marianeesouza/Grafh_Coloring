import networkx as nx
import matplotlib.pyplot as plt

def coloring_backtracking(G, num=None) -> dict:
    # Inicializa o dicionário de cores com indice -1
    # O indice -1 indica que o nó ainda não foi colorido
    K = {v:-1 for v in G.nodes()}

    # Se o número de cores for especificado, então
    # cria uma lista de cores com o número de cores especificado
    if num is not None:
        colors = [x for x in range(num)]
    # Se o número de cores não for especificado, então
    else:
        colors = [x for x in range(100)]

    # Inicio da recursão
    if coloring_backtracking_util(G, K, colors, 0):
        return K
    else:
        return None
    
def coloring_backtracking_util(G, K, colors, v):
    # v é o indice do vértice atual
    # Se v for igual ao número de vértices, então
    # todos os vértices foram coloridos
    if v == len(K):
        return True
    
    # Para cada cor disponível, verifica se é segura
    for c in colors:
        if ifSafe(v, c, G, K):
            # Se a cor c for segura, então atribui a cor c ao vértice v
            K[v] = c
            
            # Chama a função recursivamente para o próximo vértice
            if coloring_backtracking_util(G, K, colors, v+1):
                return True
            
            # Se a chamada recursiva não retornar True, então
            # a cor c não é segura, então atribui -1 ao vértice v
            K[v] = -1

    # Se nenhuma cor for segura, então retorna False
    return False

def ifSafe(v, c, G, color):
    # Verifica se a cor c é segura para o vértice v, ou seja,
    # se a cor c não foi atribuída a nenhum vizinho de v
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
