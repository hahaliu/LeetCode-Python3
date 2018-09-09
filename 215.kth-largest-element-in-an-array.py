class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        order_nums = sorted(nums, reverse=True)
        return order_nums[k-1]
