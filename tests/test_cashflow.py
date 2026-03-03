from app.cashflow import calculate_rent_projection, calculate_operating_expenses, combine_cashflows


def test_rent_projection():
    rents = calculate_rent_projection(1000, 0.05, 3)
    assert len(rents) == 3
    assert rents[0] == 1000
    assert rents[1] > rents[0]


def test_operating_expenses():
    expenses = calculate_operating_expenses(500, 0.03, 3)
    assert len(expenses) == 3
    assert expenses[1] > expenses[0]


def test_combine_cashflows():
    rent = [1000, 1050, 1100]
    expenses = [500, 520, 540]
    combined = combine_cashflows(rent, expenses)
    assert combined == [1500, 1570, 1640]
