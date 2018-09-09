class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = sorted(list(set(nums)), reverse=True)
        print(set_nums)
        return set_nums[2] if len(set_nums) >= 3 else set_nums[0]


print(Solution().thirdMax([1, 2]))
