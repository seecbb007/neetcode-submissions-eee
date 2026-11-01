class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0, len(height) - 1

        leftmax,rightmax = 0, 0
        res = 0

        while left < right:
            if height[left] < height[right]:
                leftmax = max(leftmax, height[left])
                res += leftmax - height[left]
                left += 1

            else:
                rightmax = max(rightmax, height[right])
                res += rightmax - height[right]
                right -= 1

        return res