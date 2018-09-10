# class Solution:
#     def nextGreaterElement(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         ret = []
#         for item in nums1:
#             index = nums2.index(item)
#             if index == len(nums2)-1:
#                 ret.append(-1)
#             else:
#                 find = False
#                 for i in nums2[index+1:]:
#                     if i > item:
#                         find = True
#                         ret.append(i)
#                         break
#                 if not find:
#                     ret.append(-1)

#         return ret


# 别人的代码：
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stk, lookup = [], {}
        for num in nums:
            while stk and num > stk[-1]:
                lookup[stk.pop()] = num
            stk.append(num)
        while stk:
            lookup[stk.pop()] = -1
        return map(lambda x: lookup[x], findNums)


print(list(Solution().nextGreaterElement([2, 4], [2, 1, 3, 4])))
