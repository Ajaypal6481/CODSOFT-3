from models.collaborative_filtering import CollaborativeFiltering
from models.content_based_filtering import ContentBasedFiltering

class HybridModel:
    def __init__(self, user_item_matrix, item_features):
        self.cf_model = CollaborativeFiltering(user_item_matrix)
        self.cbf_model = ContentBasedFiltering(item_features)

    def recommend(self, user_id, num_recs):
        cf_recs = self.cf_model.recommend(user_id, num_recs)
        cbf_recs = self.cbf_model.recommend(self.cbf_model.calculate_user_profile(user_id), num_recs)
        return cf_recs + cbf_recs
