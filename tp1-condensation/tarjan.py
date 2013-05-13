import networkx as nx

def execute(G):
#	verbose = True
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
		
#		if verbose: print ("Debut de parcours, num = " + str(num))

		for son in G.successors(v):
			if not has_num(son):
				num = parcours(son, num)
				numAccessible[v] = min(numAccessible[v], numAccessible[son])
			elif son in stack:
				numAccessible[v] = min(numAccessible[v], num_of[son])
		
#		if verbose: print ("num = " + str(num) + " num_of = " + str(num_of[v]) + " numAccessible = " + str(numAccessible[v]))

		if numAccessible[v] == num_of[v]:
			C = []
			p = None
			while p != v:
				p = stack.pop()
				C.append(p)
#			if verbose: print ("On ajoute partition de taille " + str(len(C)))
			partition.append(C)
	
		return num		
	
	for node in G.nodes():
		if not has_num(node): num = parcours(node, num)
#		if verbose: print ("Fin de Parcours, num = " + str(num))

	return partition



