from app.attrition import attrition_multiplier, calculate_attrition_cost
from app.models import AttritionInput


def test_attrition_multiplier():
    assert attrition_multiplier(5) == 1.0
    assert attrition_multiplier(20) > 1.0
    assert attrition_multiplier(60) == 1.6


def test_attrition_cost():
    input_data = AttritionInput(
        distance_km=30,
        base_attrition_rate=0.1,
        replacement_cost=20000,
        headcount=100
    )

    cost = calculate_attrition_cost(input_data)
    assert cost > 0
