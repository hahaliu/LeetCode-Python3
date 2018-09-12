# class Solution:
#     def flipAndInvertImage(self, A):
#         """
#         :type A: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         rows = len(A)
#         for i in range(rows):
#             A[i].reverse()
#             A[i] = [1-item for item in A[i]]

#         return A


# 别人的代码：

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            for i in range((len(row) + 1)//2):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1

        return A
