from carte import Carte


import random

class Paquet:
    
    def __init__(self):
        
        self.cartes = []
        for valeur in Carte.valeurs_valides:
            for couleur in Carte.couleurs_valides:
                c = Carte(valeur, couleur)
                self.cartes.append(c)
                
    def __repr__(self):
        
        return str(self.cartes)
    
    def melanger(self):
        
        random.shuffle(self.cartes)
        
    def couper(self):
        
        coupe_index = random.randint(0, len(self.cartes))

        self.cartes = self.cartes[coupe_index:] + self.cartes[:coupe_index]


    def piocher(self):
        
        pioche = self.cartes[0]
        self.cartes = self.cartes[1:]
        
        return pioche
    
    def distribuer(self, nb_joueurs, nb_cartes):
        
        distribution = [ [] for i in range(0, nb_joueurs)]
        
        for i in range(0, nb_joueurs):
            for j in range(0, nb_cartes):
                carte = self.piocher()
                distribution[i].append(carte)
                
        return distribution
        
    

