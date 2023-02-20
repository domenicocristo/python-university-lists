"""
Scrivete una funzione di nome somma_cumulata che prenda una lista di numeri
e restituisca la somma cumulata, cioè una nuova lista dove l'i-esimo elemento è la somma dei primi 
i + 1 elementi della lista di origine. 
"""

def somma_cumulata(t):
    totale = 0
    t2 = []
    for x in t:
        totale += x
        t2.append(totale)
    return t2

print(somma_cumulata([1, 2, 3, 4, 5]))