# ex2tron's blog:
# http://ex2tron.wang

# class Solution:
#     def isPowerOfTwo(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n == 0:
#             return False
#         while n % 2 == 0:
#             n //= 2

#         return n == 1

# 别人的解法：

# 算法注解：
# 2^0:    1
# 2^1:   10
# 2^2:  100
# ……


# class Solution:
#     def isPowerOfTwo(self, n):
#         # return n > 0 and (n & (n-1)) == 0
#         # 或者
#         return n > 0 and (n & ~-n) == 0


# 周辉礼：转成2进制，1的个数是否为1
class Solution:
    def isPowerOfTwo(self, n):
        return bin(n).count('1') and n > 0
