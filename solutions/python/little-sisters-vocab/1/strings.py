"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """
    Take the given word and add the 'un' prefix.
    """
    return "un" + word


def make_word_groups(vocab_words):
    """
    Transform a list containing a prefix and words into a string with
    the prefix followed by the words with prefix applied.
    """
    prefix = vocab_words[0]
    words = vocab_words[1:]

    result = [prefix]

    for word in words:
        result.append(prefix + word)

    return " :: ".join(result)


def remove_suffix_ness(word):
    """
    Remove the suffix 'ness' and adjust spelling if needed.
    """
    # Remove "ness"
    base = word[:-4]

    # If word ends with "i", change it to "y"
    if base.endswith("i"):
        base = base[:-1] + "y"

    return base


def adjective_to_verb(sentence, index):
    """
    Change the adjective in the sentence to a verb.
    """
    words = sentence.split()

    # Get the adjective and remove punctuation
    adjective = words[index].strip(".,!?")

    # Convert to verb
    return adjective + "en"