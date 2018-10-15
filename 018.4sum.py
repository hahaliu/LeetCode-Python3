# 我的解法：分成单数＋三数之和，超出时间限制
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 思路：同样转换成单数+三数之和，但优化了不符合的条件
        ret = []
        nums.sort()
        for i in range(len(nums)-3):
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                remain = target - nums[i]-nums[j]
                left, right = j+1, len(nums)-1
                while left < right:
                    if nums[left]+nums[right] == remain:
                        ret.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[left]+nums[right] < remain:
                        left += 1
                    else:
                        right -= 1

        return ret


print(Solution().fourSum([-1, -5, -5, -3, 2, 5, 0, 4], -7))
