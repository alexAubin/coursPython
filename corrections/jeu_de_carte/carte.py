
class InvalidCardColor(Exception):
    pass

class InvalidCardValue(Exception):
    pass


class Carte:
    
    couleurs_valides = ["trefle", "carreau", "coeur", "pique"]
    valeurs_valides = list(range(1,11)) + ["valet", "dame", "roi"]
    
    def __init__(self, valeur, couleur):
        
        if valeur not in Carte.valeurs_valides:
            raise InvalidCardValue
        if couleur not in Carte.couleurs_valides:
            raise InvalidCardColor
        
        self.valeur = valeur
        self.couleur = couleur

    @property
    def points(self):
        
        return Carte.valeurs_valides.index(self.valeur) + 1
        

    def __repr__(self):
        
        return f"<Carte {self.valeur} de {self.couleur}>"
        
        
        
        