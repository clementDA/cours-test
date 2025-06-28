import unittest
from src.ohce import OHCE
from utilities.testBuilder import OHCEBuilder

#classe de tests de la fonction palindrome
class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.builder = OHCEBuilder()

    #
    def test_palindrome_vide(self):
        ohce = self.builder.build()
        self.assertIn("Bien dit!", ohce.palindrome(""))

    def test_palindrome_palindrome(self):
        ohce = self.builder.build()
        self.assertIn("Bien dit!", ohce.palindrome("radar"))

    def test_palindrome_non_palindrome(self):
        ohce = self.builder.build()
        self.assertIn("nipal", ohce.palindrome("lapin"))

    def test_bonjour(self):
        ohce = self.builder.build()
        self.assertIn("Bonjour", ohce.palindrome(""))

    def test_aurevoir(self):
        ohce = self.builder.build()
        self.assertIn("Au revoir", ohce.palindrome(""))

    def test_palindrome_with_spaces(self):
        ohce = self.builder.build()
        self.assertIn("Bien dit!", ohce.palindrome(" "))
        self.assertIn(" nios", ohce.palindrome("soin "))


if __name__ == '__main__':
    unittest.main()
