"""
Task: Creați o funcție cu numele "task_4" care primind ca argument o matrice de liste precum [[1, 2], [3, 4], [5, 6]]
va returna o listă aplatizată sau altfel spus o listă cu elementele fiecărei liste , adică [1, 2, 3, 4, 5, 6]
"""

# CODUL TĂU VINE MAI JOS:


def task_4(matrice):
    rezultat = []
    for lista in matrice:
        rezultat.extend(lista)
    return rezultat

matrice = [[1, 2], [3, 4], [5, 6]]

print(task_4(matrice))

# sau

def task_4(matrice):
    return [element for sublista in matrice for element in sublista]
matrice = [[1, 2], [3, 4], [5, 6]]

print(task_4(matrice))

# CODUL TĂU VINE MAI SUS:
