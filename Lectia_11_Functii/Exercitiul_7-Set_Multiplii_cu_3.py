"""
Task: Creați o funcție cu numele "task_7" care utilizând list comprehension va returna un set cu multiplii de 3 de la 1 la n, unde n este un argument al funcției.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face multiplicarea.
Exemplu: Pentru n=50 rezultatul returnat va fi {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48}       
"""
# CODUL TĂU VINE MAI JOS:
# print("Ex 7:")

print("Exercitiul 7")

def task_7(n):
    rezultat = {x for x in range (1, n + 1) if x % 3 == 0}
    return rezultat
     
n = int(input("Introduceti n: "))

print(task_7(99))

# n = int(input("Introduceti n: "))
# print(task_7(99))
# CODUL TĂU VINE MAI SUS:

