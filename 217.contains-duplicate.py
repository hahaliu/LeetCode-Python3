# ex2tron's blog:
# http://ex2tron.wang



class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))


# import collections

# class Solution:
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if not nums:
#             return False
#         dicts = collections.Counter(nums)
#         return dicts.most_common(1)[0][1] > 1


print(Solution().containsDuplicate([1, 2, 1, 3]))
