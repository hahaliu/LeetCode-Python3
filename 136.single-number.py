# 别人的代码：

import operator
from functools import reduce


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)


# 我的答案1
# class Solution:
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         elements = set(nums)
#         for e in elements:
#             if(nums.count(e) == 1):
#                 return e


# 我的答案2
# class Solution:
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         elements = set(nums)
#         ret = None
#         for e in elements:
#             # enums = nums.copy()
#             nums.remove(e)
#             if e not in nums:
#                 ret = e
#                 break
#         return ret


print(Solution().singleNumber([2]))
