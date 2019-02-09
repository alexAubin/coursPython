# Feuille d'exercice : les classes

## Jeu de carte

1.1 : Créer une classe `Carte`. Une carte dispose d'une `valeur` (1 à 10 puis J, Q et K) et d'une `couleur` (coeur, pique, careau, trèfle). Par exemple, on pourra créer des cartes en invoquant `Carte(3, 'coeur')` et `Carte('K', 'pique')`. Le constructeur doit valider que les données fournies sont valides.

1.2 : Implémenter la méthode `points` pour la classe `Carte`, qui retourne un nombre entre 1 et 13 en fonction de la valeur de la carte.

1.3 : Implémenter la méthode `__repr__` pour la classe `Carte`, de sorte à ce que `print(Carte(3, "coeur"))` affiche `<Carte 3 de coeur>`.

```python
c = Carte("Q", "pique")

print(c.couleur)
# Affiche pique

print(c.points)
# Affiche 12

print(c)
# Affiche <Carte Q de pique>
```

1.4 : Créer une classe `Paquet` correspondant à un paquet de 52 cartes. Le constructeur devra créer toute les cartes du jeu et les stocker dans une liste ordonnée.

1.5 : Implémenter la méthode `melanger` pour la classe `Paquet` qui mélange l'ordre des cartes.

1.6 : Implémenter la méthode `couper` qui prends un nombre aléatoire du dessus du paquet et les place en dessous.

1.7 : Implémenter la méthode `piocher` qui retourne la `Carte` du dessus du paquet (et l'enlève du paquet)

1.8 : Implémenter la méthode `distribuer` qui prends en argument un nombre de carte et un nombre de joueur (e.g. `p.distribuer(joueurs=4, cartes=5)`), pioche des cartes pour chacun des joueurs à tour de rôle, et retourne les mains correspondantes.


```python
p = Paquet()
p.melanger()

main_alice, main_bob = p.distribuer(joueurs=2, cartes=3)

print(main_alice)
# affiche par exemple [<Carte 3 de pique>, <Carte J de carreau>, <Carte 1 de trefle>]

print(p.pioche())
# affiche <Carte 9 de carreau>

print(main_alice[1].points())
# affiche 11
```

