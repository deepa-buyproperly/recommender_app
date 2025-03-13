# # investor_data.py
# from dataclasses import dataclass
# from typing import List, Dict, Optional

# @dataclass
# class InvestorData:
    
#     user_id: int
#     invested_deals: Optional[List[int]]
#     buy_button_clicks: Optional[Dict[int, int]]
#     account_type: Optional[int]
#     age: Optional[int]
#     gender: Optional[int]
#     marital_status: Optional[int]
#     num_dependents: Optional[int]
#     city: Optional[str]
#     country: Optional[int]
#     province: Optional[int]
#     postal_code: Optional[str]
#     emp_type: Optional[int]
#     emp_name: Optional[str]
#     job_title: Optional[str]
#     years_with_company: Optional[int]
#     co_investors: Optional[int]
#     relation_founders: Optional[int]
#     current_tax_year_single_income: Optional[int]
#     previous_one_tax_year_single_income: Optional[int]
#     previous_two_tax_year_single_income: Optional[int]
#     current_tax_year_family_income: Optional[int]
#     previous_one_tax_year_family_income: Optional[int]
#     previous_two_tax_year_family_income: Optional[int]
#     total_net_assets: Optional[int]
#     net_worth_excl_residence: Optional[int]
#     is_borrowed_funds: Optional[bool]
#     is_reg_dealer: Optional[bool]
#     is_financial_firm: Optional[bool]
#     investment_time_horizon: Optional[int]
#     significant_withdrawal_years: Optional[int]
#     regular_withdrawal_years: Optional[int]
#     emergency_savings: Optional[int]
#     debt_service_percentage: Optional[int]
#     rate_of_return_objective: Optional[int]
#     investment_objectives: Optional[int]
#     attitude_towards_investing: Optional[int]
#     declining_market_outcome: Optional[int]
#     risk_assumption: Optional[int]

#     @classmethod
#     def from_request(cls, request):
#         return cls(
#             new_user=request.new_user,
#             user_id=request.user_id,
#             invested_deals=request.invested_deals,
#             buy_button_clicks=request.buy_button_clicks,
#             account_type=request.account_type,
#             age=request.age,
#             gender=request.gender,
#             marital_status=request.marital_status,
#             num_dependents=request.num_dependents,
#             city=request.city,
#             country=request.country,
#             province=request.province,
#             postal_code=request.postal_code,
#             emp_type=request.emp_type,
#             emp_name=request.emp_name,
#             job_title=request.job_title,
#             years_with_company=request.years_with_company,
#             co_investors=request.co_investors,
#             relation_founders=request.relation_founders,
#             current_tax_year_single_income=request.current_tax_year_single_income,
#             previous_one_tax_year_single_income=request.previous_one_tax_year_single_income,
#             previous_two_tax_year_single_income=request.previous_two_tax_year_single_income,
#             current_tax_year_family_income=request.current_tax_year_family_income,
#             previous_one_tax_year_family_income=request.previous_one_tax_year_family_income,
#             previous_two_tax_year_family_income=request.previous_two_tax_year_family_income,
#             total_net_assets=request.total_net_assets,
#             net_worth_excl_residence=request.net_worth_excl_residence,
#             is_borrowed_funds=request.is_borrowed_funds,
#             is_reg_dealer=request.is_reg_dealer,
#             is_financial_firm=request.is_financial_firm,
#             investment_time_horizon=request.investment_time_horizon,
#             significant_withdrawal_years=request.significant_withdrawal_years,
#             regular_withdrawal_years=request.regular_withdrawal_years,
#             emergency_savings=request.emergency_savings,
#             debt_service_percentage=request.debt_service_percentage,
#             rate_of_return_objective=request.rate_of_return_objective,
#             investment_objectives=request.investment_objectives,
#             attitude_towards_investing=request.attitude_towards_investing,
#             declining_market_outcome=request.declining_market_outcome,
#             risk_assumption=request.risk_assumption
#         )
