class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target_sum = total_sum // 2
        dp = [False] * (target_sum+1)
        dp[0] = True
        for num in nums:
            for j in range(target_sum, num-1, -1):
               
                dp[j] = dp[j] or dp[j-num]
        return dp[target_sum]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0: return 0 
        dp=[float("inf")]*(amount+1)
        dp[0]=0
        for i in range(1,len(dp)):
            for coin in coins:
                if i>=coin:
                    dp[i]=min(dp[i-coin]+1,dp[i])
        if dp[-1] == float("inf"):return -1
        return dp[-1]



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=m=nums[0]
        for i in nums[1:]:
            curr=max(i,curr+i)
            m=max(m,curr)
        return m