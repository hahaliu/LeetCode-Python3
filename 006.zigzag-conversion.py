# ex2tron's blog:
# http://ex2tron.wang

# 我的写法：太复杂，可以实现
# class Solution:
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         if numRows == 1:
#             return s
#         ret = []
#         split = 2*(numRows-1)
#         for i in range(numRows):
#             if i == 0 or i == numRows-1:
#                 split = 2*(numRows-1)
#                 index = i
#                 while True:
#                     if index >= len(s):
#                         break
#                     ret.append(s[index])
#                     index += split
#             else:
#                 split -= 2
#                 index = i
#                 while True:
#                     if index >= len(s):
#                         break
#                     ret.append(s[index])
#                     index += split
#                     if index < len(s):
#                         ret.append(s[index])
#                         index += 2*(numRows-1) - split
#         return ''.join(ret)


# 别人的写法：

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        index, step = 0, 1
        l = [""] * numRows

        for item in s:
            l[index] += item
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step

        return "".join(l)


print(Solution().convert("PAYPALISHIRING", 3))
# PINALSIGYAHRPI
# PINALSIGYAHRPI
# PAHNAPLSIIGYIR
# PAHNAPLSIIGYIR
