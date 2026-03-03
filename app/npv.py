import numpy as np


def calculate_npv(cashflows, discount_rate):
    return np.npv(discount_rate, cashflows)


def scenario_npv_comparison(scenarios: dict, discount_rate: float):
    results = {}
    for name, cashflows in scenarios.items():
        results[name] = calculate_npv(cashflows, discount_rate)
    return results
