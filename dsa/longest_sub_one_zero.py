import unittest

def longestSubstringOneZero(binaryString: str) -> int:
    left = curr = answer = 0
    for right in range(len(binaryString)):
        if binaryString[right] == "0":
            curr += 1
        while (curr > 1):
            if binaryString[left] == "0":
                curr -= 1
            left += 1

        answer = max(answer, right - left + 1)

    return answer

class TestLongestSubstringOneZero(unittest.TestCase):

    def test_longestSubstringOneZero_success(self):
        binaryString = "1100111101"
        answer = longestSubstringOneZero(binaryString)
        self.assertEqual(6, answer)

    def test_longestSubstringOneZero_single_one(self):
        binaryString = "1"
        answer = longestSubstringOneZero(binaryString)
        self.assertEqual(1, answer)
    
    def test_longestSubstringOneZero_single_zero(self):
        binaryString = "0"
        answer = longestSubstringOneZero(binaryString)
        self.assertEqual(1, answer)

    def test_longestSubstringOneZero_all_one(self):
        binaryString = "1111"
        answer = longestSubstringOneZero(binaryString)
        self.assertEqual(4, answer)

    def test_longestSubstringOneZero_all_zero(self):
        binaryString = "0000"
        answer = longestSubstringOneZero(binaryString)
        self.assertEqual(1, answer)
    
    def test_longestSubstringOneZero_empty(self):
        binaryString = ""
        answer = longestSubstringOneZero(binaryString)
        self.assertEqual(0, answer)

if __name__ == "__main__":
    unittest.main()