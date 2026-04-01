class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        str_x = str(x)
        
        if str_x[0] == "-":
            reverseStr = "-" + str_x[:0:-1]
        else:
            reverseStr = str_x[::-1]     
        reverseStr = int(reverseStr)
        if reverseStr < INT_MIN or reverseStr > INT_MAX:
            return 0

        return reverseStr