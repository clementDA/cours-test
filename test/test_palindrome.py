import unittest
from function import palindrom



class TestPalindrome(unittest.TestCase):

    def test_palindrome_simple(self):
        self.assertEqual(palindrom("radar"), "Bien dit!")

    


if __name__ == '__main__':
    unittest.main()


    