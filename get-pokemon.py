import requests
import json
import sys

def main():
    if len(sys.argv) < 2:
        print('Please run again with the number of pokemon as an argument')
    num_pokemon = sys.argv[1]
    generate_json(num_pokemon)

def generate_json(num_pokemon):
    pokemon_urls = requests.get('https://pokeapi.co/api/v2/pokemon', params={ 'limit': num_pokemon }).json()

    print('Getting Pokemon from PokeAPI...')
    all_pokemon = { 'pokemon': [] }
    for pokemon in pokemon_urls['results']:
        pokemon_data = requests.get(pokemon['url'])
        all_pokemon['pokemon'].append(pokemon_data.json())
    print('Complete!')

    print('Saving to {}-pokemon.json'.format(num_pokemon))
    with open('{}-pokemon.json'.format(num_pokemon), 'w') as file:
        json.dump(all_pokemon, file)
    print('Complete!')

if __name__ == '__main__':
    main()
