import unittest
from src.function import palindrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome_simple(self):
        self.assertEqual(palindrome("radar"), "Bien dit!")

if __name__ == '__main__':
    unittest.main()
