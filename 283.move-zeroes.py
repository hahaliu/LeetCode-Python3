# ex2tron's blog:
# http://ex2tron.wang

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        while count:
            nums.remove(0)
            nums.append(0)
            count -= 1

# 别人的代码：


# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         nums.sort(cmp=lambda a, b: 0 if b else -1)


l = [0, 1, 0, 3, 12]
Solution().moveZeroes(l)
print(l)
