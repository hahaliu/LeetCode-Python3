# 别人的代码：
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = '1'
        for i in range(n-1):
            c = start[0]
            nums = 0
            tmp = []
            for s in start:
                if s == c:
                    nums += 1
                else:
                    tmp.append([nums, c])
                    nums = 1
                    c = s
            tmp.append([nums, c])
            start = ''.join([str(d[0])+d[1] for d in tmp])

        return start

# class Solution:
#     def splitStr(self, s):
#         words = []
#         current = s[0]
#         temp = ""
#         finished = False
#         for i in range(len(s)):
#             if s[i] == current:
#                 temp += s[i]
#                 finished = True
#             else:
#                 finished = False
#                 words.append(temp)
#                 if(i == len(s)-1):
#                     words.append(s[i])
#                 else:
#                     current = temp = s[i]
#         if finished:
#             words.append(temp)

#         return words

#     def getresult(self, s, nn):
#         ret = s
#         if nn-1:
#             ret = ""
#             words = self.splitStr(s)
#             for item in words:
#                 n = len(item)
#                 ret += str(n)+item[0]

#             return self.getresult(ret, nn-1)
#         else:
#             return ret

#     def countAndSay(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """

#         return self.getresult("1", n)
