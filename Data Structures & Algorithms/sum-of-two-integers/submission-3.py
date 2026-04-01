class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF  # Maximum positive integer for 32-bit
        mask = 0xFFFFFFFF # Mask to get last 32 bits (to simulate 32-bit overflow)

        while b != 0:
            withCarry = (a ^ b) & mask  # Sum without carry
            carry = ((a & b) << 1) & mask  # Calculate carry and apply mask
            a, b = withCarry, carry  # Update a and b

        # If a is greater than the max positive 32-bit integer, we simulate a negative number
        if a > MAX:
            return ~(a ^ mask)
        
        return a
