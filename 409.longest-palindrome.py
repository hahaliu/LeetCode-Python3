# 别人更优雅的代码：

import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = 0
        for _, v in collections.Counter(s).items():
            odds += v & 1
        return len(s) - odds + int(odds > 0)


# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         set_s = list(set(s))
#         count_ch = [s.count(ch) for ch in set_s]
#         count, odd = 0, False
#         for ch in count_ch:
#             if ch % 2 == 0:
#                 count += ch
#             elif ch//2 >= 1:
#                 count += ch-1
#                 odd = True
#             else:
#                 odd = True
#         count = count+1 if odd else count

#         return count


print(Solution().longestPalindrome("abbb"))
