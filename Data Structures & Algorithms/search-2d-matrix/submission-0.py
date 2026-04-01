class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int)-> bool:
        def findTarget(row, target):
            left, right = 0 ,len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        for r in matrix:
            res = findTarget(r,target)
            if res:
                return True
        return False