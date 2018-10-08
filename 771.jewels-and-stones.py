# ex2tron's blog:
# http://ex2tron.wang

# import collections


# class Solution:
#     def numJewelsInStones(self, J, S):
#         """
#         :type J: str
#         :type S: str
#         :rtype: int
#         """
#         counter = collections.Counter(S)
#         return sum(counter[item] for item in J)


# 别人的代码：

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(s in J for s in S)


print(Solution().numJewelsInStones('z', 'ZZ'))
