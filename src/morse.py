MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}
REVERSE_MORSE = {
    value: key
    for key, value in MORSE_CODE.items()
}


def encode_text(text):
    text = text.upper()
    result = []

    for letter in text:
        if letter in MORSE_CODE:
            result.append(MORSE_CODE[letter])

    return " ".join(result)


def decode_morse(morse):
    result = []

    for code in morse.split():
        if code in REVERSE_MORSE:
            result.append(REVERSE_MORSE[code])

    return "".join(result)


print(encode_text("this is a bad idea"))
print(decode_morse(".... . .-.. .-.. ---"))
