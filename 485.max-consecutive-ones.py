# ex2tron's blog:
# http://ex2tron.wang

# 别人的代码：


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, local_max = 0, 0
        for n in nums:
            local_max = local_max+1 if n else 0
            result = max(result, local_max)
        return result

# class Solution:
#     def findMaxConsecutiveOnes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums = map(str, nums)
#         nums_str = "".join(nums)
#         nums_array = nums_str.split('0')
#         return max([len(item) for item in nums_array])


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
