
# 我的思路:太复杂,但可以通过


# class Solution:
#     def isToeplitzMatrix(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: bool
#         """
#         row, col = len(matrix), len(matrix[0])
#         row_right, col_right = True, True
#         for c in range(col):
#             r1, c1 = 0, c
#             base = matrix[r1][c1]
#             for i in range(1, min(row, col-c)):
#                 r1 += 1
#                 c1 += 1

#                 if(matrix[r1][c1] != base):
#                     row_right = False

#         for r in range(1, row):
#             r1, c1 = r, 0
#             base = matrix[r1][c1]
#             for i in range(1, min(row-r, col)):
#                 r1 += 1
#                 c1 += 1
#                 if(matrix[r1][c1] != base):
#                     col_right = False

#         return row_right and col_right


class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # print([i == 0 or j == 0 or matrix[i-1][j-1] == val for i,
        #        row in enumerate(matrix) for j, val in enumerate(row)])
        return all(i == 0 or j == 0 or matrix[i-1][j-1] == val for i, row in enumerate(matrix) for j, val in enumerate(row))


print(Solution().isToeplitzMatrix([
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]))
