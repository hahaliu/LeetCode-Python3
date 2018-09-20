
# 方法一
# 自底至上的动态规划
# 先判断前i个房间能获得的最多金钱
# maxV[i] = max( maxV[i-2]+nums[i], maxV[i-1] )
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        max_profit = []
        max_profit.append(nums[0])
        max_profit.append(max(nums[:2]))
        
        for i in range(2,len(nums)):
            max_profit.append(max(max_profit[i-2]+nums[i],max_profit[i-1]))

        return max_profit[-1]


# 改进的动态规划，不需要数组存储
# class Solution:
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         last,now = 0,0
#         for num in nums:
#             last,now = now,max(last+num,now)
#         return now

print(Solution().rob([2,7,9,3,1]))
