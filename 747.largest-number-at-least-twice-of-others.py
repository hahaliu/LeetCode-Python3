# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1):
            return 0
        lst = sorted(nums, reverse=True)
        return nums.index(lst[0]) if lst[0] >= 2*lst[1] else -1


print(Solution().dominantIndex([0, 0, 2, 3]))
