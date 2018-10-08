# ex2tron's blog:
# http://ex2tron.wang

# 别人的代码：


class Solution:
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            result += n // 5
            n //= 5
        return result


# class Solution:
#     def trailingZeroes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         ret = str(self.f(n))
#         return len(ret) - len(str(int(ret[::-1])))

#     def f(self, n):
#         if (n == 1):
#             return 1
#         else:
#             return n*self.f(n-1)


print(Solution().trailingZeroes(5))
