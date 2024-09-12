import pandas as pd

def load_user_item_matrix(file_path):
    return pd.read_csv(file_path)

def load_item_features(file_path):
    return pd.read_csv(file_path)
