import networkx as nx

def execute(digraph, partitions, nodes):
	reverse_partition = {}
	
	def to_string(partition):
		string = ""
		first = False
		for elem in partition:
			if not first: string += ", "
			else: first = True
			string += elem.mot
				

	condensed_digraph = nx.DiGraph()

	for i in range(0, len(partitions)):
		condensed_digraph.add_node(to_string(partitions[i]))
		for word in partitions[i]:
			reverse_partition[word.cle] = i
	
	print len(reverse_partition)	

	for key in reverse_partition.keys():
		for successor in digraph.successors(nodes[key]):
			condensed_digraph.add_edge(to_string(partitions[reverse_partition[key]]), to_string(partitions[reverse_partition[successor.cle]]))
