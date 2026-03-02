def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    decimal_value = 0
    for d in digits:
        decimal_value = decimal_value * input_base + d

    if decimal_value == 0:
        return [0]

    result = []
    while decimal_value > 0:
        remainder = decimal_value % output_base
        result.append(remainder)
        decimal_value //= output_base

    return result[::-1]