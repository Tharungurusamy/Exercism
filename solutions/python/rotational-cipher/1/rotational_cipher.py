def rotate(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            # Handle lowercase
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            # Shift character using modulo
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            # Keep spaces, punctuation unchanged
            result += char

    return result