# ex2tron's blog:
# http://ex2tron.wang

# 这题不会，
#　参考别人解法
# https://blog.csdn.net/asd136912/article/details/78987624
# https://segmentfault.com/a/1190000003914228


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxl = 0
        start = 0
        for i in range(n):
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]


print(Solution().longestPalindrome('babad'))
