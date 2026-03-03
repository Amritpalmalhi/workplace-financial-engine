def calculate_salary_arbitrage(
    current_salary,
    target_market_salary,
    cost_of_labor_index,
    fx_rate=1.0
):
    adjusted_target = target_market_salary * cost_of_labor_index
    adjusted_target_fx = adjusted_target * fx_rate
    return adjusted_target_fx - current_salary
