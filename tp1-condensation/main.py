from collections import namedtuple
import networkx as nx
import pydot
import tarjan


inputFile = open("graphe.dig", "r")

Node = namedtuple("Node", "cle mot racine categorie numero")

nodes = {}

digraph = nx.DiGraph()

# Lire le nombre de sommets
edgeNumber = int(inputFile.readline().split()[0])
print ("Number Of Nodes : " + str(edgeNumber))


# Lire les sommets
i=0
for ligne in inputFile:
	i += 1				# Compter les sommets

	split1 = ligne.split(":")	
	key = int(split1[0])
	numero = split1[2]

	split2 = split1[1].split("|")
	mot = split2[0]
	racine = split2[1]
	categorie = split2[2]

	nodes[key] = Node(key, mot, racine, categorie, numero)

	digraph.add_node(nodes[key])

	if i >= edgeNumber : break

for ligne in inputFile:
	splited = ligne.split("->")
	digraph.add_edge(nodes[int(splited[0])], nodes[int(splited[1])])	

inputFile.close()

#Appliquer l'algorithme tarjan
partition = tarjan.execute(digraph)

#Construire le graphe condensé
condense
