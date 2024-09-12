from sklearn.metrics import precision_score, recall_score

def precision(recommended_items, actual_items):
    return precision_score(actual_items, recommended_items)

def recall(recommended_items, actual_items):
    return recall_score(actual_items, recommended_items)
