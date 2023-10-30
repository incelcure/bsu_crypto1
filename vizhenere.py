def vizhenere(alp: str, text: str, key: str, cypher_flag):
    from itertools import cycle

    if cypher_flag == "1":
        f = lambda arg: alp[(alp.index(arg[0]) + alp.index(arg[1]) % len(alp)) % len(alp)]
        return ''.join(map(f, zip(text, cycle(key))))

    else:
        f = lambda arg: alp[alp.index(arg[0]) - alp.index(arg[1]) % len(alp)]
        return ''.join(map(f, zip(text, cycle(key))))
    return True
