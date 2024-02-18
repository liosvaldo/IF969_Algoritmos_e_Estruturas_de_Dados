import networkx as nx
import matplotlib.pyplot as plt
from src import functions
import pandas as pd

if __name__ == '__main__':
    quantidade_utilizada = 120
    matrix_pesos = pd.read_csv('datasets/matriz_arestas.csv', index_col=[0])
    matrix_pesos.columns = matrix_pesos.index
    lista_vertices = pd.read_csv('datasets/lista_vertices.csv', index_col=[0])['0'].to_list()

    matrix_pesos_utilizada = matrix_pesos.iloc[:quantidade_utilizada, :quantidade_utilizada]
    g = nx.from_pandas_adjacency(matrix_pesos_utilizada)


    # Testes
    # adj = np.loadtxt('AdjMatrix.txt')
    # adj = np.loadtxt('exemplo.txt')

    # g = nx.from_numpy_array(adj)

    t, w = functions.prim(g, 0)

    grafico = nx.Graph()
    functions.cria_vertices(grafico, g.nodes)

    for i in range(len(t)):
        if t[i] != None:
            grafico.add_edge(i, t[i], weight=w[i])


    pos = nx.spring_layout(grafico)
    nx.draw_networkx_nodes(grafico, pos,
                           nodelist=grafico.nodes,
                           node_size=300,
                           node_color='r')
    nx.draw_networkx_edges(grafico, pos,
                           edgelist=nx.edges(grafico))

    layout = {}
    for node in grafico.nodes.keys():
        layout[node] = lista_vertices[node]

    nx.draw_networkx_labels(grafico, pos, layout, font_size=10)

    plt.axis('off')
    plt.savefig('Figure/saida.png')
    plt.show()