# Medium 
def waysToSplitArray(self, nums: List[int]) -> int:
    n = len(nums)
    right_sum = sum(nums)
    left_sum = 0
    cnt = 0
    for i in range(n-1):
        left_sum += nums[i]
        right_sum -= nums[i]
        cnt += (left_sum >= right_sum)
    return cnt