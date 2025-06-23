"""
Task: Creați o funcție cu numele "task_5" care utilizând list comprehension va returna o listă care conține string-ul "par" sau "impar" pentru fiecare număr de la 1 până n (inclusiv n).
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=10 rezultatul returnat va fi ["impar", "par", "impar", "par", "impar", "par", "impar", "par", "impar", "par"]
"""

# CODUL TĂU VINE MAI JOS:

def task_5(n):
    for x in range(1, n + 1):
      if x % 2 == 0: 
        return "par"
    else: 
        return "impar" 

print(task_5(15))  # De ce in cazul meu da rezultat doar o data par, desi eu am specificat (15)

# CODUL TĂU VINE MAI SUS:

"""Cu ajutorul GPT"""
def task_5(n):
    return ["par" if x % 2 == 0 else "impar" for x in range(1, n + 1)]

print(task_5(15))