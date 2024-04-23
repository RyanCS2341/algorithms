import unittest

def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s)-1
    while left < right:
        curLeft = s[left]
        curRight = s[right]
        s[left] = curRight
        s[right] = curLeft
        left+=1
        right-=1

class TestReverseString(unittest.TestCase):

    def test_reverseString_success(self):
        letters = ["h", "e", "l", "l", "o"]
        reversed = ["o", "l", "l", "e", "h"]
        reverseString(letters)
        self.assertEqual(reversed, letters)
    
    def test_reverseString_single(self):
        letters = ["a"]
        reversed = ["a"]
        reverseString(letters)
        self.assertEqual(reversed, letters)

if __name__ == "__main__":
    unittest.main()