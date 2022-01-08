# Pokémon Recommender

The Pokémon Recommender is a recommender system that outputs similar Pokémon to the one inputted.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following dependencies.

```bash
pip install numpy pandas scikit-learn matplotlib
```

## Usage

1. At the command prompt, type `python3 get-pokemon.py 50` to generate the file `50-pokemon.json`, a JSON file that contains data on the first 50 Pokémon according to the National Dex. For more Pokémon, replace the `50` from the command with the number of Pokémon to consider. This will generate a different file `{NUM}-pokemon.json` where `NUM` is the number of Pokémon.
2. Run the cells of the Jupyter Notebook, making sure to specify the correct JSON file. Use the classes from `recommenders.py` to create recommender objects that need to be initiated with the `create` method that takes a DataFrame as input (specifically `pokemon_df`).
3. To get recommendations, use the `recommend` method, which takes a Pokémon's name as input and returns a DataFrame.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
