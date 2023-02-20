"""
Due parole sono anagrammi se potete ottenerle riordinando le lettere di cui sono composte. 
Scrivete una funzione di nome anagramma che riceva due stringhe e restituisca True se sono anagrammi.
"""

def anagramma(s1, s2):
    return sorted(s1) == sorted(s2)

print(anagramma("motore", "remoto"))