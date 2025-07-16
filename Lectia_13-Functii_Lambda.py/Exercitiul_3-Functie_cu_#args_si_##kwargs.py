"""
Task: Creați o funcție cu numele "task_3" care acceptă un nume obligatoriu, 
*args pentru hobby-uri și **kwargs pentru informații suplimentare.
Să returneze un string formatat: "Nume: [nume], Hobby-uri: [lista], Info: [dict]"
Exemplu: task_3("Ana", "citit", "alergat", varsta=25, oras="Cluj") -> 
         "Nume: Ana, Hobby-uri: ['citit', 'alergat'], Info: {'varsta': 25, 'oras': 'Cluj'}"
"""

# CODUL TĂU VINE MAI JOS:
print("\n===Exercitiul_3===")

def task_3(nume, *args, **kwargs):
    hobby = list(args)
    info = kwargs
    return f"Nume: {nume}, Hobby-uri: {hobby} Informatii:{info}"

result = task_3("Ana", "citit", "alergat", varsta=25, oras="Cluj")
print(result)
# CODUL TĂU VINE MAI SUS: 