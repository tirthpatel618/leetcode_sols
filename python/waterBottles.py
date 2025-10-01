class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numEmpty = numBottles
        drank = numBottles
        while numEmpty >= numExchange:
            numEmpty = numEmpty - numExchange + 1
            drank += 1
        return drank

#might be the easiest problem ever