import numpy as np
import pandas as pd
from geopy import distance
import networkx as nx
from pathlib import Path


total_utilizado = 120

pathfile = Path('../datasets/20220729_rede_saude_dados_abertos_versao_final.csv')
root_path = Path('../datasets/')
df_postos_saude_recife = pd.read_csv(pathfile, sep=';')

total_postos = df_postos_saude_recife.shape[0]


lista_vertices = df_postos_saude_recife['nome_oficial'].to_list()[:total_utilizado]
matriz_arestas = np.zeros((total_utilizado, total_utilizado), dtype=np.float64)


for posto_1 in np.arange(total_utilizado):
  print(posto_1)
  localizacao_1 = df_postos_saude_recife.loc[posto_1,['latitude', 'longitude']].to_list()
  nome_posto_1 = df_postos_saude_recife.loc[posto_1,'nome_oficial']
  if posto_1 == 120: break
  for posto_2 in np.arange(total_utilizado):
    localizacao_2 = df_postos_saude_recife.loc[posto_2,['latitude', 'longitude']].to_list()
    nome_posto_2 = df_postos_saude_recife.loc[posto_2,'nome_oficial']
    distancia_entre_postos = distance.distance(localizacao_1, localizacao_2).km
    if posto_2 == 120: break
    if (nome_posto_1 != nome_posto_2) and (distancia_entre_postos != 0.):
      print(f"{posto_1} {posto_2} A distancia entre: {nome_posto_1} e {nome_posto_2} é:{distancia_entre_postos}")
      matriz_arestas[posto_1, posto_2] = distancia_entre_postos

df_matriz_arestas = pd.DataFrame(matriz_arestas)
df_vertices = pd.DataFrame(lista_vertices)
df_matriz_arestas.to_csv(root_path.joinpath('matriz_arestas.csv'))
df_vertices.to_csv(root_path.joinpath('lista_vertices.csv'))