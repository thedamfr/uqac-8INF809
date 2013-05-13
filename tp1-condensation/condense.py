import networkx as nx

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
