class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = ret = 0
        current = None
        while index < len(nums):
            if(nums[index] != current):
                nums[ret] = nums[index]
                ret += 1
                current = nums[index]
            index += 1
        return ret


print(Solution().removeDuplicates([1, 1, 2]))
