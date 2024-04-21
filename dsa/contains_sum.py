import unittest

def containsSum(nums: list[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left < right:
        curSum = nums[left] + nums[right]
        if (curSum == target):
            return True
        elif (curSum > target):
            right -= 1
        else:
            left += 1

    return False

class TestContainsSum(unittest.TestCase):

    def test_containsSum_success(self):
        # Test 1
        nums = [1, 2, 4, 6, 8, 9, 14, 15]
        target = 13
        self.assertTrue(containsSum(nums, target))

    def test_containsSum_over(self):
        # Test 2
        nums = [1, 2, 4, 6, 8, 9, 14, 15]
        target = 100
        self.assertFalse(containsSum(nums, target))

    def test_containsSum_empty(self):
        # Test 3
        nums = []
        target = 5
        self.assertFalse(containsSum(nums, target))

    def test_containsSum_single(self):
        # Test 4
        nums = [5]
        target = 5
        self.assertFalse(containsSum(nums, target))

    def test_containsSum_fail(self):
        # Test 5
        nums = [1, 2, 3, 4, 4, 5, 6]
        target = 8
        self.assertTrue(containsSum(nums, target))

if __name__ == "__main__":
    unittest.main()