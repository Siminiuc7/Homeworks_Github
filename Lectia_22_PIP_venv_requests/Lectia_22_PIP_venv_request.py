# Tema pentru acasă - Lecția 22: PIP, Virtual Environments și API Requests

"""
🎯 OBIECTIVUL TEMEI:
Creează un Pokemon Info Client care folosește PokéAPI pentru a obține informații despre pokémoni.

📋 PAȘI DE URMAT:

1. SETUP PROIECT:
   - Creează un director nou numit "pokemon_client"
   - Navighează în director

2. VIRTUAL ENVIRONMENT:
   - Creează un mediu virtual numit ".venv"
   - Activează mediul virtual
   - Verifică că ești în mediul virtual

3. INSTALARE DEPENDENȚE:
   - Instalează librăria "requests"
   - Generează fișierul requirements.txt
   - Verifică că s-a instalat corect

4. IMPLEMENTARE:
   Completează funcțiile de mai jos pentru a crea un client PokéAPI care:
   - Obține informații despre un pokémon după nume
   - Caută pokémoni după tip (type)
   - Afișează informațiile într-un format frumos

5. TESTARE:
   - Testează cu pokémoni diferiți
   - Verifică că parametrii funcționează
   - Gestionează erorile

📝 COMENZI BASH (pentru referință):
```bash
# Creează proiectul
mkdir pokemon_client
cd pokemon_client

# Creează și activează virtual environment
python -m venv .venv

# Windows:
.venv\Scripts\activate

# Linux/Mac:
source .venv/bin/activate

# Instalează dependențe
pip install requests
pip freeze > requirements.txt

# Verifică instalarea
pip list
```

🚀 BONUS POINTS:
- Adaugă validări pentru input
- Implementează cache simplu (salvează rezultatele într-un fișier)
- Adaugă o funcție pentru căutarea aleatorie
- Gestionează frumos erorile de rețea
"""

import requests
import json
from typing import Dict, Optional, List

class PokemonClient:
    """Client pentru interacțiunea cu PokéAPI"""
    
    def __init__(self):
        # TODO: Setează URL-ul de bază pentru PokéAPI
        self.base_url = "https://pokeapi.co/api/v2"
        
        # TODO: Creează o sesiune requests pentru performanță mai bună
        self.session = requests.Session()
        
        # TODO: Setează un User-Agent header
        self.session.headers.update({
            'User-Agent': 'PythonPokemonClient/1.0'
        })
    
    def get_pokemon_info(self, pokemon_name: str) -> Optional[Dict]:
        pokemon_name = pokemon_name.lower()
        if pokemon_name in self.cache:
            return self.cache[pokemon_name]
        """
        Obține informații despre un pokémon după nume
        
        Args:
            pokemon_name: Numele pokémonului (ex: "pikachu", "charmander")
        
        Returns:
            Dict cu informații despre pokémon sau None dacă nu există
        """
        
        # TODO: Implementează această funcție
        # Hints:
        # - Folosește self.session.get() pentru request
        # - URL-ul ar trebui să fie: f"{self.base_url}/pokemon/{pokemon_name.lower()}"
        # - Gestionează status codes (200 = success, 404 = not found)
        # - Returnează un dict cu informații utile: nume, înălțime, greutate, tipuri, abilități
    
    url = f"{self.base_url}/pokemon/{pokemon_name.lower()}"
    if response.status_code == 200:
        data = response.json()

pass
    
def search_pokemon_by_type(self, pokemon_type: str) -> Optional[List[str]]:
        """
        Caută pokémoni după tip
        
        Args:
            pokemon_type: Tipul pokémonului (ex: "fire", "water", "electric")
            
        Returns:
            Listă cu numele pokémonilor de acel tip sau None dacă tipul nu există
        """
        # TODO: Implementează această funcție
        # Hints:
        # - URL-ul ar trebui să fie: f"{self.base_url}/type/{pokemon_type.lower()}"
        # - Răspunsul conține o listă de pokémoni în ['pokemon']
        # - Fiecare pokémon are numele în ['pokemon']['name']
        # - Returnează doar primii 10 pokémoni pentru simplitate
        
        pass
    
    def get_random_pokemon(self) -> Optional[Dict]:
        """
        BONUS: Obține un pokémon aleatoriu
        
        Returns:
            Dict cu informații despre un pokémon aleatoriu
        """
        # TODO: Implementează această funcție (BONUS)
        # Hints:
        # - Folosește import random
        # - Generează un număr aleatoriu între 1 și 1010 (numărul total de pokémoni)
        # - Folosește get_pokemon_info() cu ID-ul generat
        
        pass

def format_pokemon_info(pokemon_data: Dict) -> str:
    """
    Formatează informațiile despre pokémon pentru afișare
    
    Args:
        pokemon_data: Datele pokémonului de la API
        
    Returns:
        String formatat pentru afișare
    """
    # TODO: Implementează această funcție
    # Hints:
    # - Extrage informațiile importante: name, height, weight, types, abilities
    # - Folosește f-strings pentru formatare frumoasă
    # - Adaugă emoji-uri pentru a face output-ul mai atractiv
    
    pass

def main():
    """Funcția principală - interfața utilizatorului"""
    
    print("🐾\n Bun venit la Pokemon Info Client!")
    print("=" * 40)
    
    # TODO: Creează instanța clientului
    client = PokemonClient()
    
    while True:
        print("\n📋 Opțiuni disponibile:")
        print("1. Caută pokémon după nume")
        print("2. Caută pokémoni după tip")
        print("3. Pokémon aleatoriu (BONUS)")
        print("4. Ieșire")
        
        choice = input("\nAlege o opțiune (1-4): ").strip()
        
        if choice == '1':
            # TODO: Implementează căutarea după nume
            pokemon_name = input("Introdu numele pokémonului: ").strip()
            
            # TODO: Folosește client.get_pokemon_info(pokemon_name)
            # TODO: Verifică dacă rezultatul nu este None
            # TODO: Afișează informațiile folosind format_pokemon_info()
            
            pass
        
        elif choice == '2':
            # TODO: Implementează căutarea după tip
            pokemon_type = input("Introdu tipul pokémonului (ex: fire, water, electric): ").strip()
            
            # TODO: Folosește client.search_pokemon_by_type(pokemon_type)
            # TODO: Verifică dacă rezultatul nu este None
            # TODO: Afișează lista de pokémoni
            
            pass
        
        elif choice == '3':
            # TODO: BONUS - Implementează pokémon aleatoriu
            pass
        
        elif choice == '4':
            print("👋 La revedere! Mult noroc cu pokémonii!")
            break
        
        else:
            print("❌ Opțiune invalidă. Te rog alege 1-4.")

if __name__ == "__main__":
    main()

# TODO: După implementare, testează cu următorii pokémoni:
# - pikachu
# - charmander  
# - bulbasaur
# - squirtle
# - gengar

# TODO: Testează căutarea după tipuri:
# - electric
# - fire
# - water
# - grass
# - ghost