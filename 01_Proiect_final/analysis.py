import pandas as pd
import geopandas as gpd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os


print(f"\nProiectul final 'Dezvoltarea economica versus Energia regenerabila in Germania'")

print(f"\n-> Pasul_1.1: Încarea datelor csv cu date la nivelul Germaniei si Europei, geogson (Germ, Europa) plus definirea paletei coloristice") 

df = pd.read_csv("C:/01_Rodica/Python/Homeworks_Github/01_Proiect_final/energie_si_economie_germania.csv")


palette = {"Baden-Wuerttemberg": "#1f77b4", 
    "Bayern": "#2ca02c",             
    "Berlin": "#8c564b",              
    "Brandenburg": "#e377c2",         
    "Bremen": "#7f7f7f",             
    "Hamburg": "#bcbd22",            
    "Hessen": "#17becf",              
    "Mecklenburg-Vorpommern": "#9467bd",  
    "Niedersachsen": "#ff7f0e",       
    "Nordrhein-Westfalen": "#d62728", 
    "Rheinland-Pfalz": "#aec7e8",     
    "Saarland": "#c49c94",            
    "Sachsen": "#f7b6d2",             
    "Sachsen-Anhalt": "#c7c7c7",      
    "Schleswig-Holstein": "#ffbb78", 
    "Thueringen": "#000000"}

print()
print(f"\n-> Pasul_1.2: Afișarea primeleor rânduri din Tabela")
print()
print(df.head())

print()
print(f"\n -> Pasul_1.3: Afisarea datelor statistice descriptive") 
print()
print(df.describe())

print()
print(f"\n-> Pasul_1.4: Corelațiile între variabile")
print("\nCorelații:")
print(df.corr(numeric_only=True))

print()
print(f"\n-> Pasul_1.5: Executarea Scatterplot: PIB vs energie regenerabilă")
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x="PIB_capita", y="Energie_regenerabila_pct", hue="Land", palette= palette)
plt.title("PIB per capita vs Energie regenerabilă (%)", fontsize = 15)
plt.xlabel("PIB per capita (EUR)", fontsize = 12)
plt.ylabel("Energie regenerabilă (%)", fontsize = 12)
plt.xticks(rotation=45)
plt.xlim(0, 800000)
plt.tick_params(axis='x', labelsize=10, colors='dimgray')
plt.tick_params(axis='y', labelsize=10, colors='dimgray')
plt.grid(True)
plt.grid(True, linestyle='-', linewidth=0.8, alpha=0.7)
plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left')
plt.tight_layout()
plt.savefig("Grafic.png") 
plt.show()

print()
print(f"\n-> Pasul_1.6: Afisarea corelatiilo cu ajutorul Heatmap")
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="YlGnBu")
plt.title("Matricea corelațiilor")
plt.tight_layout()
plt.show()

print()
print(f"\n-> Pasul_2: Vizualizarea Datelor pe o harta statica si interactiva") # generare intr-un alt file aparte


print()
print(f"\n-> Pasul_3: Comparatia cu alte state europene") # generare intr-un alt file aparte


print()
print(f"\n-> Pasul_4: Generarea uniu fisier general main.py de unde se ruleaza tot codul") # generare intr-un alt file aparte
