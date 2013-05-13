import AdvancedTarjan
import condense
import networkx as nx
import pydot
import tarjan

def makeDisjoinsetGraph(partition_set):
    graphviz = pydot.Dot(graph_type='digraph')

    for n in partition_set.values():
        graphviz.add_node(pydot.Node(str(n.data)))

    for n in partition_set.values():
        graphviz.add_edge(pydot.Edge(pydot.Node(str(n.data)), pydot.Node(str(n.parent.data))))

    graphviz.write_png('disjoinset_graph.png')

def tupleToString(tuple):
    string = ""
    first = True
    for i in range(0, len(tuple) % 10):
        if tuple[i] != None:
            if first: first = False
            else: string += ", "
            string += str(tuple[i])

    if len(tuple) > 10:
        string += " and " + str(len(tuple)-1) + " others"
    return string

class Mot:
    def __init__(self, cle, mot, racine, categorie, numero):
        self.cle = cle
        self.mot = mot
        self.racine = racine
        self.categorie = categorie
        self.numero = numero

    def __str__(self):
        return str(self.mot)

    def __repr__(self):
        return " < Mot : " + str(self) + ">"


inputFile = open("graphe.dig", "r")

nodes = {}

digraph = nx.DiGraph()

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

    motMot = Mot(key, mot, racine, categorie, numero)
    nodes[key] = motMot
    digraph.add_node(motMot)

    if i >= nodeNumber: break

for ligne in inputFile:
	splited = ligne.split("->")
	digraph.add_edge(nodes[int(splited[0])], nodes[int(splited[1])])	

inputFile.close()

#Appliquer l'algorithme tarjan
partition = tarjan.Tarjan(digraph).execute()
partition_set = AdvancedTarjan.AdvancedTarjan(digraph).execute()
makeDisjoinsetGraph(partition_set)

#Construire le graphe condense
condensedFromSet = condense.execute_disjoinSet(partition_set, digraph)

graphviz = pydot.Dot(graph_type='digraph')
graphviz_nodes = {}

for n in condensedFromSet.nodes():
    print_node = pydot.Node(tupleToString(n))
    print (tupleToString(n))
    graphviz.add_node(print_node)
    graphviz_nodes[n] = print_node


for e in condensedFromSet.edges():
    graphviz.add_edge(pydot.Edge(graphviz_nodes[e[0]], graphviz_nodes[e[1]]))

graphviz.write_png('condensed_graph.png')
