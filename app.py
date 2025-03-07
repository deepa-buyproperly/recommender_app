from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from investor_data import InvestorData
from model import load_model, recommend_deals

app = FastAPI()

# Load the pickled model and related data on startup.
model_data = load_model()

class RecommendationRequest(BaseModel):
    new_user: int
    user_id: int
    invested_deals: List[str]
    buy_button_clicks: Dict[str, int]
    account_type: int
    age: int
    gender: int
    marital_status: int
    num_dependents: int
    city: int
    country: int
    province: str
    postal_code: str
    emp_type: int
    emp_name: str
    job_title: str
    years_with_company: int
    co_investors: int
    relation_founders: int
    current_tax_year_single_income: int
    previous_one_tax_year_single_income: int
    previous_two_tax_year_single_income: int
    current_tax_year_family_income: int
    previous_one_tax_year_family_income: int
    previous_two_tax_year_family_income: int
    total_net_assets: int
    net_worth_excl_residence: int
    borrowed_funds: int
    is_reg_dealer: int
    is_financial_firm: int
    investment_time_horizon: int
    significant_withdrawal_years: int
    regular_withdrawal_years: int
    emergency_savings: int
    debt_service_percentage: int
    rate_of_return_objective: int
    investment_objectives: int
    attitude_towards_investing: int
    declining_market_outcome: int
    risk_assumption: int

@app.post("/user_recommendations")
async def get_recommendation(request: RecommendationRequest):
    try:
        # Create an InvestorData instance from the request
        investor_data = InvestorData.from_request(request)
        
        result = recommend_deals(model_data, investor_data.user_id, N=3)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
