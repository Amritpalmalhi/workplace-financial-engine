def calculate_rent_projection(base_rent: float, escalation_rate: float, term_years: int):
    rents = []
    current_rent = base_rent

    for _ in range(term_years):
        rents.append(current_rent)
        current_rent *= (1 + escalation_rate)

    return rents


def calculate_operating_expenses(base_expense: float, growth_rate: float, term_years: int):
    expenses = []
    current = base_expense

    for _ in range(term_years):
        expenses.append(current)
        current *= (1 + growth_rate)

    return expenses


def combine_cashflows(rent, expenses):
    return [r + e for r, e in zip(rent, expenses)]
