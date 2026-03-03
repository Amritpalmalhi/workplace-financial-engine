from .cashflow import calculate_rent_projection, calculate_operating_expenses, combine_cashflows
from .npv import calculate_npv


class FinancialEngine:

    def run_10_year_projection(self, lease, opex):
        rent = calculate_rent_projection(
            lease.base_rent,
            lease.escalation_rate,
            lease.term_years
        )

        expenses = calculate_operating_expenses(
            opex.annual_expense,
            opex.growth_rate,
            lease.term_years
        )

        total_cashflow = combine_cashflows(rent, expenses)

        return total_cashflow

    def compute_npv(self, cashflows, discount_rate):
        return calculate_npv(cashflows, discount_rate)
