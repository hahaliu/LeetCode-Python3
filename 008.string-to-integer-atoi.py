# ex2tron's blog:
# http://ex2tron.wang


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.lstrip()
        if s[0] != '+' and s[0] != '-' and (s[0] < '0' or s[0] > '9'):
            return 0

        end = 1
        start = 1 if s[0] == '+' or s[1] == '-' else 0
        for i in range(start, len(s)):
            if s[i] < '0' or s[i] > '9':
                end = i
                break
            else:
                end += 1
        return s[start:end+1]


print(Solution().myAtoi('-90'))
