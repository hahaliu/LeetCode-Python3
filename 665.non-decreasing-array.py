# ex2tron's blog:
# http://ex2tron.wang


# 我的代码，有问题：
# class Solution:
#     def checkPossibility(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         found = False
#         for i in range(len(nums)-1):
#             if nums[i] > nums[i+1]:
#                 if found:
#                     return False
#                 if i+1 == len(nums)-1:
#                     return True
#                 if i != 0:
#                     if (nums[i+1]-nums[i-1]) > 1:
#                         found = True
#                     else:
#                         return False
#                 else:
#                     count = 1
#         return True

# 别人的代码：


class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        found, prev = False, nums[0]
        for i in range(1, len(nums)):
            if prev > nums[i]:
                print(prev)
                if found:
                    return False
                if i-2 < 0 or nums[i-2] <= nums[i]:
                    prev = nums[i]
                found = True
            else:
                prev = nums[i]

        return True


print(Solution().checkPossibility([1, 4, 3, 2]))
