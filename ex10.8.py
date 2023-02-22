"""
Se in una classe ci sono 23 studenti, quante probabilità ci sono che due di loro compiano gli anni
lo stesso giorno? Potete stimare questa probabilità generando alcuni campioni a caso di 23 date e
controllando le corrispondenze. 
"""

def paradosso_del_compleanno(num_studenti):
    # La probabilità che il primo studente non compia gli anni lo stesso giorno di nessuno degli altri è 1 (ovvero certa).
    p = 1

    for k_esimo in range(1, num_studenti+1):
        p *= (365-k_esimo+1)/365
    return int((1 - p) * 100)

print("La probabilità che due studenti compiano gli anni lo stesso giorno è del: ", paradosso_del_compleanno(23), "%")