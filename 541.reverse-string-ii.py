# ex2tron's blog:
# http://ex2tron.wang

# 我的做法：翻转字符串+不翻转合并在一起
# class Solution:
#     def reverseStr(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: str
#         """
#         return "".join([ s[i*k:i*k+k][::-1] if i%2 ==0  else s[i*k:i*k+k]    for i in  range(0, len(s), 2*k)])

# 别人的代码：
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 字符串有不可变性，所以需要转换成list
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)           

# 别人的代码2:


# class Solution:
#     def reverseStr(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: str
#         """
#         l = len(s)
#         res = ''
#         for i in range(0, l, 2 * k):
#             res += s[i:i + k][::-1] + s[i + k:i + 2 * k]

#         return res




print(Solution().reverseStr("abcdefg",2))