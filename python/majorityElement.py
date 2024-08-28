#august 28 2024

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # O(n) time | O(1) space
        #current = majority element
        current = 0
        #majority = count of current majority element
        majority = 0
        for n in nums:
            #update current majority element only if we encounter a new candidate to be one
            if majority == 0:
                current = n
            #update the count of the current candidate if it is the same as the current majority element
            if n == current:
                majority += 1
            #decrease the count of the current candidate if it is not the same as the current majority element
            else:
                majority -= 1
        return current
    

    # O(n log(n)) time | O(1) space
    def cheat_solution(self, nums: list[int]) -> int:
        return sorted(nums)[len(nums)//2]