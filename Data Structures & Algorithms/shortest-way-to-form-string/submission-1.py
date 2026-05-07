class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        count = tindex = 0
        while tindex < len(target):
            start = tindex 
            for char in source :
                if tindex < len(target) and char == target[tindex]:
                    tindex += 1

            if start == tindex:
                return - 1

            count += 1
        return count
        