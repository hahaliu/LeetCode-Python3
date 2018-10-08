# ex2tron's blog:
# http://ex2tron.wang

# 我的思路：与升序后的数组进行比较
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sort = sorted(nums)
        start, end = -1, 0
        # print(nums_sort, nums)
        for i in range(len(nums)):
            if start == -1 and nums[i] != nums_sort[i]:
                start = i
            if start != -1:
                if nums[i] != nums_sort[i]:
                    end = i

        return end-start+1 if start != -1 else 0


# 别人的代码：没理解
# class Solution(object):
#     def findUnsortedSubarray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         right, left = -1, -1
#         min_from_right, max_from_left = nums[-1], nums[0]
#         for i in range(1, n):
#             max_from_left = max(max_from_left, nums[i])
#             min_from_right = min(min_from_right, nums[n-1-i])
#             if nums[i] < max_from_left:
#                 right = i
#             if nums[n-1-i] > min_from_right:
#                 left = n-1-i
#         return right-left+1


print(Solution().findUnsortedSubarray([2, 3, 1]))
