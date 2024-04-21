import unittest

def palindrome(word: str):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left = left + 1
        right = right - 1

    return True

class TestPalindrome(unittest.TestCase):

    def test_palindrome_success(self):
        word = "racecar"
        self.assertTrue(palindrome(word))

    def test_palindrome_empty(self):
        word = ""
        self.assertTrue(palindrome(word))

    def test_palindrome_fail(self):
        word = "palindrome"
        self.assertFalse(palindrome(word))

if __name__ == "__main__":
    unittest.main()