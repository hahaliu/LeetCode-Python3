
# 我的方法：二进制统计1的个数（不合题目要求，但结果正确）
# class Solution:
#     def countBits(self, num):
#         """
#         :type num: int
#         :rtype: List[int]
#         """
#         ret = []
#         for i in range(0,num+1):
#             ret.append(bin(i).count('1'))
#         return ret

# 方法二：自底至上的动态规划
# 记录求过的解来节省时间
# 0: 0
# 1: 1
# 2: 2^1            = 1
# 3: 2^1+1          = 1   +1
# 4: 2^2            = 1
# 5: 2^2+1          = 1  +1
# ……
# 结论，num中1的个数是 num&1 + num//2中1的个数
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0]
        for i in range(1,num+1):
            ret.append((i&1)+ret[i//2])
            # 或者：
            # ret.append((i&1)+ret[i>>1])
        return ret