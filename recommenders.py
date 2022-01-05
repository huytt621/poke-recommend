import numpy as np
import pandas
from sklearn.neighbors import NearestNeighbors

class knn_recommender():
    k = 5

    def __init__(self):
        self.train_data = None
        self.pokemon_stats = None
        self.neighbors = None
        
    def create(self, train_data, proportions=False):
        self.train_data = train_data
        self.pokemon_stats = {}
        for index, row in train_data.iterrows():
            stats = np.array([row['hp'], row['attack'], row['defense'], row['special-attack'], row['special-defense'], row['speed']])
            if proportions:
                total = sum(stats)
                stats = stats / total
            self.pokemon_stats[row['name']] = stats
        self.neighbors = NearestNeighbors(n_neighbors=self.k + 1) # Extra k to allow for ignoring the same pokemon given as input
        self.neighbors.fit(np.array(list(self.pokemon_stats.values())))

    def recommend(self, pokemon_name):
        return self.neighbors.kneighbors(self.get_stats(pokemon_name))

    def get_stats(self, pokemon_name):
        return np.array([self.pokemon_stats[pokemon_name]])

    def get_pokemon(self, index):
        return self.train_data.iloc[index]['name']
        

