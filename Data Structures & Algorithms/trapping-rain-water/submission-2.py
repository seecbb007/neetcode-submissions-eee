class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        for i in range(n):
            leftmax = 0
            rightmax = 0
            for l in range(i + 1):
                leftmax = max(leftmax, height[l])
            for r in range(i,n):
                rightmax = max(rightmax, height[r])
            res += min(leftmax, rightmax) - height[i]
        return res 

        