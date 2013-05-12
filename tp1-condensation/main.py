from collections import namedtuple
import networkx as nx
import pydot


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
	key = split1[0]
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
	digraph.add_edge(int(splited[0]), int(splited[1]))	

inputFile.close()

graph = pydot.Dot(graph_type='digraph')

for node in digraph.nodes():
	graph.add_node(pydot.Node(str(node)))
for edge in digraph.edges():
	graph.add_edge(pydot.Edge(edge[0], edge[1]))
