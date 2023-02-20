"""
Scrivete una funzione di nome ordinata che prenda una lista come parametro e
restituisca True se la lista è ordinata in senso crescente, False altrimenti.
"""

def ordinata(t):
    return t == sorted(t)

print(ordinata([1, 2, 3, 4]))