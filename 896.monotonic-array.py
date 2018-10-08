# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        up, down = False, False
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                up = True
            elif A[i] < A[i-1]:
                down = True
        # 前面思路对的，这里返回值没想到，我的想法是：up^down，但有问题
        return not up or not down
        # 周辉礼的思路：
        # return A==sorted(A) or A ==sorted(A,reverse=True)


print(Solution().isMonotonic([4, 4]))
