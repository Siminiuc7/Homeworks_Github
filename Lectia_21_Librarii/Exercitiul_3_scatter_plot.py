
import matplotlib.pyplot as plt
import numpy as np

def reate_scatter_plot():
    """Creează un grafic cu puncte"""

x = np.random.randn(50)
y = np.random.randn(50)

    # TODO 1: Creează figura
    # INSTRUCȚIUNI: Folosește plt.figure() cu figsize=(8, 6)

plt.figure(figsize=(8, 6))
    
    # TODO 2: Creează plot-ul cu puncte
    # INSTRUCȚIUNI: Folosește plt.scatter() pentru grafic cu puncte
    # - Primul parametru: x
    # - Al doilea parametru: y
    # - Setează culoarea la 'purple' cu parametrul c
    # - Setează transparența cu alpha=0.6
    # - Setează mărimea punctelor cu s=100
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_scatter.asp

plt.scatter(x, y, c='purple', alpha= 0.6, s=100)
    
    # TODO 3: Adaugă titlu, labels și grid
    # INSTRUCȚIUNI: Personalizează graficul
    # - Titlu: 'Grafic cu Puncte'
    # - xlabel: 'Axa X'
    # - ylabel: 'Axa Y'
    # - Grid cu alpha=0.3

plt.title('Grafic cu Puncte')
plt.xlabel('Axa X')
plt.ylabel('Axa Y')
plt.grid(alpha=0.3)
    
    # TODO 4: Salvează și afișează
    # INSTRUCȚIUNI: Salvează ca 'scatter_plot.png'

plt.savefig('scatter_plot.png')
plt.show()





