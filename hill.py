import math


def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0

    d1, x1, y1 = extended_euclid(b, a % b)
    d = d1
    x = y1
    y = x1 - math.floor(a / b) * y1
    return d, x, y


def hill(alphabet: str, text: str, key, cypher_flag):
    if len(text) % 2 != 0:
        text += text[-1]
    permut_list = [[] for i in range(int(len(text) / 2))]
    result_list = [[] for i in range(int(len(text) / 2))]
    text_out = ''
    if cypher_flag == "1":
        for i in range(int(len(text) / 2)):
            for j in range(2):
                permut_list[i].append(alphabet.find(text[i * 2 + j]))
            result_list[i].append((permut_list[i][0] * key[0][0] + permut_list[i][1] * key[1][0]) % len(alphabet))
            text_out += alphabet[result_list[i][0]]
            result_list[i].append((permut_list[i][0] * key[0][1] + permut_list[i][1] * key[1][1]) % len(alphabet))
            text_out += alphabet[result_list[i][1]]
    else:

        temp = [[], []]
        det_a = key[0][0] * key[1][1] - key[0][1] * key[1][0]
        d, x, y = extended_euclid(det_a, len(alphabet))

        det_a = x

        temp[0].append(key[0][0])
        temp[0].append(key[1][0])
        temp[1].append(key[0][1])
        temp[1].append(key[1][1])

        key[0][0] = 1 * temp[1][1] * det_a
        key[0][1] = -1 * temp[1][0] * det_a
        key[1][0] = -1 * temp[0][1] * det_a
        key[1][1] = 1 * temp[0][0] * det_a

        for i in range(int(len(text) / 2)):
            for j in range(2):
                permut_list[i].append(alphabet.find(text[i * 2 + j]))
            result_list[i].append((permut_list[i][0] * key[0][0] + permut_list[i][1] * key[1][0]) % len(alphabet))
            text_out += alphabet[result_list[i][0]]
            result_list[i].append((permut_list[i][0] * key[0][1] + permut_list[i][1] * key[1][1]) % len(alphabet))
            text_out += alphabet[result_list[i][1]]

    return text_out
