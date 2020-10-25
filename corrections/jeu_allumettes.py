

def afficher_allumettes(n):
    assert isinstance(n, int)
    assert n > 0
    
    print("Il y a %s allumettes sur la table:" % n)
    print("    " + "|"*n)
    

def choisir_nombre(nb_allumettes_restantes):
    
    while True:
        
        n = input("Combien prendre d'allumettes ? ")
        try:
            n = int(n)
            assert n >= 1
            assert n <= 3
            assert n <= nb_allumettes_restantes
        except:
            print("Ce n'est pas un choix valide !")
            continue
        
        return n


def partie_allumettes():
    
    nb_allumettes_restantes = 30
    tour = 1
    
    while nb_allumettes_restantes >= 1:
        
        print("C'est le tour du joueur %s" % tour)
        
        afficher_allumettes(nb_allumettes_restantes)
        choix = choisir_nombre(nb_allumettes_restantes)
        nb_allumettes_restantes -= choix
        
        if nb_allumettes_restantes < 1:
            print("Le joueur %s a perdu !" % tour)
        
        if tour == 1:
            tour = 2
        else:
            tour = 1
            
partie_allumettes()
        

