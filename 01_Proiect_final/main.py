# Continutul main.py
print("=== Proiect: Dezvoltarea economică vs Energie regenerabilă în Germania si la nivel european===\n")

# Pasul_3.1_Importam continutul din file-ul Analiză generală
import analysis

# Pasul_3.2_Importam continutul din file-ul Vizualizări pe hartă
from vizualizari_harti import incarca_harta_si_date, harta_energie_regenerabila, harta_pib

# Pasul_3.3_Încarcăm harta + datele pentru Landuri
gdf = incarca_harta_si_date("Landuri_DE.shp", "energie_si_economie_germania.csv")

# # Pasul_3.4_Încarcăm harta + datele pentru LanduriGenerează hărțile
harta_energie_regenerabila(gdf)
harta_pib(gdf)