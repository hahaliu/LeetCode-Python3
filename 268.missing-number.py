# ex2tron's blog:
# http://ex2tron.wang

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums)+1))-sum(nums)
