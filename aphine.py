import math


def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0

    d1, x1, y1 = extended_euclid(b, a % b)
    d = d1
    x = y1
    y = x1 - math.floor(a / b) * y1
    return d, x, y


def aphine(alphabet: str, text: str, key: str, cypher_flag):
    a = alphabet.find(key[0])
    b = alphabet.find(key[1])
    d, x, y = extended_euclid(a, len(alphabet))

    print(f"a {a}")
    print(f"b {b}")

    print((a*x) % len(alphabet))
    if d != 1:
        print("Пошел нахуй!")
        return 0
    text_out = ""

    if cypher_flag == "1":
        for i in range(len(text)):
            if text[i] != " ":
                print((alphabet.find(text[i]) * a + b) % len(alphabet))
                text_out += alphabet[(alphabet.find(text[i]) * a + b) % len(alphabet)]
            else:
                text_out += " "
    else:
        for i in range(len(text)):
            if text[i] != " ":
                text_out += alphabet[((alphabet.find(text[i]) - b) * x) % len(alphabet)]
            else:
                text_out += " "

    print(text_out)
    o = open('out.txt', 'w', encoding="UTF-8")
    o.write(text_out)
    o.close()
