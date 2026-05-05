class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        slist = s.split()
        return len(slist[-1])