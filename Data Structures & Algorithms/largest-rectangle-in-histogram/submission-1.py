class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0

        for i in range(n):
            h = heights[i]
            left = i
            right = i
            while left >= 0 and heights[left] >= h:
                left -= 1
            while right < n and heights[right] >= h:
                right += 1

            w = right - left - 1
            res = max(res, w * h)
        return res 