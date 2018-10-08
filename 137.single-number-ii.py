# ex2tron's blog:
# http://ex2tron.wang

# 旧的解题思路：简单，超时


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

# 我的思路2：使用collections
import collections


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(collections.Counter(nums).items(), key=lambda item: item[1])[0][0]

# 我的思路3：set元素重复3次减去旧的


# class Solution:
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return (sum(set(nums))*3 - sum(nums))//2


#　别人的思路：没看懂，待理解
# 因为都是整数，所以统计某一位1出现的个数，如果不是3的倍数，那么将这位设置为0，统计0的个数，不是3的倍数，那么将这位设置为1
# 循环完所有的位后，即可得到答案

# class Solution(object):
#     def singleNumber(self, A):
#         one, two = 0, 0
#         for x in A:
#             one, two = (~x & one) | (x & ~one & ~two), (~x & two) | (x & one)
#             print(one, two)

#         return one


print(Solution().singleNumber([2, 2, 3, 2]))
