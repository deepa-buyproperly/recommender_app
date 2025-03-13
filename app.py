#app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
# from investor_data import InvestorData
from model import df_engagement, recommender
# from recommendation_model import Recommendation

app = FastAPI()

# Load the pickled model and related data on startup.
# model_data = load_model()

class RecommendationRequest(BaseModel):
    user_id: int
    invested_deals: Optional[List[int]] = []
    buy_button_clicks: Optional[Dict[str, int]] = {}
    account_type: Optional[int] = None
    age: Optional[int] = None
    gender: Optional[int] = None
    marital_status: Optional[int] = None
    num_dependents: Optional[int] = None
    city: Optional[str] = ""
    country: Optional[int] = None
    province: Optional[int] = None
    postal_code: Optional[str] = ""
    emp_type: Optional[int] = None
    emp_name: Optional[str] = ""
    job_title: Optional[str] = ""
    years_with_company: Optional[int] = None
    co_investors: Optional[int] = None
    relation_founders: Optional[int] = None
    current_tax_year_single_income: Optional[int] = None
    previous_one_tax_year_single_income: Optional[int] = None
    previous_two_tax_year_single_income: Optional[int] = None
    current_tax_year_family_income: Optional[int] = None
    previous_one_tax_year_family_income: Optional[int] = None
    previous_two_tax_year_family_income: Optional[int] = None
    total_net_assets: Optional[int] = None
    net_worth_excl_residence: Optional[int] = None
    is_borrowed_funds: Optional[bool] = None
    is_reg_dealer: Optional[bool] = None
    is_financial_firm: Optional[bool] = None
    investment_time_horizon: Optional[int] = None
    significant_withdrawal_years: Optional[int] = None
    regular_withdrawal_years: Optional[int] = None
    emergency_savings: Optional[int] = None
    debt_service_percentage: Optional[int] = None
    rate_of_return_objective: Optional[int] = None
    investment_objectives: Optional[int] = None
    attitude_towards_investing: Optional[int] = None
    declining_market_outcome: Optional[int] = None
    risk_assumption: Optional[int] = None

@app.post("/user_recommendations")
async def get_recommendation(request: RecommendationRequest):
    try:
        result = recommender.engagement_recommendations(
            df_engagement=df_engagement,
            user_id=request.user_id,
            invested=request.invested_deals,
            clicks=request.buy_button_clicks,
            top_n=3
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint to check if the API is running
@app.get("/")
def home():
    return {"message": "Recommendation API is running!"}

# @app.get("/existing_recommendation/{user_id}")
# async def get_existing(user_id: int):
#     try:
#         # Use the pickled model's get_existing_recommendation method for login-only scenario.
#         result = model_data.get_existing_recommendation(user_id, top_n=3)
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))