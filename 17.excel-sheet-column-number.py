class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ret = 0
        for item in s:
            num = ord(item)-64
            ret += num*pow(26, n-1)
            n -= 1
        return ret
