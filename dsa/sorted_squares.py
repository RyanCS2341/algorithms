import unittest

def sortedSquares(s: list[int]) -> list[int]:
    squared = []
    for i in range(len(s)):
        squared.append(s[i] ** 2)
    squared.sort()
    return squared

class TestContainsSum(unittest.TestCase):

    def test_sortedSquares_non_positive(self):
        s = [-4, 4, 0]
        sqaured = [0, 16, 16]
        sortedSquares(s)
        self.assertEqual(sqaured, sortedSquares(s))
    
    def test_sortedSquares_positive(self):
        s = [0, 10, 4]
        sqaured = [0, 16, 100]
        sortedSquares(s)
        self.assertEqual(sqaured, sortedSquares(s))

if __name__ == "__main__":
    unittest.main()