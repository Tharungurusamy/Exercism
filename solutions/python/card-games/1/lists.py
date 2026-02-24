def get_rounds(round_number):
    return [round_number, round_number + 1, round_number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, round_number):
    return round_number in rounds


def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    average = card_average(hand)
    approx = (hand[0] + hand[-1]) / 2
    middle = hand[len(hand) // 2]

    return average == approx or average == middle


def average_even_is_average_odd(hand):
    even = hand[::2]
    odd = hand[1::2]

    return sum(even) / len(even) == sum(odd) / len(odd)


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand