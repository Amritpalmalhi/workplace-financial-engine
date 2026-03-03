from app.npv import calculate_npv


def test_npv_positive():
    cashflows = [-1000, 300, 400, 500]
    result = calculate_npv(cashflows, 0.1)
    assert result > 0
