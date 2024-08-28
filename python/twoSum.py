class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff = {}
        for i, num in enumerate(nums):
            if target - num in diff:
                return [i, diff[target - num]]
            diff[num] = i