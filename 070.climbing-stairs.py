# ex2tron's blog:
# http://ex2tron.wang

# 我的解法：
# 先解决小问题，最后逐步解决大问题，使用递归，超出时间限制
# class Solution:
#     def climbStairs(self, n):
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# 别人的代码：
class Solution:
    """
    :type n: int
    :rtype: int
    """
    # 斐波拉切数列
    def climbStairs(self, n):
        prev, current = 0, 1
        for _ in range(n):
            prev, current = current, prev + current,
        return current

if __name__=="__main__":
    print(Solution().climbStairs(35))