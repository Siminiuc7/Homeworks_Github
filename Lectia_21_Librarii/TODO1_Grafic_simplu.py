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
  
    # Date simple
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]  
    plt.figure(figsize=(8, 6))
    plt.plot(x,y, color="blue", marker="o")
    plt.show()