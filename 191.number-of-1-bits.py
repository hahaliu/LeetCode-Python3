# ex2tron's blog:
# http://ex2tron.wang

# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         return (bin(n)[2:]).count('1')

# 别人的代码：


class Solution:
    def hammingWeight(self, n):
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result


print(Solution().hammingWeight(11))
