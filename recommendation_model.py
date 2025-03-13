import pandas as pd
import numpy as np
import pickle as pickle
from sklearn.decomposition import TruncatedSVD
import ast


class Recommendation:
    def __init__(self):
        pass

    def engagement_recommendations(self,df_engagement, user_id, invested, clicks, top_n):

        # Check if user_id exists in df_engagement
        if user_id in df_engagement['user_id'].values:
            # Update the row corresponding to the user_id
            df_engagement.loc[df_engagement['user_id'] == user_id, 'invested_deals'].apply(lambda x: list(invested))
            df_engagement.loc[df_engagement['user_id'] == user_id, 'buy_button_clicks'].apply(lambda x: dict(clicks))
        
        interaction_data = {}
        
        for _, row in df_engagement.iterrows():
            uid = row['user_id']
            
            # Get invested_deals
            invested_deals = row.get('invested_deals', [])
            if not isinstance(invested_deals, list):
                try:
                    invested_deals = ast.literal_eval(invested_deals)
                    if not isinstance(invested_deals, list):
                        invested_deals = []
                except Exception:
                    invested_deals = []
                    
            # Get buy_button_clicks
            buy_button_clicks = row.get('buy_button_clicks', {})
            if not isinstance(buy_button_clicks, dict):
                try:
                    buy_button_clicks = ast.literal_eval(buy_button_clicks)
                    if not isinstance(buy_button_clicks, dict):
                        buy_button_clicks = {}
                except Exception:
                    buy_button_clicks = {}
            
            # Process invested deals if any
            for deal in invested_deals:
                if deal not in interaction_data:
                    interaction_data[deal] = {}
                interaction_data[deal][uid] = interaction_data[deal].get(uid, 0) + 1
            
            # Process buy button clicks if any
            for deal, clicks in buy_button_clicks.items():
                if deal not in interaction_data:
                    interaction_data[deal] = {}
                interaction_data[deal][uid] = interaction_data[deal].get(uid, 0) + clicks
    
        # Create the interaction matrix (rows: deals, columns: users)
        interaction_matrix = pd.DataFrame.from_dict(interaction_data, orient='index').fillna(0)
        
        # Ensure all users in df_behavior are present as columns, even if they have no interactions
        all_user_ids = df_engagement['user_id'].tolist()
        interaction_matrix = interaction_matrix.reindex(columns=all_user_ids, fill_value=0)
        
        # Check if the target user has any interactions (i.e. sum == 0 means no interactions)
        if user_id not in interaction_matrix.columns or interaction_matrix[user_id].sum() == 0:
            # Cold start: recommend deals based on overall popularity
            deal_popularity = interaction_matrix.sum(axis=1)
            recommended_deals_ids = deal_popularity.sort_values(ascending=False).head(top_n).index.tolist()
            return {"user_id": user_id, "recommendations": recommended_deals_ids}
        
        # For users with interactions, perform SVD-based personalized recommendation
        n_components = min(5, min(interaction_matrix.shape))
        svd = TruncatedSVD(n_components=n_components)
        # Apply SVD to get latent features for deals (rows)
        X_svd = svd.fit_transform(interaction_matrix)  # Shape: (n_deals, n_components)
        
        # Reconstruct an approximation of the original interaction matrix
        X_pred = np.dot(X_svd, svd.components_)  # Shape: (n_deals, n_users)
        
        # Get the user column index from the interaction matrix
        user_index = interaction_matrix.columns.get_loc(user_id)
        
        # Retrieve the predicted ratings for all deals for the user
        predicted_ratings = X_pred[:, user_index]
        
        # Get the indices of the top N deals based on predicted rating
        recommended_deal_indices = predicted_ratings.argsort()[-top_n:][::-1]
        recommended_deals_ids = interaction_matrix.index[recommended_deal_indices].tolist()
        result = {"user_id": user_id, "recommendations": recommended_deals_ids}
        return result

# Create instance
recommendation = Recommendation()

# Pickle the Class
with open('class_recommender.pkl', 'wb') as f:
    pickle.dump(recommendation, f)
