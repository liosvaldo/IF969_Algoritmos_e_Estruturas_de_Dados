import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scripts

# read name of airport

# nodes 

# adjacency matrix
adj = np.loadtxt('AdjMatrix.txt')
g = nx.from_numpy_matrix(adj)


# prim 
t, w = scripts.prim(g, 0)

mst = nx.Graph()
scripts.add_nodes(mst, g.node.values())

# g.v == grafico.v
for i in range(len(t)):
  if t[i] != None:
    mst.add_edge(i, t[i], weight=w[i])

#a,b =  grafico.edges()[0]
#print grafico.edge[a]

#for e in grafico.edges():
#  a, b = e
#  print grafico.edge[a][b]['weight']

# generate community
#TODO: how cut edges (?)

def max_edge(g):
    weight = 0
    for e in g.edges():
        if g.edge[e[0]][e[1]]['weight'] > weight:
            a = e[0]
            b = e[1]
            weight = g.edge[e[0]][e[1]]['weight']
    g.edge[a][b]['weight'] = 0
    return a, b


def generate_community_k(g, k):
    comm = g.copy()
    for i in range(k-1):
        u, v = max_edge(comm) 
        comm.remove_edge(u,v)
    return comm

k2_comm = generate_community_k(mst, 2)
#k5_comm = generate_community_k(grafico, 5)


pos = nx.spring_layout(k2_comm)
nx.draw_networkx_nodes(k2_comm, pos,
                       nodelist=k2_comm.node,
                       node_size=300,
                       node_color='r')
nx.draw_networkx_edges(k2_comm, pos,
                       edgelist=nx.edges(k2_comm))

layout = {}
for node in k2_comm.node.keys():
    layout[node] = str(node)

nx.draw_networkx_labels(k2_comm,pos,layout,font_size=10)

plt.axis('off')
plt.savefig('k2.png')
plt.show()
