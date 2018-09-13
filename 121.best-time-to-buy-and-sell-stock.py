
# 我的解法1：超出时间限制
# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         sort_prices, sort_prices_reverse = sorted(
#             prices), sorted(prices, reverse=True)
#         result = []
#         for i in sort_prices:
#             index_i = prices.index(i)
#             for j in sort_prices_reverse:
#                 if j in prices[index_i+1:] and j > i:
#                     result.append(j-i)

#         return max(result) if result else 0

# 我的解法2：运行更快，但TMD还是超出时间限制


# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         ret = []
#         for i in range(len(prices)-1):
#             max_v = max(prices[i+1:])
#             if max_v > prices[i]:
#                 ret.append(max_v - prices[i])

#         return max(ret) if ret else 0


# 别人的代码：
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
