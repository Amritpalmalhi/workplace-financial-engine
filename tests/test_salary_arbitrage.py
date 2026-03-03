from app.salary_arbitrage import calculate_salary_arbitrage


def test_salary_arbitrage_positive():
    result = calculate_salary_arbitrage(
        current_salary=80000,
        target_market_salary=90000,
        cost_of_labor_index=1.0,
        fx_rate=1.0
    )
    assert result == 10000
