# ex2tron's blog:
# http://ex2tron.wang


# 我的解法1：超出时间限制


# class Solution:
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         r_nums = range(1, n+1)
#         return [item for item in r_nums if item not in nums]


# 别人的代码：
# list不可以直接相减，但set可以
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums)+1)) - set(nums))

# 别人的代码2，思路清奇，厉害：
# class Solution:
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             index = abs(nums[i]) - 1
#             nums[index] = - abs(nums[index])
#             print(index, nums)
#         return [i + 1 for i in range(len(nums)) if nums[i] > 0]


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
