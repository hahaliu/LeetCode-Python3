# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        for _ in range(len(A[0])):
            ret.append([])

        for row in A:
            for j in range(len(A[0])):
                ret[j].append(row[j])
        return ret


# 别人的代码：
# class Solution:
#     def transpose(self, A):
#         """
#         :type A: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         return list(zip(*A))


print(Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
