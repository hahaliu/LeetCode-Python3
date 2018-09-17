class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = ret = 0
        while index < len(nums):
            if (nums[index] != val):
                nums[ret] = nums[index]
                ret += 1
            index += 1
        return ret


print(Solution().searchInsert([0, 1, 2, 2, 3, 0, 4, 2], 2))
