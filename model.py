#model.py
import pickle
import pandas as pd
# from recommendation_model import Recommendation 

# Load DataFrame
with open("df_engagement.pkl", "rb") as f:
    df_engagement = pickle.load(f)

# Load Pickled Class Object
with open("class_recommender.pkl", "rb") as f:
    recommender = pickle.load(f)
