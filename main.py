from hill import *
from permutation import *
from vizhenere import *
from shift import *
from aphine import *
from simplesub import *


def file_handler(file: str):
    with open(file) as f:
        s = f.read()
    return s


options = {
    "HILL": hill,
    "PERMUT": permutation,
    "APHIN": aphine,
    "VIZHEN": vizhenere,
    "SHIFT": shift,
    "SIMSUB": simple_substitution,
}

print("Pick a cipher to use:\nHILL to use Hill cypher\nPERMUT to use Permutation cypher\n"
      "APHIN to use Aphine cypher\nVIZHEN to use Vizhenere cypher\nSHIFT to use Shift cypher\n"
      "SIMSUB to use Simple Substitution cypher\nAnd we use:")
cypher = input()
print("What we do? Type 1 to encrypt or 0 to decrypt: ")
cypher_flag = input()

alphabet = file_handler("alphabet.txt")
text = file_handler("in.txt")

if cypher != "HILL":
    key = file_handler("key.txt")
else:
    with open("key.txt") as k:
        key = [[] for i in range(2)]
        for i in range(2):
            key[i] = [int(t) for t in k.readline().split()]
print(f"source text {text}")

text_out = options[cypher](alphabet, text, key, cypher_flag)
o = open('out.txt', 'w', encoding="UTF-8")
o.write(text_out)
o.close()


