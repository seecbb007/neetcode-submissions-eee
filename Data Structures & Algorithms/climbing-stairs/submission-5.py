class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        currone = 1
        prevtwo = 1

        for _ in range(n - 1):
            temp = currone
            currone = prevtwo + currone
            prevtwo = temp
        return currone