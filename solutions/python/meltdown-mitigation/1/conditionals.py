def is_criticality_balanced(temperature, neutrons_emitted):
    # Condition 1: temperature < 800
    # Condition 2: neutrons > 500
    # Condition 3: temperature * neutrons < 500000

    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000:
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    # Calculate generated power
    generated_power = voltage * current

    # Calculate efficiency percentage
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    # Calculate reactor load
    load = temperature * neutrons_produced_per_second

    # LOW: < 90% of threshold
    if load < 0.9 * threshold:
        return "LOW"

    # NORMAL: within ±10% of threshold
    elif 0.9 * threshold <= load <= 1.1 * threshold:
        return "NORMAL"

    # DANGER: outside safe range
    else:
        return "DANGER"
