import networkx as nx

class Tarjan:
    """
    Implémentation classique de Tarjan
    """
    def __init__(self, G):
        self.G = G


    def has_num(self, node):
		return set([node]).issubset(self.num_of)

    def parcours(self, v):
        self.num_of[v] = self.num
        self.numAccessible[v] = self.num
        self.num += 1
        self.stack.append(v)

#		if verbose: print ("Debut de parcours, num = " + str(num))

        for son in self.G.successors(v):
            if not self.has_num(son):
                self.parcours(son)
                self.numAccessible[v] = min(self.numAccessible[v], self.numAccessible[son])
            elif son in self.stack:
                self.numAccessible[v] = min(self.numAccessible[v], self.num_of[son])

#		if verbose: print ("num = " + str(num) + " num_of = " + str(num_of[v]) + " numAccessible = " + str(numAccessible[v]))

        if self.numAccessible[v] == self.num_of[v]:
            self.addPartition(v)

    def addPartition(self, v):
        C = []
        p = None
        while p != v:
            p = self.stack.pop()
            C.append(p)
#			if verbose: print ("On ajoute partition de taille " + str(len(C)))
        self.partition.append(C)

    def init(self):
        self.num = 0
        self.stack = []
        self.partition = []

        self.num_of = {}
        self.numAccessible = {}

    def execute(self):
        self.init()
        for node in self.G.nodes():
            if not self.has_num(node): self.parcours(node)
    #		if verbose: print ("Fin de Parcours, num = " + str(num))

        return self.partition
