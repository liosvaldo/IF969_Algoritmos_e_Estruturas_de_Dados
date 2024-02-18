import networkx as nx
import numpy as np

# create graph
# add nodes
def add_nodes(g, nodes):
  for i in range(len(nodes)):
    g.add_node(i, name=nodes[i])

# add edges
def add_edges(g, adj_matrix):
  v = nx.number_of_nodes(g)
  for i in range(v):
    for j in range(v):
      if i != j and adj_matrix[i][j] != 0.:
        g.add_edge(i, j, weight=adj_matrix[i][j])

# get min
def node_min(nodes, weight):
  value = float('inf')
  m = None
  for node in nodes:
    if weight[node] < value:
      value = weight[node]
      m = node

  return m

# prim
def prim(g, init):
  open_node = []
  closed_node = []

  w = [] # weight 
  t = [] # predecessor
  for n in g.node:
    w.append(float('inf'))
    t.append(None)

  w[init] = 0
  open_node.append(init)
  

  while len(open_node) != 0:
    n = node_min(open_node, w)
    open_node.remove(n)
    closed_node.append(n)

    for e in g.neighbors(n):
      if e not in closed_node and w[e] > g.edge[n][e]['weight']: 
        open_node.append(e)
        t[e] = n
        w[e] = g.edge[n][e]['weight']

  return t, w # return array of predecessors and weights
