class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 1. 初始化为 0
        dp = [0] * (amount + 1)
        
        # 2. Base case: 凑成 0 元只有 1 种方法（什么都不选）
        dp[0] = 1
        
        # 3. 重点！先遍历硬币 (保证组合，不重复)
        for coin in coins:
            # 4. 再遍历金额
            for i in range(coin, amount + 1):
                # 5. 累加方法数
                dp[i] += dp[i - coin]
                
        return dp[amount]