"""
Scrivete una funzione di nome mediani che prenda una lista e restituisca una 
nuova lista che contenga tutti gli elementi, escluisi il primo e l'ultimo.
"""

def mediani(t):
    return t[1:-1]

print(mediani([1, 2, 3, 4, 5, 6]))