class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        num = num if num >= 0 else 4294967296-abs(num)
        dicts = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

        ret = ""
        quotient, remainder = num, 0
        while quotient > 15:
            quotient, remainder = divmod(quotient, 16)
            ret += str(remainder) if remainder < 10 else dicts[remainder]

        ret += str(quotient) if quotient < 10 else dicts[quotient]
        return ret[::-1]

# 别人的代码：
# class Solution(object):
#     def toHex(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         if not num:
#             return "0"

#         result = []
#         while num and len(result) != 8:
#             h = num & 15
#             if h < 10:
#                 result.append(str(chr(ord('0') + h)))
#             else:
#                 result.append(str(chr(ord('a') + h-10)))
#             num >>= 4
#         result.reverse()

#         return "".join(result)


print(Solution().toHex(-1))
