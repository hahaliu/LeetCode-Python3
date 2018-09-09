# 我的代码也实现了，别人的代码更好一点

# 别人的代码：


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = []
        i, j, carry = len(num1)-1, len(num2)-1, 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += ord(num1[i])-ord('0')
                i -= 1
            if j >= 0:
                carry += ord(num2[j])-ord('0')
                j -= 1
            carry, result = divmod(carry, 10)
            ret.append(str(result))

        ret.reverse()
        return "".join(ret)


# 我的代码：

# class Solution(object):
#     def addStrings(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         ret, i, carry = "", 0, 0
#         if len(num1) >= len(num2):
#             ls, ss = num1, num2
#         else:
#             ls, ss = num2, num1

#         ls, ss = ls[::-1], ss[::-1]

#         while i < len(ss) or i < len(ls):
#             sum_i = 0
#             if i < len(ss) and i < len(ls):
#                 carry, val = divmod(int(ls[i])+int(ss[i])+carry, 10)
#             else:
#                 carry, val = divmod(int(ls[i])+carry, 10)
#             sum_i += val
#             ret += str(sum_i)
#             i += 1

#         if carry == 1:
#             ret += "1"

#         return ret[::-1]


print(Solution().addStrings("33", "19967"))
