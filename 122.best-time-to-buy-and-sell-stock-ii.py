# ex2tron's blog:
# http://ex2tron.wang

# 这题不会

# 别人的思路：


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            print(prices[i+1]-prices[i])
            profit += max(0, prices[i+1]-prices[i])
        return profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 10]))
