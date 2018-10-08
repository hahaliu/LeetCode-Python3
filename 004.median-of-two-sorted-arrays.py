# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1+nums2)

        n = len(nums)
        return (nums[n//2]+nums[n//2-1])/2 if n % 2 == 0 else nums[n//2]


print(Solution().findMedianSortedArrays([1], [1, 2]))
