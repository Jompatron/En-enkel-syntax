import unittest

from molekyler import *

class SyntaxTest(unittest.TestCase):

    def test_LETTER_letter(self):
        """ Testar stor bokstav liten bokstav"""
        self.assertEqual(kollaGrammatiken())

    def test_Num(self):
        """ Testar siffra """
        self.assertEqual(kollaGrammatiken())

if __name__ == '__main__':
    main()