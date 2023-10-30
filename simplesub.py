def simple_substitution(alphabet: str, text: str, key: str, cypher_flag):
    text_out = ""
    if cypher_flag == "1":
        for i in range(len(text)):
            if text[i] != " ":
                ch = alphabet.find(text[i])
                text_out += key[ch]
            else:
                text_out += " "
    else:
        for i in range(len(text)):
            if text[i] != " ":
                ch = key.find(text[i])
                text_out += alphabet[ch]
            else:
                text_out += " "
    return text_out
