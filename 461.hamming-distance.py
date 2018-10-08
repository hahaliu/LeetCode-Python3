# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return (bin(x ^ y)[2:]).count('1')
