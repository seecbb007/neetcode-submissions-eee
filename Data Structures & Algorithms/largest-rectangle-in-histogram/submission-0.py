class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0

        for i, curr_h in enumerate(heights):
            while stack and heights[stack[-1]] > curr_h:
                h = heights[stack.pop()]
                right = i
                left = stack[-1]
                w = right - left - 1 # (right - 1) - (left - 1) - 1 = right - 1 - left + 1 
                res = max(res, w * h)
            stack.append(i)
        return res 