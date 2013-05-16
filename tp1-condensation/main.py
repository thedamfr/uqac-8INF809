# -*- coding: ISO-8859-1 -*-
import advanced_tarjan as at
import condense
import networkx as nx
import tarjan
import mot as m
import graphviz as gv
import sys
import sys, getopt

nodes = {}
digraph = nx.DiGraph()

inputFile='graphe.dig'
outputFile='condensed_graph.png'

# Cli

###############################
# o == option
# a == argument passed to the o
###############################
# Cache an error with try..except
# Note: options is the string of option letters that the script wants to recognize, with
# options that require an argument followed by a colon (':') i.e. -i fileName
#
try:
    myopts, args = getopt.getopt(sys.argv[1:],"i:o:")
except getopt.GetoptError as e:
    print (str(e))
    print("Usage: %s -i input -o output" % sys.argv[0])
    sys.exit(2)

for o, a in myopts:
    if o == '-i':
        inputFile=a
    elif o == '-o':
        outputFile=a

# Display input and output file name passed as the args
print ("Input file : %s and output file: %s" % (inputFile,outputFile) )


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
readInput(inputFile)

#Appliquer l'algorithme tarjan
partition = tarjan.Tarjan(digraph).execute()
partition_set = at.AdvancedTarjan(digraph).execute()
gv.makeDisjoinsetGraph(partition_set)

#Construire le graphe condense
condensedFromSet = condense.execute_disjoinSet(partition_set, digraph)

gv.printCondensedGraph(condensedFromSet,outputFile)
