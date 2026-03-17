SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def is_sublist(a, b):
    if not a:
        return True
    for i in range(len(b) - len(a) + 1):
        if b[i:i + len(a)] == a:
            return True
    return False


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL