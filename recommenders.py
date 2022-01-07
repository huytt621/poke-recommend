import numpy as np
import pandas
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

class cosine_recommender():

    def __init__(self):
        self.train_data = None
        self.similarity_matrix = None
        self.pokemon_index = None
        
    def create(self, train_data):
        self.train_data = train_data
        self.pokemon_index = {}
        vectorizer = CountVectorizer()
        words = []
        for index, row in train_data.iterrows():
            types_and_abilities = ' '.join([row['ability 0'], row['ability 1'], row['ability 2'], row['type 0'], row['type 1']])
            words.append(types_and_abilities)
            self.pokemon_index[row['name']] = index
        word_count = vectorizer.fit_transform(words)
        self.similarity_matrix = cosine_similarity(word_count, word_count)

    def recommend(self, pokemon_name):
        pokemon_index = self.get_pokemon_index(pokemon_name)
        pokemon_row = [(similarity, index) for index, similarity in enumerate(self.similarity_matrix[pokemon_index])]
        pokemon_row.sort(key=lambda pair: pair[0], reverse=True)
        return pokemon_row[0:6]

    def get_pokemon_index(self, pokemon_name):
        return self.pokemon_index[pokemon_name]

    def get_pokemon(self, index):
        return self.train_data.iloc[index]['name']