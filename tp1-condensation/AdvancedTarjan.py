from disjoin_set import DisjoinSet
import tarjan as super
import disjoin_set as ds

class AdvancedTarjan(super.Tarjan):

    def init(self):
        self.num = 0
        self.stack = []
        self.partition = {}

        self.num_of = {}
        self.numAccessible = {}

    def addPartition(self, v):
        poped = self.stack.pop()
        C = ds.DisjoinSet.makeSet(poped)
        self.partition[poped] = C
        while poped != v:
            poped = self.stack.pop()
            disjoinset = ds.DisjoinSet(poped)
            C.union(disjoinset)
            #			if verbose: print ("On ajoute partition de taille " + str(len(C)))
            self.partition[poped] = disjoinset