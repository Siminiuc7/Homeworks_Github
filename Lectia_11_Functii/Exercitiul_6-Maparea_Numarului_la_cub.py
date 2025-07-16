"""
Task: Creați o funcție cu numele "task_6" care utilizând list comprehension va returna un dicționar care mappează fiecare număr de la 1 la 5 la cubul său.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=5 rezultatul returnat va fi {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
"""

# CODUL TĂU VINE MAI JOS:
# print("Ex 6:")
print(f"Exercitiul 6")

def task_6(n):
    return {x: x**3 for x in range(1, n + 1)}

n = int(input("Introduceți n: "))
print(task_6(n))

# n = int(input("Introduceti n: "))
# print(task_6(n))
# CODUL TĂU VINE MAI SUS: