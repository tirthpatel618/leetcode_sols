#medium

class Solution:
    def findMin(self, nums: list[int]) -> int:
        smallest = 5000
        for i in range(len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
        return smallest

        