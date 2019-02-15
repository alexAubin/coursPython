class: impact

# Parallelisation avec Python

---

# Parallelisation

## Multi-thread vs multi-process

- Multi-thread (module `threading`)
   - léger : utilisent la meme memoire RAM
   - ... mais faire attention aux écritures concurrentes
   - idéal lorsque beaucoup d'IO sont bloquantes
   - **en python**(!) : tournent sur un seul coeur
- Multi-process (module `multiprocessing`)
   - mémoire séparée
   - communication entre process + complexe
   - sur plusieurs CPU / core
   - les process fils peuvent être tués si necessaire

---

# Parallelisation

## Exemple classique pour calcul scientifique

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
for letter in "abcdefjklmnoprst":
    queue.put(letter)
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

class: impact

# Interface avec des fonctions en C

---

# Code C à interfacer

```c
// ###############
// # libalex.cpp #
// ###############

#include <stdio.h>
#include <math.h>

extern "C" float exponent(int n, float f)
{
    return pow(n, f);
}

extern "C" float sum(float* tab, int length)
{
    float acc = 0;
    for (int i = 0 ; i < length ; i++)
        acc += tab[i];

    return acc;
}
```

---

# Compilation vers `libalex.so`

```bash
g++ -c -fPIC libalex.cpp -o libalex.o
g++ -shared -Wl,-soname,libalex.so -o libalex.so libalex.o
```

Important : le fichier d'origine doit contenir `extern 'C'` autrement le fichier `.so` ne contient plus le nom originel de la fonction !


---

# Interface Python <-> C avec `ctypes`

```python
################
# pylibalex.py #
################
from ctypes import cdll, c_int, c_float, POINTER
libalex = cdll.LoadLibrary('./libalex.so')


libalex.exponent.argtypes = (c_int, c_float)
libalex.exponent.restype = c_float

def alex_exponent(n, f):
    return libalex.exponent(c_int(n), c_float(f))


libalex.sum.argtypes = (POINTER(c_float), c_int)
libalex.sum.restype = c_float

def alex_sum(tab):
    ftab = [float(e) for e in tab]
    ftab = (c_float * len(ftab))(*ftab)
    return libalex.sum(ftab, len(ftab))
```

---

# Utilisation

```python
from pylibalex import alex_exponent, alex_sum

#
# Test the functions
#

#assert alex_exponent(5, 1.5) == 5**1.5
assert alex_exponent(5, 1.5) - 5**1.5 < 0.0001


L = [5, 6, 1.2, 7.8, 9.5]
assert alex_sum(L) == sum(L)


print("OK!")
```

