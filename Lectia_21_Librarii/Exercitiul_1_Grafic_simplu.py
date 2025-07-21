# Tema Simplă - Matplotlib și Git
import termcolor as tc
import colorama as col
import matplotlib.pyplot as plt

import random
import numpy as np


# Tema Simplă - Matplotlib și Git

def create_line_plot():
    """Creează un grafic cu linii"""

    # TODO 1: Creează figura
    # INSTRUCȚIUNI: Folosește plt.figure() pentru a crea o figură nouă
    # - Setează dimensiunea la 8x6 inch folosind parametrul figsize=(8, 6)
    # - Exemplu de sintaxă: plt.figure(figsize=(width, height))
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_pyplot.asp

    # TODO 2: Creează plot-ul cu linii
    # INSTRUCȚIUNI: Folosește plt.plot() pentru a desena liniile
    # - Primul parametru: lista x
    # - Al doilea parametru: lista y
    # - Setează culoarea la 'blue' cu parametrul color
    # - Adaugă marcatori circulari cu marker='o'
    # - Setează grosimea liniei cu linewidth=2
    # - Setează mărimea markerilor cu markersize=8
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_line.asp
        
    # TODO 3: Adaugă titlu, labels și grid
    # INSTRUCȚIUNI: Personalizează graficul
    # - plt.title() pentru titlu: 'Grafic cu Linii'
    # - plt.xlabel() pentru label axa X: 'Axa X'
    # - plt.ylabel() pentru label axa Y: 'Axa Y'
    # - plt.grid(True) pentru a activa grila
    # - Pentru fontsize folosește parametrul fontsize=16 la titlu și 12 la labels
    # - Pentru font bold folosește fontweight='bold'
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_labels.asp

    
    # TODO 4: Salvează și afișează graficul
    # INSTRUCȚIUNI: Salvează și afișează
    # - plt.savefig() pentru a salva imaginea ca 'line_plot.png'
    # - Folosește dpi=300 pentru calitate înaltă
    # - Folosește bbox_inches='tight' pentru a elimina spațiile albe
    # - plt.show() pentru a afișa graficul
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_pyplot.asp
    
    plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
    plt.show()
  
    # Date simple
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]  
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color='blue', marker='o', linewidth=2, markersize=8)
    plt.title("rafic cu Linii", fontsize=16,fontweight='bold')
    plt.xlabel('Axa X', fontsize=12,fontweight='bold')
    plt.ylabel('Axa Y',fontsize=12, fontweight='bold')
    plt.grid(True)
    plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
    plt.show()
    