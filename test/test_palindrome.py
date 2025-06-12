import unittest
from src.ohce import OHCE

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.testpalind = OHCE()

    def test_palindrome_vide(self):
        self.assertIn("Bien dit!", self.testpalind.palindrome(""))

    def test_palindrome_palindrome(self):
        self.assertIn("Bien dit!", self.testpalind.palindrome("radar"))

    def test_palindrome_non_palindrome(self):
        self.assertIn("nipal", self.testpalind.palindrome("lapin"))

    def test_bonjour(self):
        self.assertIn("Bonjour", self.testpalind.palindrome(""))

    def test_aurevoir(self):
        self.assertIn("Au revoir", self.testpalind.palindrome(""))

if __name__ == '__main__':
    unittest.main()
