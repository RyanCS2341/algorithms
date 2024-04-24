import unittest

def maxWindowLengthSum(sumMax: int, arr: list[int]) -> int:
    left = 0
    curr = 0
    answer = 0
    for right in range(len(arr)):
        curr += arr[right]
        while (curr > sumMax):
            curr -= arr[left]
            left += 1

        answer = max(answer, right - left + 1)

    return answer

class TestMaxWindowLengthSum(unittest.TestCase):

    def test_maxWindowLengthSum_success(self):
        arr = [1, 1, 4, 2, 1, 1, 1, 1, 1, 1]
        answer = maxWindowLengthSum(6, arr)
        self.assertEqual(6, answer)

if __name__ == "__main__":
    unittest.main()