class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k:
            nums.insert(0, nums.pop())
            k -= 1


# 别人的方法：
# class Solution:
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         nums[:] = nums[len(nums)-k:]+nums[:len(nums)-k]


nums = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(nums, 3)

print(nums)
