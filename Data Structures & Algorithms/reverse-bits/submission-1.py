class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n & 1
    # shift left and add the extract bit
            res = (res << 1) | bit

            n >>= 1 
            # shift right and process next bit
        return res    