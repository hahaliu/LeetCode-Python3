class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos = True if x >= 0 else False
        x = int(str(abs(x))[::-1])
        x = x if pos else -x
        return x if abs(x) <= 0x7fffffff else 0


if __name__ == '__main__':
    print(Solution().reverse(-15342364691))
