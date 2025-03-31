def fuzzify_altitude(altitude):
    if altitude > 500:
        return {"high": 1.0, "medium": 0.0, "low": 0.0}
    elif 200 <= altitude <= 500:
        return {"high": (500 - altitude) / 300, "medium": (altitude - 200) / 300, "low": 0.0}
    else:
        return {"high": 0.0, "medium": (200 - altitude) / 200, "low": 1.0}

def fuzzify_vertical_speed(vertical_speed):
    if vertical_speed > 10:
        return {"fast": 1.0, "normal": 0.0, "slow": 0.0}
    elif 0 <= vertical_speed <= 10:
        return {"fast": (10 - vertical_speed) / 10, "normal": vertical_speed / 10, "slow": 0.0}
    else:
        return {"fast": 0.0, "normal": (-vertical_speed) / 10, "slow": 1.0}

def fuzzy_rules(altitude_fuzzy, vertical_speed_fuzzy):
    rules = {
        "increase_thrust": max(altitude_fuzzy["high"], vertical_speed_fuzzy["slow"]),
        "decrease_thrust": max(altitude_fuzzy["low"], vertical_speed_fuzzy["fast"]),
        "maintain_thrust": min(altitude_fuzzy["medium"], vertical_speed_fuzzy["normal"])
    }
    return rules

def defuzzify_thrust(fuzzy_output):
    increase = fuzzy_output["increase_thrust"]
    decrease = fuzzy_output["decrease_thrust"]
    maintain = fuzzy_output["maintain_thrust"]

    # Simplified weighted average defuzzification
    if increase > decrease and increase > maintain:
        return 1.0 # Increase thrust
    elif decrease > increase and decrease > maintain:
        return -1.0 # Decrease thrust
    else:
        return 0.0 # Maintain thrust

# Example usage
altitude = 1000  # Example altitude
vertical_speed = -10  # Example vertical speed

altitude_fuzzy = fuzzify_altitude(altitude)
vertical_speed_fuzzy = fuzzify_vertical_speed(vertical_speed)
fuzzy_output = fuzzy_rules(altitude_fuzzy, vertical_speed_fuzzy)
thrust_adjustment = defuzzify_thrust(fuzzy_output)

print(f"Altitude: {altitude}, Vertical Speed: {vertical_speed}")
print(f"Fuzzy Altitude: {altitude_fuzzy}")
print(f"Fuzzy Vertical Speed: {vertical_speed_fuzzy}")
print(f"Fuzzy Rules Output: {fuzzy_output}")
print(f"Thrust Adjustment: {thrust_adjustment}")
