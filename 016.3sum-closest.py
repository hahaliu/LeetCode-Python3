
# 我的解法，思路是对的，也可以通过，但需要优化


# class Solution:
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         min_dis = float('inf')
#         ret = 0
#         nums.sort()
#         for i in range(len(nums)-2):
#             if i == 0 or nums[i] > nums[i-1]:
#                 left = i+1
#                 right = len(nums)-1
#                 while left < right:
#                     add = nums[i]+nums[left]+nums[right]
#                     if abs(target-add) < min_dis:
#                         ret = add
#                         min_dis = abs(target-add)
#                     else:
#                         if target-add < 0:
#                             right -= 1
#                             while left < right and nums[right] == nums[right+1]:
#                                 right -= 1
#                         else:
#                             left += 1
#                             while left < right and nums[left] == nums[left-1]:
#                                 left += 1
#         return ret


# 优化后的代码
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_dis, ret = float('inf'), float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left, right = i+1, len(nums)-1
                while left < right:
                    diff = target - (nums[i]+nums[left]+nums[right])
                    if abs(diff) < min_dis:
                        ret = nums[i]+nums[left]+nums[right]
                        min_dis = abs(diff)
                    if diff < 0:
                        right -= 1
                    elif diff > 0:
                        left += 1
                    # 距离为０，直接返回
                    else:
                        return target
        return ret


print(Solution().threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82))
