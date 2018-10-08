# ex2tron's blog:
# http://ex2tron.wang

# class Solution:
#     def isUgly(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         elements = [2, 3, 5]
#         if num == 1:
#             return True
#         elif num == 0:
#             return False
#         tresult = [num % item == 0 for item in elements]
#         if not any(tresult):
#             return False
#         element = elements[tresult.index(True)]
#         if num//element == 1:
#             return True
#         return self.isUgly(num//element)

# 别人的代码：


class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num //= i
        return num == 1


print(Solution().isUgly(1))
