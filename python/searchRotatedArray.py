class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        #first find the pivot
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                #if the middle is past the right, then the pivot is past the middle
                #so you update the lower bound accordingly
                l = m + 1
            else:
                #pivot is in first half. Shrink right to the mid 
                r = m
        #this lands at l as the pivot
        pivot = l
        l, r = 0, len(nums) -1

        
        if target >= nums[pivot] and target <= nums[r]:
            #if the target is past the pivot AND less than the right most, 
            #it is in the [pivot, r] interval
            l = pivot
        else:
            # if its not you shift the interval to [l, pivot-1]
            r = pivot -1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1
        return -1


        
