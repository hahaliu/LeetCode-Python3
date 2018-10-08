# ex2tron's blog:
# http://ex2tron.wang

# 这题没写出来，别人的代码：


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        m = len(nums)
        if m == 1:
            return [nums]
        if m == 0:
            return [[]]
        ans1 = self.permute(nums[1:])
        b = nums[0]
        n = len(ans1)
        for i in range(m):
            for j in range(n):
                str1 = []
                str1 += ans1[j][:i]
                str1 += [b]
                str1 += ans1[j][i:]
                ans.append(str1)
        return ans


print(Solution().permute([1, 2, 3]))
