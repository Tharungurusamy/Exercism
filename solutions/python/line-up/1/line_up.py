def ordinal(n):
    if 10 <= n % 100 <= 13:
        return str(n) + "th"
    elif n % 10 == 1:
        return str(n) + "st"
    elif n % 10 == 2:
        return str(n) + "nd"
    elif n % 10 == 3:
        return str(n) + "rd"
    else:
        return str(n) + "th"


def line_up(name, number):
    return f"{name}, you are the {ordinal(number)} customer we serve today. Thank you!"