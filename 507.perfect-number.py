class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 2:
            return False
        ret_array = [1]
        sqrtx = int(num**0.5)+1
        for i in range(2, sqrtx):
            shangshu, yushu = divmod(num, i)
            if not yushu:
                ret_array.append(i)
                ret_array.append(shangshu)

        return num == sum(ret_array)

# 别人的代码：
# class Solution(object):
#     def checkPerfectNumber(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num <= 0:
#             return False

#         sqrt_num = int(num ** 0.5)
#         total = sum(i+num//i for i in range(1, sqrt_num+1) if num % i == 0)
#         if sqrt_num ** 2 == num:
#             total -= sqrt_num
#         return total - num == num


print(Solution().checkPerfectNumber(4))
