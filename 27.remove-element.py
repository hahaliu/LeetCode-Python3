class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(target in nums):
            return nums.index(target)

        for item in nums:
            if(item >= target):
                return nums.index(item)

        return len(nums)


print(Solution().searchInsert([1, 3, 5, 6], 2))
