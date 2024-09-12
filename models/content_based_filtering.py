import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedFiltering:
    def __init__(self, item_features):
        self.item_features = item_features

    def calculate_similarity(self, user_profile):
        self.similarity_matrix = cosine_similarity(user_profile, self.item_features)

    def recommend(self, user_profile, num_recs):
        recs = self.similarity_matrix.argsort()[:num_recs]
        return recs
