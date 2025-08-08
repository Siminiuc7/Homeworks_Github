import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pasul_3.1_Încarcăm shapefile-ul și CSV-ul 

csv_path = r"C:\01_Rodica\Python\Homeworks_Github\01_Proiect_final\energie_si_economie_europa.csv"
df_eu = pd.read_csv(csv_path)

print(df_eu.head())

# Elabirarea personalizată a paletei cu 26 culori distincte
culori_26 = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b",
    "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#393b79", "#637939",
    "#8c6d31", "#843c39", "#7b4173", "#3182bd", "#e6550d", "#31a354",
    "#756bb1", "#636363", "#ff9896", "#98df8a", "#c5b0d5", "#c49c94",
    "#f7b6d2", "#9edae5"
]

# Pasul_3.2_Crearea scatterplot PIB per capita vs Energie regenerabila
plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=df_eu,
    x="PIB_per_capita_EUR",
    y="Energie_regenerabila_pct",
    hue="Tara",
    palette=culori_26,
    s=100
)

# Pasul_3.3_Evidentiem Germania
germany = df_eu[df_eu["Tara"] == "Germania"]
plt.scatter(germany["PIB_per_capita_EUR"], germany["Energie_regenerabila_pct"], color="red", label="Germania", s=150)

plt.title("PIB per capita vs Energie regenerabila (%) in Europa", fontsize=14)
plt.xlabel("PIB per capita (EUR)", fontsize=12)
plt.ylabel("Energie regenerabila (%)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig("Grafic.png") 
plt.show()

"""
# Pasul_3.4_Crearea Graficului: PIB per capita
plt.figure(figsize=(14, 6))
df_sorted_pib = df_eu.sort_values(by="PIB_per_capita_EUR", ascending=False)
sns.barplot(data=df_sorted_pib, x="Tara", y="PIB_per_capita_EUR", palette="Blues_d")
plt.xticks(rotation=45, ha="right")
plt.title("PIB per capita in tarile europene", fontsize=14)
plt.ylabel("EUR")
plt.tight_layout()
plt.show()

# Pasul_3.4_Crearea Graficului: Energie regenerabila
plt.figure(figsize=(14, 6))
df_sorted_energy = df_eu.sort_values(by="Energie_regenerabila_pct", ascending=False)
sns.barplot(data=df_sorted_energy, x="Tara", y="Energie_regenerabila_pct", palette="Greens")
plt.xticks(rotation=45, ha="right")
plt.title("Ponderea energiei regenerabile (%) in Europa", fontsize=14)
plt.ylabel("%")
plt.tight_layout()
plt.show()

# HEATMAP: Corelatii
plt.figure(figsize=(8, 6))
sns.heatmap(df_eu.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Corelatii intre indicatorii socio-economici")
plt.tight_layout()
plt.show()
"""