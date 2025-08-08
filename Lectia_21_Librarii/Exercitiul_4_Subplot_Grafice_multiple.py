import matplotlib.pyplot as plt
import numpy as np

def create_subplot():
    """Creează subplot cu toate graficele împreună"""
    
    # TODO 1: Creează figura cu subplots
    # INSTRUCȚIUNI: Folosește plt.subplots() pentru multiple grafice
    # - Primul parametru: 2 (2 rânduri)
    # - Al doilea parametru: 2 (2 coloane)
    # - figsize=(12, 10) pentru dimensiune mai mare
    # - Sintaxă: fig, axes = plt.subplots(rows, cols, figsize=(width, height))
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_subplot.asp

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # TODO 2: Subplot 1 (sus-stânga): Grafic cu linii
    # INSTRUCȚIUNI: Folosește axes[0, 0] pentru primul subplot
    # - axes[0, 0].plot([1, 2, 3, 4], [1, 4, 2, 3]) pentru date
    # - Adaugă marker și culoare: 'bo-' (blue circles cu linii)
    # - axes[0, 0].set_title('Linii') pentru titlu
    # - axes[0, 0].grid(True) pentru grid

axes[0, 0].plot([1, 2, 3, 4], [1, 4, 2, 3], 'bo')
axes[0, 0].set_title('Linii')
axes[0, 0].grid(True)

    
    # TODO 3: Subplot 2 (sus-dreapta): Grafic cu bare
    # INSTRUCȚIUNI: Folosește axes[0, 1] pentru al doilea subplot
    # - axes[0, 1].bar(['X', 'Y', 'Z'], [10, 20, 15]) pentru date
    # - Setează culoarea la 'green' cu parametrul color
    # - axes[0, 1].set_title('Bare') pentru titlu
    # - axes[0, 1].grid(True) pentru grid

axes[0, 1].bar(['X', 'Y', 'Z'], [10, 20, 15], color ='green')
axes[0, 1].set_title('Bare')
axes[0, 1].grid(True)

    
    # TODO 4: Subplot 3 (jos-stânga): Grafic cu puncte
    # INSTRUCȚIUNI: Folosește axes[1, 0] pentru al treilea subplot
    # - axes[1, 0].scatter([1, 2, 3, 4], [2, 3, 1, 4]) pentru date
    # - Setează culoarea la 'red' și mărimea cu s=100
    # - axes[1, 0].set_title('Puncte') pentru titlu
    # - axes[1, 0].grid(True) pentru grid

axes[1, 0].scatter([1, 2, 3, 4], [2, 3, 1, 4], color ='red', s = 100)
axes[1, 0].set_title('Puncte')
axes[1, 0].grid(True)
    
    # TODO 5: Subplot 4 (jos-dreapta): Pie chart
    # INSTRUCȚIUNI: Folosește axes[1, 1] pentru al patrulea subplot
    # - axes[1, 1].pie([30, 25, 20, 25]) pentru date
    # - Adaugă labels: labels=['A', 'B', 'C', 'D']
    # - Adaugă procente: autopct='%1.1f%%'
    # - axes[1, 1].set_title('Pie Chart') pentru titlu
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_pie_charts.asp
    
axes[1, 1].pie([30, 25, 20, 25], labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
axes[1, 1].set_title('Pie Chart')

    # TODO 6: Ajustează layout-ul
    # INSTRUCȚIUNI: Folosește plt.tight_layout() pentru a ajusta automat spațierea
    # - Acest lucru previne suprapunerea elementelor

plt.tight_layout()
    
    # TODO 7: Salvează și afișează
    # INSTRUCȚIUNI: Salvează ca 'subplot.png'
    # - Folosește aceleași setări ca la celelalte grafice

plt.savefig('subplot.png')
plt.show()