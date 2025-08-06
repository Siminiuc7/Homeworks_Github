import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Pasul_2.1_Încarcăm shapefile-ul și CSV-ul

def incarca_harta_si_date(shapefile_path, csv_path):               
   
    gdf = gpd.read_file(shapefile_path)                     
    df = pd.read_csv(csv_path)
    
    gdf = gdf.merge(df, left_on="NUTS_NAME", right_on="Land")        # facem merge pe baza numelui landului; Îmbină după numele landului
    return gdf



# Pasul_2.2_Generam hartă statică pentru energia regenerabilă pe landuri

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
    plt.savefig("harta_energie_regenerabila.png")
    #plt.show()



# Pasul_2.3_Generează hartă statică pentru PIB per capita

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


from vizualizari_harti import incarca_harta_si_date, harta_energie_regenerabila, harta_pib

gdf = incarca_harta_si_date("Landuri_DE.shp", "energie_si_economie_germania.csv")
harta_energie_regenerabila(gdf)
harta_pib(gdf)



# !!! Apelarea funcțiilor dacă fișierul e rulat direct
if __name__ == "__main__":
    gdf = incarca_harta_si_date("Landuri_DE.shp", "energie_si_economie_germania.csv")
    harta_energie_regenerabila(gdf)
    harta_pib(gdf)