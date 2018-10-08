# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        W = int(area**0.5)
        L = 0
        while W > 0:
            if area % W == 0:
                L = area//W
                break
            W -= 1

        return [L, W]

# 别人的代码：


import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area))
        while area % w:
            w -= 1

        return [area // w, w]
