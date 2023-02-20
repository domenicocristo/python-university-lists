"""
Scrivete una funzione di nome tronca che prenda una lista, la modifichi togliendo 
il primo e l'ultimo elemento, e restituisca None.
"""

def tronca(t):
    del t[0]
    del t[-1]

t = [1, 2, 3, 4]
tronca(t)
print(t)