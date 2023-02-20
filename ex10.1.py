"""
Scrivete una funzione di nome somma_nidificata che prenda una lista di liste di
numeri interi e sommi gli elementi di tutte le liste nidificate. 
"""

def somma_nidificata(t):
    totale = 0
    for nidificate in t:
        totale += sum(nidificate)
    return totale

print(somma_nidificata([[1, 2], [3], [4, 5, 6]]))