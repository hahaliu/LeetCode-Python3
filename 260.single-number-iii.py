# 我的思路：使用collections.Counter统计

import collections


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_counter = sorted(collections.Counter(
            nums).items(), key=lambda item: item[1], reverse=False)
        # print(sorted_counter)
        return [sorted_counter[0][0]] + [sorted_counter[1][0]]

# 别人的代码：还不是特别理解
# import operator
# from functools import reduce


# class Solution:
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         x_xor_y = reduce(operator.xor, nums)
#         bit = x_xor_y & -x_xor_y
#         # print(x_xor_y, bit)
#         result = [0, 0]
#         for i in nums:
#             print(i & bit)
#             result[bool(i & bit)] ^= i
#             print(result)
#         return result


print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))
