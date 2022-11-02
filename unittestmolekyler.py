import unittest

from molekylerjohannes import *

class SyntaxTest(unittest.TestCase):

    def test_LETTER_letter(self):
        """ Testar stor bokstav liten bokstav"""
        self.assertEqual(kollaGrammatiken("Ag3"), "Formeln är syntaktiskt korrekt")

    def test_LETTER_LETTER(self):
        """ Testar stor bokstav stor bokstav"""
        self.assertEqual(kollaGrammatiken("AG3"), "Formeln är syntaktiskt in-korrekt")

    def test_letter_letter(self):
        """ Testar liten bokstav liten bokstav"""
        self.assertEqual(kollaGrammatiken("cr12"), "Saknad stor bokstav vid radslutet")

    def test_letter_x(self):
        """ Testar endast liten bokstav"""
        self.assertEqual(kollaGrammatiken("c"), "Saknad stor bokstav vid radslutet")

    def test_siffra_noll(self):
        """ Testar om siffran är endast 0"""
        self.assertEqual(kollaGrammatiken("Cr0"), "	För litet tal vid radslutet")

    def test_siffra_ett(self):
        """ Testar om siffran är endast 1"""
        self.assertEqual(kollaGrammatiken("Pb1"), "	För litet tal vid radslutet")

    def test_siffra_start_noll(self):
        """ Testar om första siffran är 0"""
        self.assertEqual(kollaGrammatiken("H01011"), "	För litet tal vid radslutet")


if __name__ == '__main__':
    main()
