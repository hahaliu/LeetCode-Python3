class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last,now = 0,0
        for num in nums:
            last,now = now,max(last+num,now)
            # print(last,now)
        return now

print(Solution().rob([1,2,3,1]))
