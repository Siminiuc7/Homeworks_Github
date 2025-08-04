"""
Task: Creați o funcție cu numele "task_2" care acceptă orice număr de argumente cu cuvinte cheie 
folosind **kwargs și returnează un dicționar cu toate cheile în majuscule.
Exemplu: task_2(nume="ana", varsta=25) -> {"NUME": "ana", "VARSTA": 25}
         task_2(oras="bucuresti", cod=123) -> {"ORAS": "bucuresti", "COD": 123}
"""

# CODUL TĂU VINE MAI JOS:
print("\n===Exercitiul_2")

def task_2(**kwargs):
    return {cheie.upper(): valoare for cheie, valoare in kwargs.items()}

print (task_2(nume="ana", varsta=25))
print (task_2(oras="bucuresti", cod=123))

# CODUL TĂU VINE MAI SUS: