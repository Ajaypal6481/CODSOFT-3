import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class CollaborativeFiltering:
    def __init__(self, user_item_matrix):
        self.user_item_matrix = user_item_matrix

    def calculate_similarity(self):
        self.similarity_matrix = cosine_similarity(self.user_item_matrix)

    def recommend(self, user_id, num_recs):
        similar_users = self.similarity_matrix[user_id].argsort()[:num_recs]
        recs = []
        for sim_user in similar_users:
            recs.extend(self.user_item_matrix.iloc[sim_user].index)
        return recs
