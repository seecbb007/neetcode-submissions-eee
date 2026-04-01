class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        # create an array, and size for n + 1

        for i in range(n+1):
            output[i] = output[i >> 1] + (i & 1)
            # used to count the number of 1 in the binary 
            # right shift
            # bitewise AND to check the least significant bit of i
        return output    