from carte import Carte

c1 = Carte(3, "pique")
c2 = Carte("dame", "coeur")

print(c1)
print(c1.points)

print(c2)
print(c2.points)

#############################

from paquet import Paquet

P = Paquet()

print("\nAvant coupe\n")
print(P)

P.couper()


print("\nApres coupe\n")
print(P)

P.melanger()

print("\nApres melange\n")
print(P)


print(f"Actuellement il y a {len(P.cartes)} cartes dans le paquet")
print(P.piocher())
print(P.piocher())
print(f"Actuellement il y a {len(P.cartes)} cartes dans le paquet")

cartes_alice, cartes_bob = P.distribuer(nb_joueurs=2, nb_cartes=5)
print(cartes_alice)
print(cartes_bob)








        
    