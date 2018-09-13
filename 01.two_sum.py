# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """

#         dicts = {}
#         for index, value in enumerate(nums):
#             if target - value in dicts:
#                 return [dicts.get(target-value), index]
#             dicts[value] = index

# 周辉礼的解法：


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, value in enumerate(nums):
            if target - value in nums:
                if index != nums.index(target - value):
                    return index, nums.index(target - value)


if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 9))
