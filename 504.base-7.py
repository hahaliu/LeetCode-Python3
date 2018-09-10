# class Solution:
#     def convertToBase7(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         ret = ""
#         negative = True if num < 0 else False

#         shangshu = abs(num)
#         while shangshu >= 7:
#             shangshu, yushu = divmod(shangshu, 7)
#             ret += str(yushu)

#         ret += str(shangshu)
#         return '-'+ret[::-1] if negative else ret[::-1]


# 别人的代码：
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return "-"+self.convertToBase7(-num)
        if num < 7:
            return str(num)
        return self.convertToBase7(num//7)+str(num % 7)


print(Solution().convertToBase7(-1))
