# -*- coding: ISO-8859-1 -*-
## Ce fichier presente une interface sous forme de module
## et contient également une interface objet


# La methode makeSet cree un set
def makeSet(data):
    return DisjoinSet(data)

# La methode find renvoie la racine correspondant au noeud demandé
# Il s'agit d'une version améliorée. Elle applatit l'arbre pour améliorer
# les temps d'accès suivants
def find(x):
    # On remonte jusqu'au pere, en applatissant l'arbre recursivement
    if x.parent != x:
        x.parent = find(x.parent)
    # Vu qu'on a applit l'arbre, le pere est forcement la racine
    return x.parent

# La Methode Union rejoint deux sets sous la même racine
# Cette méthode est améliorée. Elle utilise la valeur du rang afin d'ajouter
# l'arbre le plus petit à la racine de l'arbre le plus grand
#
def union(x, y):
    xRoot = find(x)
    yRoot = find(y)
    if xRoot == yRoot:
        # Court-circuit : ils sont deja dans le meme set
        return
    if xRoot.rank < yRoot.rank:
        xRoot.parent = yRoot
    elif xRoot.rank > yRoot.rank:
        yRoot.parent = xRoot
    else:
        yRoot.parent = xRoot
        #On doit incrementer le rang de xRoot, vu qu'on sait qu'il a un enfant de plus maintenant
        xRoot.rank = xRoot.rank + 1

# La Classe DisjoinSet Wrappe l'objet data dans la structure DisjoinSet
# et offre une interface objet attendue
#
class DisjoinSet:

    def __init__(self, data):
        self.data = data
        self.parent = self
        self.rank = 0

    def makeSet(cls, data):
        return makeSet(data)
    
    makeSet = classmethod(makeSet)

    def find(self):
        return find(self)

    def union(self, y):
        union(self, y)

    def isRoot(self):
        return self.parent == self

    def __str__(self):
        return self.data.__str__()

    def __repr__(self):
        if self.isRoot():
            return "Root of class : " + self.__str__()
        else:
            return self.__str__() + " as elem of class of " + str(self.find())
  



