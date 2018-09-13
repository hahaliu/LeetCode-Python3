import collections


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_counter = collections.Counter(nums)
        degree = max(nums_counter.values())

        ret = []
        for k in nums_counter.keys():
            if nums_counter[k] == degree:
                temp = len(nums) - nums[::-1].index(k)-nums.index(k)
                ret.append(temp)
        return min(ret)


# 别人的代码：
# import collections


# class Solution(object):
#     def findShortestSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         counts = collections.Counter(nums)
#         left, right = {}, {}
#         for i, num in enumerate(nums):
#             left.setdefault(num, i)
#             right[num] = i
#         print(left, right)
#         degree = max(counts.values())
#         return min(right[num]-left[num]+1 for num in counts.keys() if counts[num] == degree)


print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
