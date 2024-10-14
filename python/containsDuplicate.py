class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = set()
        for num in nums:
            if num not in hashmap:
                hashmap.add(num)
            else:
                return True
        return False
         