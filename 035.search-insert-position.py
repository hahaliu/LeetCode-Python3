# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(target in nums):
            return nums.index(target)

        nums.append(target)
        return sorted(nums).index(target)
