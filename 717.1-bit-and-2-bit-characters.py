# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        index = 0
        while index < len(bits)-1:
            if bits[index] == 1:
                index += 2
            elif bits[index] == 0:
                index += 1

        return index != len(bits)


# 别人的代码：
# class Solution(object):
#     def isOneBitCharacter(self, bits):
#         """
#         :type bits: List[int]
#         :rtype: bool
#         """
#         parity = 0
#         for i in reversed(range(len(bits)-1)):
#             if bits[i] == 0:
#                 break
#             parity ^= bits[i]

#         return parity == 0


print(Solution().isOneBitCharacter([1, 1, 0]))
