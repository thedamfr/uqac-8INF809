class Mot:
    """
    Mot est le Modele representant un mot. Oui Oui !
    """
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