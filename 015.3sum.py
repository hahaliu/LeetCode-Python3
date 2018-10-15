
# 我的解法：超出时间限制
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         ret = []
#         for i in range(len(nums)):
#             remain = 0 - nums[i]
#             for j in range(i+1, len(nums)-1):
#                 remain2 = remain - nums[j]
#                 if remain2 in nums[j+1:]:
#                     lst = sorted([nums[i], nums[j], remain2])
#                     if lst not in ret:
#                         ret.append(lst)
#         return ret


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #　思路：需要求解的是ａ+b＝-c
        ret = []
        nums.sort()
        for i in range(len(nums)-2):
            # 这个条件防止两个元素相同导致的重复问题
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = len(nums)-1
                while left < right:
                    add = nums[i]+nums[left]+nums[right]
                    if add == 0:
                        ret.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # 下面两个ｗhile用来去重复元素，如[-2,0,0,2,2]
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif add < 0:
                        left += 1
                    else:
                        right -= 1

        return ret


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
