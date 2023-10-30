from hill import *
from permutation import *
from vizhenere import *
from shift import *
from aphine import *
from simplesub import *

import unittest


class TestCiphers(unittest.TestCase):

    def test_hill(self):
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        cypher_flag = "1"
        text = "ПРИВЕТ"
        key = [[4, 5], [3, 4]]
        self.assertEqual(hill(alphabet, text, key, cypher_flag), 'ППИУКВ')

        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        cypher_flag = "0"
        text = "ППИУКВ"
        key = [[4, 5], [3, 4]]
        self.assertEqual(hill(alphabet, text, key, cypher_flag), 'ПРИВЕТ')

    def test_permut(self):
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        cypher_flag = "1"
        text = "ПРИВЕТ"
        key = "ВАБ"
        self.assertEqual(permutation(alphabet, text, key, cypher_flag), 'ИПРТВЕ')

        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        cypher_flag = "0"
        text = "ИПРТВЕ"
        key = "ВАБ"
        self.assertEqual(permutation(alphabet, text, key, cypher_flag), 'ПРИВЕТ')
    def test_aphin(self):
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        cypher_flag = "1"
        text = "ПРИВЕТ"
        key = "ВГ"
        self.assertEqual(aphine(alphabet, text, key, cypher_flag), 'ВДФЖМЗ')

        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        cypher_flag = "0"
        text = "ВДФЖМЗ"
        key = "ВГ"
        self.assertEqual(aphine(alphabet, text, key, cypher_flag), 'ПРИВЕТ')

    def test_vizhen(self):
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        cypher_flag = "1"
        text = "ПРИВЕТ"
        key = "МЯУ"
        self.assertEqual(vizhenere(alphabet, text, key, cypher_flag), 'ЬПЬОДЁ')

        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        cypher_flag = "0"
        text = "ЬПЬОДЁ"
        key = "МЯУ"
        self.assertEqual(vizhenere(alphabet, text, key, cypher_flag), 'ПРИВЕТ')

    def test_shift(self):
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        cypher_flag = "1"
        text = "ПРИВЕТ"
        key = "Х"
        self.assertEqual(shift(alphabet, text, key, cypher_flag), 'ЕЁЮЧЪЗ')

        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        cypher_flag = "0"
        text = "ЕЁЮЧЪЗ"
        key = "Х"
        self.assertEqual(shift(alphabet, text, key, cypher_flag), 'ПРИВЕТ')

    def test_simsub(self):
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        cypher_flag = "1"
        text = "ПРИВЕТ"
        key = "ТУФХЦЧМНЮКШЩЪЫЯАБВГДЛОЖЗИЙПЕЁЬЭРС"
        self.assertEqual(simple_substitution(alphabet, text, key, cypher_flag), 'БВКФЧД')

        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        cypher_flag = "0"
        text = "БВКФЧД"
        key = "ТУФХЦЧМНЮКШЩЪЫЯАБВГДЛОЖЗИЙПЕЁЬЭРС"
        self.assertEqual(simple_substitution(alphabet, text, key, cypher_flag), 'ПРИВЕТ')
