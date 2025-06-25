"""
Task_4: Creați o funcție cu numele "task_4" care calculează aria unei forme geometrice.
Parametri: forma (obligatoriu - "dreptunghi", "triunghi", "cerc"), a (obligatoriu), b (default None).
- Pentru dreptunghi: aria = a * b (b este obligatoriu)
- Pentru pătrat (când forma="dreptunghi" și b=None): aria = a * a  
- Pentru triunghi: aria = a * b / 2 (b este obligatoriu)
- Pentru cerc: aria = 3.14159 * a * a (a este raza, b se ignoră)
Returnează aria calculată sau -1 dacă parametrii sunt invalizi.
"""


# CODUL TĂU VINE MAI JOS:

def task_4(forma, a, b=None):
    if forma == "dreptunghi":
      return a * b
    if b is None:
      return a * a          #Tot exercitiul apare ca greseala sinu pot controla daca la rulare e corect
print(task_4(dreptunghi, 5))
# CODUL TĂU VINE MAI SUS: