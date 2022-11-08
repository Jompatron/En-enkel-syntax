import unittest

from molekyler_labb_9 import *

class SyntaxTest(unittest.TestCase):

# Tester från labb 8

    def test_LETTER_letter(self):
        """ Testar stor bokstav liten bokstav"""
        self.assertEqual(kollaGrammatiken("Ag3"), "Formeln är syntaktiskt korrekt")

    def test_letter_letter(self):
        """ Testar liten bokstav liten bokstav"""
        self.assertEqual(kollaGrammatiken("cr12"), "Saknad stor bokstav vid radslutet cr12")

    def test_letter_x(self):
        """ Testar endast liten bokstav"""
        self.assertEqual(kollaGrammatiken("c"), "Saknad stor bokstav vid radslutet c")

    def test_siffra_noll(self):
        """ Testar om siffran är endast 0"""
        self.assertEqual(kollaGrammatiken("Cr0"), "För litet tal vid radslutet ")

    def test_siffra_ett(self):
        """ Testar om siffran är endast 1"""
        self.assertEqual(kollaGrammatiken("Pb1"), "För litet tal vid radslutet ")

    def test_siffra_start_noll(self):
        """ Testar om första siffran är 0"""
        self.assertEqual(kollaGrammatiken("H01011"), "För litet tal vid radslutet 1011")


# Tester för labb 9 sample input 1

    def test_LETTER_letter_9(self):
        """ Testar stor bokstav liten bokstav"""
        self.assertEqual(kollaGrammatiken("Na"), "Formeln är syntaktiskt korrekt")

    def test_LETTER_num_letter_9(self):
        """ Testar en molekyl"""
        self.assertEqual(kollaGrammatiken("H2O"), "Formeln är syntaktiskt korrekt")

    def test_groups(self):
        """ Testar stor flera grupper efter varandra """
        self.assertEqual(kollaGrammatiken("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")

    def test_flera_siffror(self):
        """ Testar flera siffror i molekylen"""
        self.assertEqual(kollaGrammatiken("Na332"), "Formeln är syntaktiskt korrekt")




if __name__ == '__main__':
    main()