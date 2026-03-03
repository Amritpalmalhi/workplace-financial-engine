from pydantic import BaseModel
from typing import List


class LeaseInput(BaseModel):
    base_rent: float
    escalation_rate: float  # annual %
    term_years: int


class OperatingExpense(BaseModel):
    annual_expense: float
    growth_rate: float


class CapExInput(BaseModel):
    year: int
    amount: float


class SalaryInput(BaseModel):
    current_salary: float
    target_market_salary: float
    cost_of_labor_index: float


class AttritionInput(BaseModel):
    distance_km: float
    base_attrition_rate: float
    replacement_cost: float
    headcount: int
