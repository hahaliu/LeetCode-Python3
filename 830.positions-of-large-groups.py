# class Solution:
#     def largeGroupPositions(self, S):
#         """
#         :type S: str
#         :rtype: List[List[int]]
#         """
#         ret = []
#         start, end = 0, 0
#         for i in range(len(S)-1):
#             if S[i] != S[i+1]:
#                 end = i
#                 if end-start+1 >= 3:
#                     ret.append([start, end])
#                 start = i+1
#             else:
#                 end = i+1

#         if end-start+1 >= 3:
#             ret.append([start, end])

#         return ret


# 别人的代码，跟我思路一样，更简洁一些(注意数组边界的情况)
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ret = []
        i = 0
        for j in range(len(S)):
            if j == len(S)-1 or S[j] != S[j+1]:
                if j-i+1 >= 3:
                    ret.append([i, j])
                i = j+1
        return ret


# print(Solution().largeGroupPositions("abbxxxxzzyyyy"))
print(Solution().largeGroupPositions("aaa"))
