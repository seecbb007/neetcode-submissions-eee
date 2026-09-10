class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = (i - index) * height
                maxarea = max(maxarea, area)
                start = index
            stack.append((start, h))

        for index,h in stack:
            area = (len(heights) - index) * h
            maxarea = max(maxarea, area)
        return maxarea