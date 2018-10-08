# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_s = ""
        s = s.lower()
        for item in s:
            if ('a' <= item <= 'z') or ('0' <= item <= '9'):
                valid_s += item
        if not valid_s:
            return True
        else:
            return valid_s == valid_s[::-1]


print(Solution().isPalindrome('race a car'))
