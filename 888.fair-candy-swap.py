
# 我的最初解法：超出时间限制


# class Solution:
#     def fairCandySwap(self, A, B):
#         """
#         :type A: List[int]
#         :type B: List[int]
#         :rtype: List[int]
#         """
#         average_sum = (sum(A)+sum(B))//2
#         diff = sum(A) - average_sum
#         for i in A:
#             if (i-diff) in B:
#                 return [i, i-diff]

#         return []

# 借鉴之后的改进写法：
class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = (sum(A)-sum(B))//2
        setA, setB = set(A), set(B)
        for i in setA:
            if (i-diff) in setB:
                return [i, i-diff]

        return []


print(Solution().fairCandySwap([1, 2, 5], [2, 4]))
