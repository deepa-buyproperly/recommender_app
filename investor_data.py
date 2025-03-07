from dataclasses import dataclass

@dataclass
class InvestorData:
    new_user: int
    user_id: int
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

    @classmethod
    def from_request(cls, request):
        return cls(
            new_user=request.new_user,
            user_id=request.user_id,
            account_type=request.account_type,
            age=request.age,
            gender=request.gender,
            marital_status=request.marital_status,
            num_dependents=request.num_dependents,
            city=request.city,
            country=request.country,
            province=request.province,
            postal_code=request.postal_code,
            emp_type=request.emp_type,
            emp_name=request.emp_name,
            job_title=request.job_title,
            years_with_company=request.years_with_company,
            co_investors=request.co_investors,
            relation_founders=request.relation_founders,
            current_tax_year_single_income=request.current_tax_year_single_income,
            previous_one_tax_year_single_income=request.previous_one_tax_year_single_income,
            previous_two_tax_year_single_income=request.previous_two_tax_year_single_income,
            current_tax_year_family_income=request.current_tax_year_family_income,
            previous_one_tax_year_family_income=request.previous_one_tax_year_family_income,
            previous_two_tax_year_family_income=request.previous_two_tax_year_family_income,
            total_net_assets=request.total_net_assets,
            net_worth_excl_residence=request.net_worth_excl_residence,
            borrowed_funds=request.borrowed_funds,
            is_reg_dealer=request.is_reg_dealer,
            is_financial_firm=request.is_financial_firm,
            investment_time_horizon=request.investment_time_horizon,
            significant_withdrawal_years=request.significant_withdrawal_years,
            regular_withdrawal_years=request.regular_withdrawal_years,
            emergency_savings=request.emergency_savings,
            debt_service_percentage=request.debt_service_percentage,
            rate_of_return_objective=request.rate_of_return_objective,
            investment_objectives=request.investment_objectives,
            attitude_towards_investing=request.attitude_towards_investing,
            declining_market_outcome=request.declining_market_outcome,
            risk_assumption=request.risk_assumption
        )
