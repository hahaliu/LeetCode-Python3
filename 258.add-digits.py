# ex2tron's blog:
# http://ex2tron.wang


# 数根：
# https://en.wikipedia.org/wiki/Digital_root
# https://blog.csdn.net/NoMasp/article/details/50392541
# https://blog.csdn.net/ray0354315/article/details/53991199


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (num-1) % 9 + 1 if num > 0 else 0
