import time
import random
import sys
from multiprocessing import JoinableQueue, Process, Pool, Queue


# Definition du travail des workers
def travailler_durement(tache):
    print("Task %s" % tache)
    time.sleep(random.randint(3,7))
    return ord(tache)

def worker_func(id_, queue, out):
    while True:
        print("[Worker %s] Waiting for task" % id_)
        t = queue.get()
        print("[Worker %s] Got task %s" % (id_, t))
        v = travailler_durement(t)
        out.put(v)
        print("[Worker %s] Done with task %s" % (id_, t))
        queue.task_done()


# Création et initialisation de la queue de tâches à faire
queue = JoinableQueue()
for letter in "abcdefjklmnoprst":
    queue.put(letter)
out = Queue()


# Création et démarrage de la pool de worker
nWorkers = 5
print("[Master] Creating pool of", nWorkers, "workers")
workers = []
for id in range(nWorkers):
    w = Process(target=worker_func,args=(id,queue,out))
    w.daemon = True
    w.start()
    workers.append(w)


# Boire du café jusqu'à ce que les subordonné aient fini
# ce qu'ils ont à faire
print("[Master] Waiting for queue to be completed")
queue.join()
while not out.empty():
    print(out.get())
print("[Master] All done!")
