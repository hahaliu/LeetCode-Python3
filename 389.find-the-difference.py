# ex2tron's blog:
# http://ex2tron.wang

# class Solution:
#     def findTheDifference(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         s_list = list(t)
#         for ch in s:
#             if ch in s_list:
#                 s_list.remove(ch)

#         return s_list[0]

# 别人的写法：

import operator
from functools import reduce


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(operator.xor, map(ord, s+t)))


print(Solution().findTheDifference("a", "aa"))
