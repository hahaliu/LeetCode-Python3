class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dicts = {}
        for index, value in enumerate(nums):
            if target - value in dicts:
                return [dicts.get(target-value), index]
            dicts[value] = index


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         dicts = {}
#         for k, v in enumerate(nums):
#             if target - v in dicts:
#                 return [dicts.get(target-v), k]
#             dicts[v] = k


if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 9))
