import pickle
import numpy as np

def load_model(model_path="svd_recommender.pkl"):
    """
    Loads the pickled SVD recommender model along with its mapping dictionaries.
    """
    with open(model_path, "rb") as f:
        model_data = pickle.load(f)
    return model_data

def recommend_deals(model_data, user_id, N=3):
    """
    Given the loaded model_data and a user_id, this function returns the top N recommended deal IDs.
    The returned dictionary is of the format:
    {
      "user_id": user_id,
      "recommendations": [deal_id1, deal_id2, ...]
    }
    """
    user_id_to_idx = model_data["user_id_to_idx"]
    deal_ids = model_data["deal_ids"]
    predicted_matrix = model_data["predicted_matrix"]

    # If the user_id does not exist, return the recent deals ids.
    if user_id not in user_id_to_idx:
        return {"user_id": user_id, "recommendations": [42,43,44]} # change required

    user_idx = user_id_to_idx[user_id]
    scores = predicted_matrix[user_idx].copy()

    # Get indices of the top N deals with the highest predicted scores.
    recommended_indices = np.argpartition(scores, -N)[-N:]
    recommended_indices = recommended_indices[np.argsort(-scores[recommended_indices])]
    recommendations = [deal_ids[i] for i in recommended_indices]

    return {"user_id": user_id, "recommendations": recommendations}
