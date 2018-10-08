# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        reverse_bin = [str(1-int(ch)) for ch in bin(num)[2:]]
        return int("".join(reverse_bin[reverse_bin.index('1'):]), 2) if '1' in reverse_bin else 0


print(Solution().findComplement(4))
