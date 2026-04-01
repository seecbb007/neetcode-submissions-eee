class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
    
        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # 空字符串1种解法，首字符非0才1种解法

        for i in range(2, n + 1):
            # 单独解码最后一位
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            
            # 解码最后两位
            if "10" <= s[i-2:i] <= "26":
                dp[i] += dp[i-2]

        return dp[n]