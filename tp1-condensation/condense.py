
import networkx as nx
from collections import namedtuple

def execute_digraph(digraph, partitions, nodes):
	reverse_partition = {}
	
	def to_string(partition):
		string = ""
		first = True
		for elem in partition:
			if not first: string += ", "
			else: first = False
			string += elem.mot
		return string
				

	condensed_digraph = nx.DiGraph()

	for i in range(0, len(partitions)):
		condensed_digraph.add_node(to_string(partitions[i]))
		for word in partitions[i]:
			reverse_partition[word.cle] = i
	

	for key in reverse_partition.keys():
		for successor in digraph.successors(nodes[key]):
			if reverse_partition[key] != reverse_partition[successor.cle]:
				condensed_digraph.add_edge(to_string(partitions[reverse_partition[key]]), to_string(partitions[reverse_partition[successor.cle]]))

	return condensed_digraph


def execute_disjoinSet(disjointSet, digraph):
    """
    Construit le graphe condense a partir des disjointSets
    """
    condensed_digraph = nx.DiGraph()

    dicoNodeForRootElem = {}

    # On rassemble les set sous formes de listes
    for set in disjointSet.values():
        p = set.find()
        if dicoNodeForRootElem.get(p) == None:
            dicoNodeForRootElem[p] = []
        dicoNodeForRootElem[p].append(set.data)


    # On transforme les listes en tuples
    for key in dicoNodeForRootElem.keys():
        tup = tuple(dicoNodeForRootElem[key])
        condensed_digraph.add_node(tup)
        dicoNodeForRootElem[key] = tup

    # On transposes les edges
    for node in disjointSet.keys():
        for successor in digraph.successors(node):
            if disjointSet[node].find() != disjointSet[successor].find():
                condensed_digraph.add_edge(dicoNodeForRootElem[disjointSet[node].find()], dicoNodeForRootElem[disjointSet[successor].find()])

    return condensed_digraph




