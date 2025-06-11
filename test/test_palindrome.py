import unittest
from src.ohce import OHCE

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.palind = OHCE()

    def test_palindrome_vide(self):
        self.assertIn("Bien dit!", self.palind.palindrome(""))

    def test_palindrome_palindrome(self):
        self.assertIn("Bien dit!", self.palind.palindrome("radar"))

    def test_palindrome_non_palindrome(self):
        self.assertIn("nipal", self.palind.palindrome("lapin"))

    def test_bonjour(self):
        self.assertIn("Bonjour", self.palind.palindrome(""))

    def test_aurevoir(self):
        self.assertIn("Au revoir", self.palind.palindrome(""))

if __name__ == '__main__':
    unittest.main()
