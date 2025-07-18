# Tema Simplă - Matplotlib și Git
import termcolor as tc
import colorama as col
import matplotlib.pyplot as plt

import random
import numpy as np


# Tema Simplă - Matplotlib și Git

"""
🎯 TEMA FOARTE SIMPLĂ:
Creează grafice cu matplotlib și încarcă pe GitHub.

📋 PAȘI:
1. Creează repo pe GitHub numit "my-matplotlib-project"
2. Clone repo local
3. Creează virtual environment
4. Instalează matplotlib
5. Completează codul de mai jos
6. Commitează și push pe GitHub

💻 COMENZI:
# Pe GitHub: Creează repo "my-matplotlib-project"
git clone https://github.com/USERNAME/my-matplotlib-project.git
cd my-matplotlib-project
python -m venv .venv
.venv\Scripts\activate    (Windows)
source .venv/bin/activate (Mac/Linux)
pip install matplotlib
pip freeze > requirements.txt

📚 RESURSE UTILE:
- Matplotlib Tutorial: https://www.w3schools.com/python/matplotlib_intro.asp
- Plot Types: https://www.w3schools.com/python/matplotlib_plotting.asp
- Customization: https://www.w3schools.com/python/matplotlib_labels.asp
- Git Basics: https://www.w3schools.com/git/
"""

import matplotlib.pyplot as plt
import numpy as np

def create_line_plot():
    """Creează un grafic cu linii"""
    
    # Date simple
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    
    # TODO 1: Creează figura
    # INSTRUCȚIUNI: Folosește plt.figure() pentru a crea o figură nouă
    # - Setează dimensiunea la 8x6 inch folosind parametrul figsize=(8, 6)
    # - Exemplu de sintaxă: plt.figure(figsize=(width, height))
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_pyplot.asp
    
    plt.figure(figsize=(8, 6))

    # TODO 2: Creează plot-ul cu linii
    # INSTRUCȚIUNI: Folosește plt.plot() pentru a desena liniile
    # - Primul parametru: lista x
    # - Al doilea parametru: lista y
    # - Setează culoarea la 'blue' cu parametrul color
    # - Adaugă marcatori circulari cu marker='o'
    # - Setează grosimea liniei cu linewidth=2
    # - Setează mărimea markerilor cu markersize=8
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_line.asp
    
    plt.plot(x, y, color='blue', marker='o', linewidth=2, markersize=8)


    # TODO 3: Adaugă titlu, labels și grid
    # INSTRUCȚIUNI: Personalizează graficul
    # - plt.title() pentru titlu: 'Grafic cu Linii'
    # - plt.xlabel() pentru label axa X: 'Axa X'
    # - plt.ylabel() pentru label axa Y: 'Axa Y'
    # - plt.grid(True) pentru a activa grila
    # - Pentru fontsize folosește parametrul fontsize=16 la titlu și 12 la labels
    # - Pentru font bold folosește fontweight='bold'
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_labels.asp
    
    plt.title('Grafic cu Linii', fontsize=16, fontweight='bold')
    plt.xlabel('Axa X', fontsize=12, fontweight='bold')
    plt.ylabel('Axa Y', fontsize=12, fontweight='bold')
    plt.grid(True)

    # TODO 4: Salvează și afișează graficul
    # INSTRUCȚIUNI: Salvează și afișează
    # - plt.savefig() pentru a salva imaginea ca 'line_plot.png'
    # - Folosește dpi=300 pentru calitate înaltă
    # - Folosește bbox_inches='tight' pentru a elimina spațiile albe
    # - plt.show() pentru a afișa graficul
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_pyplot.asp
    
    plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
    plt.show()


def create_bar_plot():
    """Creează un grafic cu bare"""
    
    # Date simple
    categories = ['A', 'B', 'C', 'D']
    values = [15, 25, 30, 20]
    
    # TODO 1: Creează figura
    # INSTRUCȚIUNI: La fel ca la line_plot
    # - Folosește plt.figure() cu figsize=(8, 6)
    
    plt.figure(figsize=(8, 6))

    # TODO 2: Creează plot-ul cu bare
    # INSTRUCȚIUNI: Folosește plt.bar() pentru grafic cu bare
    # - Primul parametru: categories (pentru axa X)
    # - Al doilea parametru: values (pentru înălțimea barelor)
    # - Setează culori diferite: color=['red', 'green', 'blue', 'orange']
    # - Setează transparența cu alpha=0.7
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_bars.asp
    
    plt.bar(categories, values, color=['red', 'green', 'blue', 'orange'], alpha=0.7)


    # TODO 3: Adaugă titlu, labels și grid
    # INSTRUCȚIUNI: Personalizează graficul
    # - Titlu: 'Grafic cu Bare'
    # - xlabel: 'Categorii'
    # - ylabel: 'Valori'
    # - Grid doar pe axa Y: plt.grid(True, axis='y')
    # - Setează alpha=0.3 pentru transparența gridului
    
    
    # TODO 4: Salvează și afișează
    # INSTRUCȚIUNI: Salvează ca 'bar_plot.png'
    # - Folosește aceleași setări ca la line_plot
    
    pass

def create_scatter_plot():
    """Creează un grafic cu puncte"""
    
    # Date aleatorii
    x = np.random.randn(50)
    y = np.random.randn(50)
    
    # TODO 1: Creează figura
    # INSTRUCȚIUNI: Folosește plt.figure() cu figsize=(8, 6)
    
    # TODO 2: Creează plot-ul cu puncte
    # INSTRUCȚIUNI: Folosește plt.scatter() pentru grafic cu puncte
    # - Primul parametru: x
    # - Al doilea parametru: y
    # - Setează culoarea la 'purple' cu parametrul c
    # - Setează transparența cu alpha=0.6
    # - Setează mărimea punctelor cu s=100
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_scatter.asp
    
    # TODO 3: Adaugă titlu, labels și grid
    # INSTRUCȚIUNI: Personalizează graficul
    # - Titlu: 'Grafic cu Puncte'
    # - xlabel: 'Axa X'
    # - ylabel: 'Axa Y'
    # - Grid cu alpha=0.3
    
    # TODO 4: Salvează și afișează
    # INSTRUCȚIUNI: Salvează ca 'scatter_plot.png'
    
    pass

def create_subplot():
    """Creează subplot cu toate graficele împreună"""
    
    # TODO 1: Creează figura cu subplots
    # INSTRUCȚIUNI: Folosește plt.subplots() pentru multiple grafice
    # - Primul parametru: 2 (2 rânduri)
    # - Al doilea parametru: 2 (2 coloane)
    # - figsize=(12, 10) pentru dimensiune mai mare
    # - Sintaxă: fig, axes = plt.subplots(rows, cols, figsize=(width, height))
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_subplot.asp
    
    # TODO 2: Subplot 1 (sus-stânga): Grafic cu linii
    # INSTRUCȚIUNI: Folosește axes[0, 0] pentru primul subplot
    # - axes[0, 0].plot([1, 2, 3, 4], [1, 4, 2, 3]) pentru date
    # - Adaugă marker și culoare: 'bo-' (blue circles cu linii)
    # - axes[0, 0].set_title('Linii') pentru titlu
    # - axes[0, 0].grid(True) pentru grid
    
    # TODO 3: Subplot 2 (sus-dreapta): Grafic cu bare
    # INSTRUCȚIUNI: Folosește axes[0, 1] pentru al doilea subplot
    # - axes[0, 1].bar(['X', 'Y', 'Z'], [10, 20, 15]) pentru date
    # - Setează culoarea la 'green' cu parametrul color
    # - axes[0, 1].set_title('Bare') pentru titlu
    # - axes[0, 1].grid(True) pentru grid
    
    # TODO 4: Subplot 3 (jos-stânga): Grafic cu puncte
    # INSTRUCȚIUNI: Folosește axes[1, 0] pentru al treilea subplot
    # - axes[1, 0].scatter([1, 2, 3, 4], [2, 3, 1, 4]) pentru date
    # - Setează culoarea la 'red' și mărimea cu s=100
    # - axes[1, 0].set_title('Puncte') pentru titlu
    # - axes[1, 0].grid(True) pentru grid
    
    # TODO 5: Subplot 4 (jos-dreapta): Pie chart
    # INSTRUCȚIUNI: Folosește axes[1, 1] pentru al patrulea subplot
    # - axes[1, 1].pie([30, 25, 20, 25]) pentru date
    # - Adaugă labels: labels=['A', 'B', 'C', 'D']
    # - Adaugă procente: autopct='%1.1f%%'
    # - axes[1, 1].set_title('Pie Chart') pentru titlu
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_pie_charts.asp
    
    # TODO 6: Ajustează layout-ul
    # INSTRUCȚIUNI: Folosește plt.tight_layout() pentru a ajusta automat spațierea
    # - Acest lucru previne suprapunerea elementelor
    
    # TODO 7: Salvează și afișează
    # INSTRUCȚIUNI: Salvează ca 'subplot.png'
    # - Folosește aceleași setări ca la celelalte grafice
    
    pass

def main():
    """Funcția principală"""
    
    print("📊 Matplotlib Demo")
    print("=" * 20)
    
    # TODO: Apelează toate funcțiile
    # INSTRUCȚIUNI: Decomentează și apelează fiecare funcție
    # - create_line_plot()
    # - create_bar_plot()
    # - create_scatter_plot()
    # - create_subplot()
    
    print("Creez grafic cu linii...")
    # create_line_plot()
    
    print("Creez grafic cu bare...")
    # create_bar_plot()
    
    print("Creez grafic cu puncte...")
    # create_scatter_plot()
    
    print("Creez subplot...")
    # create_subplot()
    
    print("✅ Toate graficele au fost create!")

if __name__ == "__main__":
    main()

# 📋 LISTA DE VERIFICARE:
# □ Am creat repo-ul pe GitHub
# □ Am clonat repo-ul local
# □ Am creat virtual environment
# □ Am instalat matplotlib
# □ Am completat toate TODO-urile
# □ Am rulat programul și s-au creat imaginile PNG
# □ Am adăugat și commitat fișierele
# □ Am făcut push pe GitHub

# 🔗 COMENZI GIT FINALE:
# git add .
# git commit -m "Add matplotlib plots"
# git push origin main

# 🎯 OBIECTIVE ÎNDEPLINITE:
# ✅ Virtual environment
# ✅ Instalare cu PIP
# ✅ 4 tipuri de grafice
# ✅ Personalizare (culori, markeri, labels, titluri)
# ✅ Salvare ca PNG
# ✅ Încărcare pe GitHub