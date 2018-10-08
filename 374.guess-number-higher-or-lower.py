# ex2tron's blog:
# http://ex2tron.wang

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


# class Solution(object):
#     def guessNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         left, right = 1, n
#         while left <= right:
#             mid = (left+right)//2
#             if guess(mid) == -1:
#                 left = mid + 1
#             elif guess(mid) == 1:
#                 right = mid - 1
#             else:
#                 ret = mid
#                 break
#         return ret


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if guess(mid) <= 0:
                right = mid - 1
            else:
                left = mid + 1
        return left


print(Solution().guessNumber(10))
