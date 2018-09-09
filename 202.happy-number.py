class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lookup = []
        print(n)
        while n != 1 and n not in lookup:
            lookup.append(n)
            n = self.next(n)
            print(n)
        return n == 1

    def next(self, n):
        ret = 0
        for ch in str(n):
            ret += int(ch)**2
        return ret


print(Solution().isHappy(20))
