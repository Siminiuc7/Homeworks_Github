
# Continutul main.py
print("=== Proiect: Dezvoltarea economică vs Energie regenerabilă în Germania si la nivel european===\n")

# Pasul_3.1_Importam continutul din file-ul Analiză generală
import analysis

# Pasul_3.2_Importam continutul din file-ul Vizualizări pe hartă
from vizualizari_harti import incarca_harta_si_date, harta_energie_regenerabila, harta_pib

# Pasul_3.3_Încarcăm harta + datele pentru Landuri
shapefile_path = "C:/01_Rodica/Python/Homeworks_Github/01_Proiect_final/Landuri_DE.shp"
csv_path = "C:/01_Rodica/Python/Homeworks_Github/01_Proiect_final/energie_si_economie_germania.csv"

gdf = incarca_harta_si_date(shapefile_path, csv_path)


# # Pasul_3.4_Încarcăm harta + datele pentru Landuri
harta_energie_regenerabila(gdf)
harta_pib(gdf)

# Pasul_3.5_Importam continutul din file-ul Analiză generală
import Germ_vs_EU