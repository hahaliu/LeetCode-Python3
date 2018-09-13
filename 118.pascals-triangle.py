# class Solution:
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """

#         ret = []
#         current = []
#         for i in range(1, numRows+1):
#             if i == 1:
#                 current = [1]
#             elif i == 2:
#                 current = [1, 1]
#             else:
#                 temp = [1]
#                 for i in range(len(current)-1):
#                     temp.append(current[i]+current[i+1])
#                 temp.append(1)
#                 current = temp.copy()

#             ret.append(current)

#         return ret


# 别人的代码，很优雅：
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []

        res = [[1]]
        for _ in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1]+[0], [0]+res[-1]))]

        return res


print(Solution().generate(3))
