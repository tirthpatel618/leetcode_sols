class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l+r) // 2

            totalTime = 0
            for x in piles:
                totalTime += math.ceil(float(x) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k +1
        return res
    

# Koko Eating Bananas 
# one of the cooler problems ive done