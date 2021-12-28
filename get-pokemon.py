import requests
import json

def main():
    num_pokemon = 898
    pokemon_urls = requests.get('https://pokeapi.co/api/v2/pokemon', params={ 'limit': num_pokemon }).json()

    all_pokemon = { 'pokemon': [] }
    for pokemon in pokemon_urls['results']:
        pokemon_data = requests.get(pokemon['url'])
        all_pokemon['pokemon'].append(pokemon_data.json())

    with open('pokemon.json', 'w') as file:
        json.dump(all_pokemon, file)


if __name__ == '__main__':
    main()