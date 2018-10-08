# ex2tron's blog:
# http://ex2tron.wang


# 我的思路:先展平成一维,再分割


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row, col = len(nums), len(nums[0])
        if r*c != row*col:
            return nums

        nums_1D = nums[0]
        for i in range(1, row):
            nums_1D += nums[i]

        if r == 1:
            return [nums_1D]

        ret = []
        for i in range(r):
            ret.append(nums_1D[i*c:i*c+c])
        return ret


# 别人的代码:原矩阵与新矩阵的数学对应关系
# class Solution(object):
#     def matrixReshape(self, nums, r, c):
#         """
#         :type nums: List[List[int]]
#         :type r: int
#         :type c: int
#         :rtype: List[List[int]]
#         """
#         if not nums or r*c != len(nums) * len(nums[0]):
#             return nums

#         result = [[0 for _ in range(c)] for _ in range(r)]
#         count = 0
#         for i in range(len(nums)):
#             for j in range(len(nums[0])):
#                 result[count/c][count % c] = nums[i][j]
#                 count += 1
#         return result


print(Solution().matrixReshape([[1, 2, 3], [4, 5, 6]], 6, 1))
