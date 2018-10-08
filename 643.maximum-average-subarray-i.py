# ex2tron's blog:
# http://ex2tron.wang

# 我的代码：超出时间限制


# class Solution:
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#         """

#         ret = float('-inf')
#         for i in range(len(nums)-k+1):
#             ret = max(ret, sum(nums[i:k+i]))

#         return ret/k


# 别人的代码：
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ret, total = sum(nums[:k]), sum(nums[:k])

        for i in range(k, len(nums)):
            total += nums[i]-nums[i-k]
            ret = max(ret, total)

        return ret/k


print(Solution().findMaxAverage([-1], 1))
