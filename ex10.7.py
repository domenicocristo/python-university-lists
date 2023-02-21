"""
Scrivete una funzione di nome ha_duplicati che richieda una lista e restituisca 
True se contiene elementi che compaiono più di una volta. Non deve modificare la lista di origine.
"""

def ha_duplicati(s):
    t = list(s)
    t.sort()

    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

print(ha_duplicati(["hello", "world", "hello"]))