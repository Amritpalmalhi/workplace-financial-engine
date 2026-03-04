def attrition_multiplier(distance_km):
    if distance_km < 10:
        return 1.0
    elif distance_km < 25:
        return 1.15
    elif distance_km < 50:
        return 1.35
    else:
        return 1.6


def calculate_attrition_cost(input_data):
    multiplier = attrition_multiplier(input_data.distance_km)
    effective_attrition = input_data.base_attrition_rate * multiplier
    affected_employees = input_data.headcount * effective_attrition
    return affected_employees * input_data.replacement_cost

