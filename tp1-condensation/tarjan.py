import networkx as nx

def execute(G):
	num = 0
	stack = []
	partition = []
	
	num_of = {}
	numAccessible = {}

	def has_num(node):
		return set([node]).issubset(num_of)

	def parcours(v, num):
		num_of[v] = num
		numAccessible[v] = num
		num += 1
		stack.append(v)

		for son in G.successors(v):
			if not has_num(son):
				num = parcours(son, num)
				numAccessible[v] = min(numAccessible[v], numAccessible[son])
			elif son in stack:
				numAccessible[v] = min(numAccessible[v], num_of[son])
		

		if numAccessible[v] == num_of[v]:
			C = []
			p = stack.pop()
			while p != v:
				C.append(p)
				p = stack.pop()
			partition.append(C)
	
		return num		
	
	for node in G.nodes():
		if not has_num(node): num = parcours(node, num)

	return partition



