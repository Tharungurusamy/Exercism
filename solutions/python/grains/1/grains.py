def square(number):
    """
    Return the number of grains on a given square.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total():
    """
    Return the total number of grains on the chessboard.
    """
    total_grains = 0

    for i in range(1, 65):
        total_grains += 2 ** (i - 1)

    return total_grains