title: Python : avancé
class: animation-fade
layout: true

<!-- This slide will serve as the base layout for all your slides -->
<!--
.bottom-bar[
  {{title}}
]
-->

---

class: impact

# Python "avancé"

- Utiliser, créer ses propres modules python
- Librairies communes : `os`, `logging`
- Bonnes pratiques de dev : conventions, PEP8, Black, MyPy
- Debugging avec pdb / ipdb
- Multiprocess, multithreading



---

class: impact

# Modules python : utilisation, création

---

# Modules python : utilisation, création

## `pip`

- Gestionnaire de paquet / modules Python
- PIP : "Pip Install Packages"
- PyPI : Python Package Index
- Installer un paquet :
    - `pip3 install <paquet>`
- Rechercher un paquet :
    - `pip3 search <motclef>`
- Installer une liste de dépendances :
    - `pip3 install -r requirements.txt`
- Lister les paquets installés
    - `pip3 list`, `pip3 freeze`

---

# Modules python : utilisation, création

## `pip`

- Les paquets Pythons sont installés dans `/usr/lib/python*/dist-packages/`

---

## Ecrire ses propres modules

Considérant les fichiers suivants :

```bash
├── main.py
└── mylib/
    ├── __init__.py
    └── bonjour.py      # <-- Contient "def dire_bonjour..."
```

Depuis `main.py`, je peux faire

```python
from mylib.bonjour import dire_bonjour

dire_bonjour("Alex") # -> "Bonjour Alex !"

print(dire_bonjour)
# -> <function dire_bonjour at 0x7fb964fab668>
```


---

## Ecrire ses propres modules

Considérant les fichiers suivants :

```bash
├── main.py
└── mylib/
    ├── __init__.py
    └── bonjour.py      # <-- Contient "def dire_bonjour..."
```

Depuis `main.py`, je peux *aussi* faire

```python
from mylib import bonjour

bonjour.dire_bonjour("Alex") # -> "Bonjour Alex !"

print(bonjour)
# -> <module 'mylib.bonjour' from 'mylib/bonjour.pyc'>
```

---

## Ecrire ses propres modules

Considérant les fichiers suivants :

```bash
├── main.py
└── mylib/
    ├── __init__.py
    └── bonjour.py      # <-- Contient "def dire_bonjour..."
```

Attention : si j'ai du code dans le contexte 'global' de `bonjour.py` (comme par exemple des `print()` ou des tests de la fonction), le code sera executé au moment de l'import (donc les `print()` apparaîtront dans la console etc...)

Il existe tout de même une astuce qui consiste à êcrire:

```python
if __name__ == "__main__":
    # Ici, du code qui ne sera executé *QUE* si je lance `python3 bonjour.py`
    # directement (pas lors de l'import)

    # Test dire_bonjour
    dire_bonjour("Alex")
```

---

## Ecrire ses propres modules

Situation de la vraie vie, un site de vente en ligne : on a pleins de structures différentes à gérer, on les organise dans un dossier `models/`:

```text
├── app.py
└── models/
    ├── __init__.py
    ├── user.py
    ├── product.py
    ├── order.py
    └── invoice.py
└── views/
    ├── landpage.html
    ├── catalog.html
    └── checkout.html
└── assets/
    └── logo.png
```

---

## Un "vrai" module (installable par d'autres gens)

- Étape 1 : écrire un fichier 'setup.py' à la racine de mon projet, qui contient les métadonnées de mon module

```bash
└── mylib/
    ├── __init__.py
    └── bonjour.py      
└─ setup.py
```

```python
from setuptools import setup

setup(
   name='mylib',
   version='1.0',
   license="MIT",
   description='Un super module avec des utilitaires pour dire bonjour',
   author='Alex',
   author_email='aleks@whatever.tld',
   packages=['mylib'],
   install_requires=['wheel', 'requests'], # Dépendances nécessaires pour ce paquet
)
```

---

## Un "vrai" module (installable par d'autres gens)

- Étape 1.5 : Tester d'installer le module sur son propre système

```bash
python3 setup.py install
```

On devrait voir:

```text
copying build/lib/bonjour/bonjour.py -> build/bdist.linux-x86_64/egg/bonjour
[...]
byte-compiling build/bdist.linux-x86_64/egg/bonjour/bonjour.py to bonjour.cpython-39.pyc
[...]
Copying bonjour-1.0-py3.9.egg to /usr/local/lib/python3.9/dist-packages

Installed /usr/local/lib/python3.9/dist-packages/bonjour-1.0-py3.9.egg
[...]
```

Et ensuite, n'importe où sur le système je devrais pouvoir faire:

```python
from mylib.bonjour import dire_bonjour
dire_bonjour("Alex")
```

---

## Un "vrai" module (installable par d'autres gens)

- Étape 2 : Envoyer le paquet sur les serveurs de Pypi.org
- *(pour tester, on peut utiliser plutôt TestPyPI / test.pypi.org)*
- Il faut créer un compte: https://test.pypi.org/account/register/
- Vérifier que le nom de la librairie qu'on veut créer n'existe pas déjà
- Installer `twine` sur machine (petit utilitaire pour uploader sur pypi)
- Uploader : `twine upload --repository testpypi dist/*`
- ... attendre quelques minutes ...
- Tester l'install avec : `pip install --index-url https://test.pypi.org/simple/ your-package`









---

class: impact

## Librairie `logging` et `os`




---

# Librairie `logging`

### Pourquoi une librairie pour le logging plutot que juste `print`

- Différent niveaux de message : `debug`, `info`, `warning`, `error`, `critical`(?)
- Possibilité de logger les infos dans un fichier (ou virtuellement n'importe quoi)
   - on est pas forcément "devant" le terminal dans lequel le programme se lance
   - recherche plus facile dans un fichier lorsqu'on a un grand volume de message
- Suivi de l'heure à laquelle un message a été émis
- Suivi de quelle partie du code (ou fichier) a émis le message
- ...

De plus, la librairie `logging` est une sorte de standard de-facto utilisé par plein de librairie, et fourni un fonctionnement unifié que l'on peut personnaliser ensuite.

---

# Librairie `logging`

### Fonctionnement de base

```python
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')

logging.info("Le programme vient de se lancer")
for i in range(10):
    logging.debug(f"La valeur de i vaut {i}")

logging.warning("Oh non c'est la fin du programme!")
```

```
2022-11-03 23:42:47,887 : root : INFO : Le programme vient de se lancer
2022-11-03 23:42:47,887 : root : WARNING : Oh non c'est la fin du programme!
```

---

# Librairie `logging`

### Fonctionnement avancé

```python
import logging
import logging.handlers
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

# Definir le 'handler' qui va vers le fichier + son style de formattage
file_handler = logging.handlers.RotatingFileHandler('programme.log')
formatter    = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
file_handler.setFormatter(formatter)

# Ajouter le handler qui va vers le fichier + aussi celui vers la console
logger.addHandler(file_handler)
logger.addHandler(logging.StreamHandler())

logger.info("Le programme vient de se lancer")
for i in range(10):
    logger.debug(f"La valeur de i vaut {i}")
logger.warning("Oh non c'est la fin du programme!")
```

---

# Librairie `logging`

### Éléments de fonctionnement

- Les **logger** : c'est l'objet qui permet d'émettre les messages avec `logger.info()`, `.warning()`, etc.
    - Pour la tracabilité, on en créer un différent dans chaque fichier de code avec `logger = logging.getLogger(__name__)`
- Les **handler** : ce sont les destinations des messages, typiquement console ou fichier
- Les **formatter** : c'est la façon dont sont écrit les messages dans le log
- Les **filter** : (pas illustré) ce sont des mécaniques pour ne garder que certains messages

---

# Librairie `logging`

### Logger les exceptions

- Les méthodes `logger.info()`, `.warning()`, `.error()`, etc. loggent juste un message
- Il existe une méthode spéciale `logger.exception()` qui *en plus* logge la stacktrace de la dernière exception qui s'est produite (mais sans redéclencher l'erreur ni faire crasher le programme)

```python
try:
    int("trois")
except:
    logger.exception("Une exception s'est produite")
```

```
Une exception s'est produite
Traceback (most recent call last):
  File "/home/alex/dev/coursPython/sandbox/log/main.py", line 23, in <module>
    int("trois")
ValueError: invalid literal for int() with base 10: 'trois'
```

---

# Librairie `os`

Il s'agit de pleins de petites fonction utilitaire pour interagir avec l'OS : le système de fichier, les variables d'environnement, lancer des commandes "brutes", ...

Ces fonctionnalités sont rendues "portables" autant que possible et sont censées s'adapter au système de fichier sur lequel on exécute 

---

# Librairie `os`

### Créer/supprimer/gérer les permissions/voir les métadonnées

- `os.mkdir(chemin)` :  créer un dossier
- `os.remove(chemin)` : supprimer un fichier
- `os.chown`/`os.chmod` : permet de changer le propriétaire / les permissions d'un fichier
- `os.stat(chemin)` : retourne les métadonnées d'un fichier
    - par ex.: `os.stat("/var/log/kern.log")`
    - renvoie: `os.stat_result(st_mode=33184, st_ino=3160118, st_dev=65025, st_nlink=1, st_uid=0, st_gid=4, st_size=106455, st_atime=1667689202, st_mtime=1667923564, st_ctime=1667923564)`
    - par ex. `st_mtime` est la date / timestamp de dernière modification

---

# Librairie `os`

### Naviguer dans les fichiers

- `os.path.listdir(dossier)` : retourne la liste des fichiers et sous-dossiers dans `dossier`
- `os.walk(dossier)` : génère les noms de fichiers récursivement dans `dossier`
- `os.path.isfile(chemin)` : teste si `chemin` corresponds à un fichier
- `os.path.isdir(chemin)` : teste si `chemin` correponds à un dossier
- `os.path.join('/home', 'alex', 'Documents')` : construit un chemin complet 'intelligement' à partir des différents morceaux fournis, dans ce cas : `/home/alex/Documents`

et aussi une autre librairie cool: `glob`
- `glob.glob(/home/alex/*.py)` : permet d'itérer sur tous les fichiers qui finissent par `.py` dans mon dossier perso

---

# Librairie `os`

### Variables d'environnement

- `os.environ` : retourne un dictionnaire avec les variables d'environnement passées au script
   - par ex.: `os.environ["USER"]` vaut `alex`
   - ou encore: `os.environ["HOME"]` vaut `/home/alex`

---


# Librairie `os`

### Executer des commandes "brutes"

- `code_de_retour = os.system("ls /home/alex")` : 
    - execute la commande et affiche le résultat dans le terminal
    - renvoie **le code de retour** de la commande (NB: la sortie de la commande est uniquement dans le terminal, elle n'est pas renvoyée, on obtient seulement le code de retour!)
    - ATTENTION aux injections ! Par ex. `os.system("ls /home/alex/" + fichier)` avec `fichier` qui serait une information fournie par l'utilisateur créé un gros problème de sécurité.

Pour un mécanisme plus sécurisé et puissant, voir la librairie `subprocess`:

```python
out = subprocess.check_output(["echo", "Hello World!"])
print(out)    # -> Affiche 'Hello World'
```

- `subprocess.check_output(...)` : recupère la sortie d'une commande
- `subprocess.check_call(...)` : verifie que la commande a bien marché (code de retour '0') ou declenche une exception
- `subprocess.Popen(...)` : méthode plus bas niveau où on a un contrôle très fin






---

class: impact

# Conventions, linter, bonnes pratiques

---

# Conventions, linter, bonnes pratiques

## Faire du "bon code"

.center[
**La lisibilité est la priorité numéro 1**
]

Un programme est vivant et évolue. Mieux vaut un programme cassé mais lisible (donc débuggable) qu'un programme qui marche mais incompréhensible (donc fragile et/ou qu'on ne saura pas faire évoluer)

>“You primarily write your code to communicate with other coders, and, to a lesser extent, to impose your will on the computer.”
>   — Guido van Rossum

 <br/>

>"Maintainable code is more important than clever code"
>   — Guido van Rossum

https://blog.dropbox.com/topics/company/thank-you--guido 


---

# Conventions, linter, bonnes pratiques

## Lisibilité, "bon code"

- **Keep It Simple**
- **Sémantique** : utiliser des noms de variables et de fonctions concis et pertinents
- **Commentaires** : *lorsque c'est nécessaire*, pour démystifier ce qu'il se passe
- **Modularité** : découper son programme en fonctions qui chacune résolvent un sous-problème
- **Couplage faible** : garder ses fonctions autant que possibles indépendantes, limiter les effets de bords
- **Prendre le temps de refactoriser** quand nécessaire
    - si je répète plusieurs fois les mémes opérations, peut-être définir une nouvelle fonction
    - si le contenu d'une variable ou d'une fonction change, peut-être changer son nom
- **Ne pas abuser** des principes précédents
    - trop d'abstractions tue l'abstraction
    - tout ça viens avec le temps et l'expérience
    - à un moment c'est "good enough" et on passe à autre chose

---

# Conventions, linter, bonnes pratiques

## Lisibilité, "bon code"

[How to write good code](https://xkcd.lapin.org/strips/844Code%20correct.png)

---

# Conventions, linter, bonnes pratiques

## Conventions de nommages des variables, fonctions et classes

Variables et fonctions en snake case : `nom_de_ma_variable`

Constantes globales en macro case: `NOM_DE_MA_CONSTANTE`

Nom de classes en upper camel case : `NomDeMaClasse`

---

# Conventions, linter, bonnes pratiques

## Les docstrings

Un commentaire multiligne placé directement après le prototype(?) de la fonction, et qui peut être plus tard lu avec `help(ma_fonction)`

```python
def ma_fonction(arg1, arg2):
    """
    Ici je documente ce que fait ma fonction : 
    ses arguments, son retour, son comportement
    """

    # et ici le vrai code de la fonction
```

---

# Conventions, linter, bonnes pratiques

## Des commentaires utiles ... ou pas

- Un commentaire qui se contente de paraphrase le code est inutile
- La meilleure documentation commence par nommer de manière adéquate ses variables et fonctions

![](img/thisisastopsign.png)

---

# Conventions, linter, bonnes pratiques

## Syntaxe, PEP8, linters

- Le style d'écriture de python est standardisé via la norme PEP8
- Il existe des "linter" pour détecter le non-respect des conventions (et également certaines erreurs logiques)
    - Par exemple `flake8`, `pylint`
- Intégration possible dans `vim` et autres IDE...
- `autopep8` ou `black` permettent de corriger un bon nombre de problème automatiquement

---

# Conventions, linter, bonnes pratiques

## Black

![](img/black.png)

"The Uncompromising Code Formatter"

- Formattage automatique de votre code Python, PEP8-compatible
- L'idée est de laisser Black s'occuper du formattage du code pour **oublier la forme et vous concentrer sur le fond**
- Utilisation avec `pip3 install black` puis `black fichier_ou_dossier`
- À automatiser dans vos chaînes de développement (par ex. pre-commit hook, pull request automatique, ...)

---

# Conventions, linter, bonnes pratiques

## Type hints (Python typé ... sort of)

- Depuis Python 3.5 (puis amélioré dans les versions suivantes)
- ***Annotations** de types: **ignorées au runtime** !
- À voir comme des commentaires formalisés
- Utilisé par des outils d'analyse statique de code pour vérifier la cohérence
- Optionnel (on peut l'utiliser un peu sur quelques endroits du code, pas forcément partout)

```python
# Prends en argument un dictionnaire d'app,
# et renvoie une liste de nom d'app qui ont un level >= M
def at_least_level(apps: Dict[str, Dict], N: int) -> List[str]:

    L: List[str] = []
    for app, infos in apps.items():
        if infos["level"] >= N:
            L.append(L)
    return L
```

---

# Conventions, linter, bonnes pratiques

## Type hints : autres exemples

```python
age: int = 1

# Pas besoin d'initialiser une variable pour annoter son type
x: int  # Ok (no value at runtime until assigned)

# Structures spéciales pour créer des types
from typing import Union, Optional

ma_liste: List[Union[int, str]] = [3, 5, "test", "fun"]

x: Optional[str] = "something" if some_condition() else None
# Mypy understands a value can't be None in an if-statement
if x is not None:
    print(x.upper())
```

Plus d'infos: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

---

# Conventions, linter, bonnes pratiques

## Type hints : `mypy`

- Un outil qui fait une analyse statique du code
- `pip3 install mypy`

---

```python
from typing import List

def plus_grand(liste: List[int]) -> int:

    max_tmp = liste[0]
    for element in liste:
        if element > max_tmp:
            max_tmp = element

    return max_tmp

assert plus_grand([8, 32, 9, 10, -9, 5]) == 32
assert plus_grand([3.14, 1.414, 2.718]) == 16
assert plus_grand("toto") == "t"
```

```text
 > mypy script.py 
script.py:15: error: List item 0 has incompatible type "float"; expected "int"
script.py:15: error: List item 1 has incompatible type "float"; expected "int"
script.py:15: error: List item 2 has incompatible type "float"; expected "int"
script.py:16: error: Argument 1 to "plus_grand" has incompatible type "str"; expected "List[int]"
Found 4 errors in 1 file (checked 1 source file)
```

---



class: impact

# Debugging interactif : `pdb`, `ipdb`

---

# Debugging interactif : `pdb`, `ipdb`

- Python DeBugger
- Permet (entre autre) de définir des "break point" pour rentrer en interactif
   - `import ipdb; ipdb.set_trace()`
   - en 3.7 : `breakpoint()` <small>Mais fait appel à `pdb` et non `ipdb` ?</small>
- Une fois en interactif, on peut inspecter les variables, tester des choses, ...
- On dispose aussi de commandes spéciales pour executer le code pas-à-pas
- Significativement plus efficace que de rajouter des `print()` un peu partout !

---

# Debugging interactif : `pdb`, `ipdb`

### Commandes spéciales

- `l(ist)` : affiche les lignes de code autour de code (ou continue le listing precedent)
- `c(ontinue)` : continuer l'execution normalement (jusqu'au prochain breakpoint)
- `s(tep into)` : investiguer plus en détail la ligne en cours, possiblement en descendant dans les appels de fonction
- `n(ext)` : passer directement à la ligne suivante
- `w(here)` : print the stack trace, c.a.d. les différents sous-appels de fonction dans lesquels on se trouve
- `u(p)` : remonte d'un cran dans les appels de la stacktrace
- `d(own)` : redescend d'un cran dans les appels de la stacktrace

- `pp <variable>` : pretty-print d'une variable (par ex. une liste, un dict, ..)










---

class: impact

# Parallelisation avec Python

---

# Parallelisation

## Multi-thread vs multi-process

- Multi-thread (module `threading`)
   - léger : utilisent la meme memoire RAM
   - ... mais faire attention aux écritures concurrentes
   - idéal lorsque beaucoup d'IO sont bloquantes
   - **en python**(!) : tournent sur un seul coeur (probleme de GIL)
- Multi-process (module `multiprocessing`)
   - mémoire séparée
   - communication entre process + complexe
   - sur plusieurs CPU / core
   - les process fils peuvent être tués si necessaire

---

# Parallelisation

![](img/multithreadinggil.png)

---

# Parallelisation

![](img/gil.png)

---

# Parallelisation

## Exemple classique pour calcul scientifique

- Des tâches qui prennent du CPU .. donc on utilise un fonctionnement multi-process pour pas être limité par la GIL
- On initialise un lot de *workers*
- Le *master* gère une queue / liste de tâches à faire (pile FIFO)
- Les *workers* piochent dans les tâches et les réalisent
- ... jusqu'à ce qu'il n'y ai plus rien à faire!

---

# Parallelisation

## Exemple de tâche que l'on peut souhaiter paralleliser

- Hypothèse : des tâches indépendantes les unes des autres ...

```python
def gaussian_filter(path_to_image):
    image = load(path_to_image)
    filtered_image = Image(..)
    for x,y in image.pixels:
       ...
    return filtered_image


filtered_images = [gaussian_filter(i) for i in os.listdir(...)]
```

---

```python
from multiprocessing import JoinableQueue, Process

def worker_func(id_, queue):
    while True:
        print("[Worker %s] Waiting for task" % id_)
        path_to_image = queue.get()
        print("[Worker %s] Got task %s" % (id_, t))
        gaussian_filter(path_to_image)
        print("[Worker %s] Done with task %s" % (id_, t))
        queue.task_done()

# Création et initialisation de la queue de tâches à faire
queue = JoinableQueue()
for image_path in os.lisdir(...):
    queue.put(image_path)
```

---

```python

# Création et démarrage de la pool de worker
nWorkers = 5
print("[Master] Creating pool of", nWorkers, "workers")
workers = []
for id in range(nWorkers):
    w = Process(target=worker_func,args=(id,queue))
    w.daemon = True
    w.start()
    workers.append(w)

# Partir boire du café jusqu'à ce que les subordonné 
# aient fini leur travail !
print("[Master] Waiting for queue to be completed")
queue.join()
print("[Master] All done!")
```

---

- Récupérer des valeurs de retour depuis les workers ?
- Possibilité de simplification avec l'objet `Pool`

---


# Parallelisation

## Bon OK, mais si notre contrainte c'est les I/O ?

- Par exemple : visiter toutes les pages d'un site web, récursivement

![](img/cpuio.png)

---

![](img/cpuio.png)

- Alternative au multithreading: la programmation asynchrone (`async`, `asyncio`)
    - cf par ex. https://stackoverflow.com/questions/47169474/parallel-asynchronous-io-in-pythons-coroutines
