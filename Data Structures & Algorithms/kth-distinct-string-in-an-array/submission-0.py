class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        currk = 0
        for i, char in enumerate(arr):
            if count[char] == 1:
                currk += 1
                if currk == k:
                    return char
        return ""