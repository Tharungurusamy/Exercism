def translate(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:

        # Rule 1
        if word.startswith(("xr", "yt")) or word[0] in vowels:
            result.append(word + "ay")
            continue

        i = 0
        while i < len(word):
            if word[i] in vowels or (word[i] == "y" and i != 0):
                break
            if word[i:i+2] == "qu":
                i += 2
                break
            i += 1

        result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)