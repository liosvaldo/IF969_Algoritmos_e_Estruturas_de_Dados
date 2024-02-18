import numpy as np
import pandas as pd
import networkx as nx
from pathlib import Path

def cria_vertices(g, lista_vertices):
    for i in range(len(lista_vertices)):
        g.add_node(i, name=lista_vertices[i])


def cria_arestas(g, matriz_pesos):
    v = nx.number_of_nodes(g)
    for i in range(v):
        for j in range(v):
            if i != j and matriz_pesos[i][j] != 0.:
                g.add_edge(i, j, weight=matriz_pesos[i][j])


def menor_vertice(lista_vertices, w):
    value = float('inf')
    mini = None
    for vertice in lista_vertices:
        if w[vertice] < value:
            value = w[vertice]
            mini = vertice
    return mini


def prim(g, inicio):
    vertices_avaliados = []
    vertices_salvos = []

    pesos = []
    predecessores = []

    for n in g.nodes:
        pesos.append(float('inf'))
        predecessores.append(None)

    pesos[inicio] = 0
    vertices_avaliados.append(inicio)

    while len(vertices_avaliados) != 0:

        min = menor_vertice(vertices_avaliados, pesos)
        vertices_avaliados.remove(min)
        vertices_salvos.append(min)

        for vizinho in g.neighbors(min):
            if vizinho not in vertices_salvos and pesos[vizinho] > \
                    g.adj[min][vizinho]['weight']:
                vertices_avaliados.append(vizinho)
                predecessores[vizinho] = min
                pesos[vizinho] = g.adj[min][vizinho]['weight']

    return predecessores, pesos

def max_edge(g):
    weight = 0
    for e in g.adj:
        if e[0][1]['weight'] > weight:
            a = e[0]
            b = e[1]
            weight = e[0][1]['weight']
    g.adj[a][b]['weight'] = 0
    return a, b


def generate_community_k(g, k):
    comm = g.copy()
    for i in range(k-1):
        u, v = max_edge(comm)
        comm.remove_edge(u , v)
    return comm

