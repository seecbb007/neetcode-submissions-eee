class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0, len(heights) - 1
        res = 0

        while left < right:
            width = right - left
            h = min(heights[left],heights[right])
            curr_area = width * h

            res = max(res, curr_area)

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

        return res 