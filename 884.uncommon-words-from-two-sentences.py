# 别人的代码：
import collections


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count = collections.Counter(A.split()) + collections.Counter(B.split())
        return [item for item in count if count[item] == 1]


# class Solution:
#     def uncommonFromSentences(self, A, B):
#         """
#         :type A: str
#         :type B: str
#         :rtype: List[str]
#         """
#         words = list(set((A+" "+B).split()))
#         A, B = A.split(), B.split()
#         # print(words)
#         ret = []
#         for word in words:
#             if A.count(word) == 1 and word not in B:
#                 ret.append(word)
#             elif B.count(word) == 1 and word not in A:
#                 ret.append(word)
#             else:
#                 pass
#         return ret


print(Solution().uncommonFromSentences(
    "d b zu d t", "udb zu ap"))
