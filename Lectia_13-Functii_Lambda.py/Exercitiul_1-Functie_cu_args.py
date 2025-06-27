# Tema pentru acasă - Lecția 13: Funcții Avansate (*args, **kwargs, lambda, closure, decoratori, recursivitate)

"""
Task: Creați o funcție cu numele "task_1" care acceptă orice număr de argumente numerice 
folosind *args și returnează suma tuturor argumentelor.
Exemplu: task_1(1, 2, 3) -> 6
         task_1(10, 20) -> 30
         task_1() -> 0
"""

# CODUL TĂU VINE MAI JOS:
print("\n"
"===Exercitiul_1===")

def task_1(*args):
    return sum(args)

print (task_1(5, 6, 7))
print (task_1(11, 22))
print (task_1())

# CODUL TĂU VINE MAI SUS: