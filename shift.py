def shift(alphabet: str, text: str, key: str, cypher_flag):
    text_out = ""
    c = alphabet.find(key)

    if cypher_flag == "1":
        for i in range(len(text)):
            if text[i] != " ":
                text_out += alphabet[(alphabet.find(text[i]) + c) % len(alphabet)]
            else:
                text_out += " "
    else:
        for i in range(len(text)):
            if text[i] != " ":
                text_out += alphabet[(alphabet.find(text[i]) - c) % len(alphabet)]
            else:
                text_out += " "

    print(text_out)
    o = open('out.txt', 'w', encoding="UTF-8")
    o.write(text_out)
    o.close()
