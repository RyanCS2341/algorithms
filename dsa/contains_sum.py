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

if __name__ == "__main__":
    nums = [1, 2, 4, 6, 8, 9, 14, 15]
    target = 13
    hasSum = containsSum(nums, target)
    print(hasSum)