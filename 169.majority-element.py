# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        elements = list(set(nums))
        counts = [nums.count(e) for e in elements]
        return elements[counts.index(max(counts))]


print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
