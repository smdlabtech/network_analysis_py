#!/usr/bin/env
##------------------------------------------------------------------------------------
##----------------------------- Web_Analitics project --------------------------------
import numpy as np
import community 
import pandas as pd
import itertools
import networkx as nx
import matplotlib.pyplot as plt
from pandas import read_excel
from toolz.itertoolz import last

##------------------ data1.gml -----------------------------
##1.1 Importation et Affichage des donnees
file="C:/Users/mamad/OneDrive/Documents/Data1/data1.gml"
G = nx.read_gml(file,label='id')
print(nx.info(G))
##Number of nodes: 40421
##Number of edges: 175692
##Average degree:   8.6931

##1.2 Calcul des Mesures de centralités et densité
print("__Degree centrality : ",nx.degree_centrality(G), "/n")
print("__Betweeness_centrality : ", nx.betweenness_centrality(G), "/n")
print("__Closeness_centrality : ", nx.closeness_centrality(G), "/n")
print("__Graph density : ", nx.density(G), "/n")    #densite:0.0002150693980491644

##print(nx.average_shortest_path_length(G))
##Puisque le graphe n'est pas un graphe connecté, on a de longueur moyenne de chemin

##1.3 Détection des communautés
def community_detection(g,k=1):
    comp = nx.algorithms.community.centrality.girvan_newman(g)
    for communities in itertools.islice(comp, k):
        community = tuple(sorted(c) for c in communities)
    return community

##Déterminer la meilleur partition possible de G
##partition = community.best_partition(G, weight='weight')
##print(partition)

##------------------------ data2.gml ---------------------------------
##2.1 Importation et Affichage des donnees
file="C:/Users/mamad/OneDrive/Documents/Data2/data2.gml"
G = nx.read_gml(file,label='id')
print(nx.info(G))
##Number of nodes: 1589 (Avec Noeuds de degree>=1 :1461 soit 91.94% de noeuds)
##Number of edges: 2742
##Average degree:   3.4512

##2.2 Calcul des Mesures de centralités et densité
print("__Degree centrality : ",nx.degree_centrality(G), "/n")
print("__Betweeness_centrality : ", nx.betweenness_centrality(G), "/n")
print("__Closeness_centrality : ", nx.closeness_centrality(G), "/n")
print("__Graph density : ", nx.density(G), "/n")    #densite:0.0021733168683312383

##2.3 Detection de community
def community_detection(g,k=1):
    comp = nx.algorithms.community.centrality.girvan_newman(g)
    for communities in itertools.islice(comp, k):
        community = tuple(sorted(c) for c in communities)
    return community

##2.4: Performence: lors du calcul, on s'arrete quand la performence cesse de croitre.
def community_detection_performance(g,k=1):
    comp = nx.algorithms.community.centrality.girvan_newman(g)
    for communities in itertools.islice(comp, k):
        per = nx.algorithms.community.quality.performance(g,communities)
    return per

##2.5 Analyse de chaque noeud et affichage du graphique
def analyse_node(g):
    shortestPath=nx.shortest_path(g)
    node_colors = ["red" if n in shortestPath else "green" for n in g.nodes()]
    pos = nx.spring_layout(g)
    nx.draw_networkx_nodes(g, pos=pos, node_color=node_colors)
    nx.draw_networkx_edges(g, pos=pos)
    ##print(shortestPath)
    return nx.draw(g)

##2.6: Degre de chaque noeud du graphe
def deg_node(g):            
    for s in g.degree():
        print(s)

##2.7: Afficher tous les noeud de degre >= 1 (A faire pour une l'analyse)

##2.8: Degre intra des noeud associé à la même communauté
def intra_deg(g,k=1):     
        comp = nx.algorithms.community.centrality.girvan_newman(g)
        #k = 1
        for communities in itertools.islice(comp, k):
            for community in communities:
                graph = nx.Graph.subgraph(g, community)
                degrees = list(graph.degree)
                for i in range(len(community)):
                    print(degrees[i])

##2.9 Noeuds ayant le plus de connexions
def highest_intra_deg(g,k=1): ##Highest_Intra: equipe ayant joue le max de match
    degrees = list(g.degree)
    val=[]
    for i in range(len(degrees)):
        val+=[degrees[i][1]]
        if degrees[i][1]==max(val):
            print(degrees[i])

##2.10 Noeud le plus populaire
def most_popular_nod(g):
    degrees = list(g.degree)
    node = degrees[0]
    for i in range(len(degrees)):
        if degrees[i][1] > node[1]:
            node = degrees[i]
    return node


##2.11: les noeuds les plus populaires parmi tous les noeuds
def most_popnod_among(g):
    #degre le plus eleve = equipe la plus populaire
    degrees = list(g.degree)
    val=[]
    for i in range(len(degrees)):
        val+=[degrees[i][1]]
        if degrees[i][1]==max(val):
            print(degrees[i])
            

if __name__=="__main__":

    ##--------- Analyse de la data1 ----------
    print("hello")
    print(community_detection(G,k=1))   ##detection des communautés

    ##--------- Analyse de la data2 ----------
    ##2.3 Detection de communauté
    print(community_detection(G,k=1))  
    ##Nous obtenons un total de 277 communautés (en enlevant tous les noeuds de deg 1)

    ##2.4 Performancce de l'algo de detection des communautés 
    for i in range(1,len(G)):
        print(community_detection_performance(G,k=i))
        if community_detection_performance(G,k=i)>community_detection_performance(G,k=i+1):
            break

    ##2.5 Analyse de chaque noeud et affichage des résultats
    print(analyse_node(G))
    plt.show()

    ##2.6 Degre de chaque noeud du graphe
    print(deg_node(G))

    ##2.8 Degre intra des noeud associé à la même communauté
    print(intra_deg(G))

    ##2.9 Noeuds ayant le plus de connexions
    print(highest_intra_deg(G,k=1))

    ##2.10 Noeud le plus populaire
    print(most_popular_nod(G))  ##(33, 34)

    ##2.11 Noeuds les plus populaires
    print(most_popnod_among(G))
    
    

























