"""
Scrivete una funzione di nome bisezione che richieda una lista ordinata e un valore da ricercare,
e restituisca True se la parola fa parte della lista, o False se non è presente.
"""

def bisezione(t, v):
    sinistra = 0
    destra = len(t) - 1

    while sinistra <= destra:
        centro = (sinistra + destra) // 2
        if t[centro] == v:
            return True
        elif t[centro] < v:
            sinistra = centro + 1
        else:
            destra = centro - 1

    return False

lista_parole = ["arancia", "banana", "ciao", "mondo"]
print(bisezione(lista_parole, "ciao"))