# class Solution:
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         n_sqrt = int(n**0.5)+1


# class Solution(object):
#     _num = [0]
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         num = self._num
#         while len(num) <= n:
#             num += min(num[-i*i] for i in range(1, int(len(num)**0.5+1))) + 1,
#             print(num)
#         return num[n]

print(Solution().numSquares(13))