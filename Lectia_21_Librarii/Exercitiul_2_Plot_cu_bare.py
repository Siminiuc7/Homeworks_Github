

    # TODO 1: Creează figura
    # INSTRUCȚIUNI: La fel ca la line_plot
    # - Folosește plt.figure() cu figsize=(8, 6)
    
    # TODO 2: Creează plot-ul cu bare
    # INSTRUCȚIUNI: Folosește plt.bar() pentru grafic cu bare
    # - Primul parametru: categories (pentru axa X)
    # - Al doilea parametru: values (pentru înălțimea barelor)
    # - Setează culori diferite: color=['red', 'green', 'blue', 'orange']
    # - Setează transparența cu alpha=0.7
    # 📖 Vezi: https://www.w3schools.com/python/matplotlib_bars.asp

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

    # Date simple
import matplotlib.pyplot as plt

def create_bar_plot():
        """Creează un grafic cu bare"""
categories = ['A', 'B', 'C', 'D']
values = [15, 25, 30, 20]
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color=['red', 'green', 'blue', 'orange'], alpha=0.7)
plt.title('Grafic cu Bare', fontweight='bold')
plt.xlabel('Categorii', fontweight='bold')
plt.ylabel('Valori', fontweight='bold')
plt.grid(True, axis='y', alpha=0.3)
plt.savefig('bar_plot.png')
plt.show()
