class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        start = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == " ":
                left,right = start, i - 1
                while left < right:
                    s[left],s[right] = s[right], s[left]
                    left  += 1
                    right -= 1
                start = i + 1