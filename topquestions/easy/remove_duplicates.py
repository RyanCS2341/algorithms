import unittest

def removeDuplicates(nums: list[int]) -> int:
        replaceIndex = 1
        for curIndex in range(1, len(nums)):
            if (nums[curIndex] != nums[curIndex-1]):
                nums[replaceIndex] = nums[curIndex]
                replaceIndex += 1

        return replaceIndex;
                

class TestContainsSum(unittest.TestCase):

    def test_removeDuplicates_oneunique(self):
        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        uniqueElements = removeDuplicates(nums)
        self.assertEqual(1, uniqueElements)
    
    def test_removeDuplicates_twounique(self):
        nums = [1, 2]
        uniqueElements = removeDuplicates(nums)
        self.assertEqual(2, uniqueElements)

    def test_removeDuplicates_single(self):
        nums = [1]
        uniqueElements = removeDuplicates(nums)
        self.assertEqual(1, uniqueElements)

if __name__ == "__main__":
    unittest.main()