# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for _ in range(1, rowIndex+1):
            # res = [list(map(lambda x, y: x+y, res+[0], [0]+res))]
            # 方式二：使用zip函数
            res = [x+y for x, y in zip(res+[0], [0]+res)]
        return res


print(Solution().getRow(2))
