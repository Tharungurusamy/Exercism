"""
Functions to help play and score a game of blackjack.
"""


def value_of_card(card):

    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):

    value1 = value_of_card(card_one)
    value2 = value_of_card(card_two)

    if value1 > value2:
        return card_one

    elif value2 > value1:
        return card_two

    else:
        return (card_one, card_two)


def value_of_ace(card_one, card_two):

    # If either card is Ace → return 1 (as per test rules)
    if card_one == 'A' or card_two == 'A':
        return 1

    total = value_of_card(card_one) + value_of_card(card_two)

    if total + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):

    cards = [card_one, card_two]

    if 'A' in cards and any(card in ['10', 'J', 'Q', 'K'] for card in cards):
        return True

    return False


def can_split_pairs(card_one, card_two):

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):

    total = value_of_card(card_one) + value_of_card(card_two)

    return total == 9 or total == 10 or total == 11