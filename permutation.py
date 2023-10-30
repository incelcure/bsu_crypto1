def permutation(alphabet: str, text: str, key: str, cypher_flag):
    permut_list = []
    if len(text) % len(key) != 0:
        text += text[-1] in range(len(text) % len(key))
    sorted_key = ''.join(sorted(key))
    permut = ''
    text_out = ''
    if cypher_flag == "1":
        for i in range(int(len(text) / len(key))):
            permut_list.append(''.join(text[i * len(key): (i + 1) * len(key)]))
        for i in range(len(key)):
            permut += "".join(str((sorted_key.find(key[i]))))
        for i in range(len(permut_list)):
            for j in range(len(key)):
                text_out += permut_list[i][int(permut[j])]
    else:
        for i in range(int(len(text) / len(key))):
            permut_list.append(''.join(text[i * len(key): (i + 1) * len(key)]))
        for i in range(len(key)):
            permut += "".join(str((sorted_key.find(key[i]))))
        for i in range(len(permut_list)):
            for j in range(len(key)):
                text_out += permut_list[i][permut.find(f"{j}")]

    return text_out
