
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os

# Verificăm folderul curent
print("Folderul curent este:", os.getcwd())

# 🔧 Calea absolută către fișiere (modifică dacă ai altă locație)
shapefile_path = "C:/01_Rodica/Python/Homeworks_Github/01_Proiect_final/Landuri_DE.shp"
csv_path = "C:/01_Rodica/Python/Homeworks_Github/01_Proiect_final/energie_si_economie_germania.csv"

# Verificăm dacă fișierele există
if not os.path.exists(shapefile_path):
    print(f"Fișierul shapefile nu a fost găsit: {shapefile_path}")
    exit()

if not os.path.exists(csv_path):
    print(f"Fișierul CSV nu a fost găsit: {csv_path}")
    exit()

# Funcție pentru încărcare și îmbinare
def incarca_harta_si_date(shapefile_path, csv_path):
    gdf = gpd.read_file(shapefile_path)
    df = pd.read_csv(csv_path)

    # Îmbinare pe baza numelui landului
    gdf = gdf.merge(df, left_on="NUTS_NAME", right_on="Land")
    return gdf

# Hartă pentru energia regenerabilă
def harta_energie_regenerabila(gdf):
    fig, ax = plt.subplots(figsize=(12, 10))
    gdf.plot(
        column="Energie_regenerabila_pct",
        cmap="YlGn",
        linewidth=0.8,
        edgecolor="0.8",
        legend=True,
        ax=ax
    )
    ax.set_title("Ponderea energiei regenerabile în Germania (%)", fontsize=14)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig("harta_energie_regenerabila.png")
    plt.show()

# Hartă pentru PIB per capita
def harta_pib(gdf):
    fig, ax = plt.subplots(figsize=(12, 10))
    gdf.plot(
        column="PIB_capita",
        cmap="Blues",
        linewidth=0.8,
        edgecolor="0.8",
        legend=True,
        ax=ax
    )
    ax.set_title("PIB per capita în Germania (EUR)", fontsize=14)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig("harta_pib.png")
    plt.show()

# Executăm dacă fișierul e rulat direct
if __name__ == "__main__":
    gdf = incarca_harta_si_date(shapefile_path, csv_path)
    harta_energie_regenerabila(gdf)
    harta_pib(gdf)
    print("✅ Hărțile au fost generate și salvate.")
