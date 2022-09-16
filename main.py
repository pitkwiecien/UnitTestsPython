def encode(text: str) -> str:
    """
    :param str text: The text which we want to encode
    :return: The encoded text
    :rtype: str
    """

    cypher = {"G": "A", "D": "E", "R": "Y", "P": "O", "L": "U", "K": "I"}
    inv_cypher = {value: key for key, value in cypher.items()}
    new_text = ""
    for letter in text:
        if letter in cypher.keys():
            new_text += cypher[letter]
        elif letter in inv_cypher.keys():
            new_text += inv_cypher[letter]
        else:
            new_text += letter
    return new_text


given_number = input("Podaj tekst do zaszyfrowania: ")
print(encode(given_number))
