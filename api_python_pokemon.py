#libreria para hacer peticiones HTTP
import requests
URL_BASE = "https://pokeapi.co/api/v2"
def get_pokemon(nombre):
    url = f"{URL_BASE}/pokemon/{nombre.lower()}"
    response = requests.get(url) # hace la peticion get
    
    if response.status_code == 200:
        return response.json()  #Peticion exitosa, devuelve la respuesta en formato JSON
    else:
        print("Error: Pokemon no encontrado")
        return None  # Si no se encuentra el pokemon, devuelve None
        
if __name__ == "__main__":
    print("Bienvenido a la API de Pokémon....")
    nombre=input("Introduce el nombre de un Pokémon: ").strip()
    
    if(datos := get_pokemon(nombre)):
        print(f"\nNombre: {datos['name'].capitalize()}")
        print(f"Altura: "{datos['height']/10} metros")
        print(f"Peso:"{datos['weight']/10} kg")
        print("\nMovimientos: ")
        for move in datos['moves'] [:5]:
            print(f"- {move['move']['name'].replace('-', ' ') }")
        
    
