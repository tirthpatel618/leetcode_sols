class Solution:
    def climbStairs2(self, n: int) -> int:
        prev = 1
        prev2 = 0

        for i in range(1, n+1):
            curi = prev + prev2
            prev2 = prev
            prev = curi
        return prev
    
    def climbStairs(self, n):
        if (n <=2):
            return n
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
