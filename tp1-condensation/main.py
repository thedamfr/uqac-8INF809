# -*- coding: ISO-8859-1 -*-
import advanced_tarjan as at
import condense
import networkx as nx
import tarjan
import mot as m
import graphviz as gv

nodes = {}
digraph = nx.DiGraph()

# Fonctions

def readInput(path="graphe.dig"):
    """
    Lire le fichier précisé
    Defaut : "graphe.dig"
    """
    inputFile = open(path, "r")
    # Lire le nombre de sommets
    nodeNumber = int(inputFile.readline().split()[0])
    print ("Number Of Nodes : " + str(nodeNumber))


    # Lire les sommets
    i = 0
    for ligne in inputFile:
        i += 1				# Compter les sommets

        split1 = ligne.split(":")
        key = int(split1[0])
        numero = split1[2]

        split2 = split1[1].split("|")
        mot = split2[0]
        racine = split2[1]
        categorie = split2[2]

        mMot = m.Mot(key, mot, racine, categorie, numero)
        nodes[key] = mMot
        digraph.add_node(mMot)

        if i >= nodeNumber: break

    for ligne in inputFile:
        splited = ligne.split("->")
        digraph.add_edge(nodes[int(splited[0])], nodes[int(splited[1])])

    inputFile.close()

#Lire le fichier
readInput()

#Appliquer l'algorithme tarjan
partition = tarjan.Tarjan(digraph).execute()
partition_set = at.AdvancedTarjan(digraph).execute()
gv.makeDisjoinsetGraph(partition_set)

#Construire le graphe condense
condensedFromSet = condense.execute_disjoinSet(partition_set, digraph)

gv.printCondensedGraph(condensedFromSet)
