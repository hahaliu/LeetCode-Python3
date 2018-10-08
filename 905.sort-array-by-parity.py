# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd, even = [], []
        while len(A) > 0:
            item = A.pop()
            if item % 2 == 0:
                even.append(item)
            else:
                odd.append(item)

        return even+odd


# 别人的方法，直接交换位置：
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        for j in range(len(A)):
            if A[j] & 1 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A
