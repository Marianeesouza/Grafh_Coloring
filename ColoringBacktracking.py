import networkx as nx
import matplotlib.pyplot as plt

def ifSafe(v, c, G, color):
    for i in G.neighbors(v):
        if color[i] == c:
            return False
    return True

def coloring_backtracking(G, num=None) -> dict:
    K = {v:-1 for v in G.nodes()}
    if num is not None:
        colors = [x for x in range(num)]
    else:
        colors = [x for x in range(100)]

    if coloring_backtracking_util(G, K, colors, 0):
        return K
    else:
        return None
    
def coloring_backtracking_util(G, K, colors, v):
    if v == len(K):
        return True
    for c in colors:
        if ifSafe(v, c, G, K):
            K[v] = c
            if coloring_backtracking_util(G, K, colors, v+1):
                return True
            K[v] = -1
    return False


def plot_graph(G, K):
    pos = nx.spring_layout(G)
    if K is not None:
        nx.draw(G, pos, with_labels=True, node_color=[K[v] for v in G.nodes()], cmap=plt.cm.rainbow, node_size=500)
        plt.show()
    else:
        print("Nenhuma solução de coloração encontrada.")

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([(0,1), (0,2), (0,3), (2,3), (2,4), (3,4), (4,5)])
    K = coloring_backtracking(G,3)
    plot_graph(G, K)
    
