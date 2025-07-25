# Tema de casă: Lucrul cu fișiere în Python
# Timp estimat: 20 minute

"""
INSTRUCȚIUNI:
Completează următoarele exerciții. Testează fiecare exercițiu pentru a te asigura că funcționează.
"""

# ===============================================
# EXERCIȚIUL 1: Crearea și scrierea într-un fișier
# ===============================================

"""
Creează un fișier numit 'info_personal.txt' și scrie următoarele informații în el:
- Numele tău (pe prima linie)
- Vârsta ta (pe a doua linie)  
- Hobby-ul tău preferat (pe a treia linie)

Folosește funcția open() cu modul 'w' și metoda write().
Nu uita să închizi fișierul!
"""

print(f"\nExercitiul 1: Crearea și scrierea într-un fișier")
# Scrie codul tău aici:
# TODO: Deschide fișierul 'info_personal.txt' pentru scriere
f = open("info_personal.txt", "w")

# TODO: Scrie numele tău
f.write("Informatii personale:\n")
f.write("Numele: Rodica Siminiuc\n")

# TODO: Scrie vârsta ta
f.write("Varsta: 34\n")

# TODO: Scrie hobby-ul tău
f.write("Hobby: Cititul\n")

# TODO: Închide fișierul
f.close()

# ===============================================
# EXERCIȚIUL 2: Citirea unui fișier
# ===============================================

"""
Citește conținutul fișierului 'info_personal.txt' pe care l-ai creat mai sus
și afișează-l pe ecran.

Folosește funcția open() cu modul 'r' și metoda read().
"""
print(f"\nExercitiul 2: Citirea unui fișier")

# Scrie codul tău aici:
# TODO: Deschide fișierul 'info_personal.txt' pentru citire
f = open("info_personal.txt", "r")

# TODO: Citește conținutul și salvează-l într-o variabilă
continut = f.read()

# TODO: Afișează conținutul
print("Conținutul fișierului:")
print(continut)

# TODO: Închide fișierul
f.close()

# ===============================================
# EXERCIȚIUL 3: Utilizarea modulului os
# ===============================================

"""
Folosește modulul os pentru a:
1. Afișa directorul curent de lucru
2. Lista toate fișierele din directorul curent
3. Verifica dacă fișierul 'info_personal.txt' există
"""

import os

print(f"\nExercitiul 3: Utilizarea modulului os")

# Scrie codul tău aici:
# TODO: Afișează directorul curent folosind os.getcwd()
print("Directorul curent:", os.getcwd())

# TODO: Afișează lista fișierelor din directorul curent folosind os.listdir()
print("Fișiere în director:")


# TODO: Verifică dacă 'info_personal.txt' există folosind os.path.exists()
print(os.listdir())

if os.path.exists("info_personal.txt"):
    print("'info_personal.txt' există.")
else:
    print("'info_personal.txt' nu există.") 

# ===============================================
# EXERCIȚIUL 4: Lucrul cu JSON
# ===============================================

"""
Creează un dicționar cu informațiile tale personale și salvează-l într-un fișier JSON.
Apoi citește datele din fișierul JSON și afișează-le.

Dicționarul să conțină:
- "nume": numele tău
- "varsta": vârsta ta
- "hobby": hobby-ul tău
- "limbaje_programare": o listă cu limbajele pe care le cunoști (ex: ["Python"])
"""

import json

print(f"\nExercitiul 4: Lucrul cu JSON")

# Scrie codul tău aici:
# TODO: Creează dicționarul cu informațiile tale
info_dict = {
    "nume": "Rodica Siminiuc",
    "varsta": 34,
    "hobby": "Cititul",
    "limbaje_programare": ["Python"]
}

# TODO: Salvează dicționarul într-un fișier JSON numit 'info.json'
with open('info.json', 'w') as json_file:
    json.dump(info_dict, json_file, indent=4)


# TODO: Citește datele din 'info.json' și afișează-le
with open('info.json', 'r') as json_file:
    data = json.load(json_file)
    print("Informații din fișierul JSON:")
    print(data)


# ===============================================
# BONUS (OPȚIONAL)
# ===============================================

"""
Creează o funcție care primește un nume de fișier ca parametru și:
- Verifică dacă fișierul există
- Dacă există, afișează dimensiunea fișierului în bytes
- Dacă nu există, afișează un mesaj corespunzător
"""

def info_fisier(info_personal):
    # TODO: Implementează funcția
    if os.path.exists(info_personal):
        dimensiune = os.path.getsize(info_personal)
        print(f"Fișierul '{info_personal}' există și are {dimensiune} bytes.")
    else:
        print(f"Fișierul '{info_personal}' NU există.")

# Testează funcția cu 'info_personal.txt'

info_fisier('info_personal.txt')