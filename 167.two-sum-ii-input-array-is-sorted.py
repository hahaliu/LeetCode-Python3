# ex2tron's blog:
# http://ex2tron.wang

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(numbers)-1
        while start != end:
            add_v = numbers[start]+numbers[end]
            if(add_v > target):
                end -= 1
            elif (add_v < target):
                start += 1
            else:
                return [start+1, end+1]


print(Solution().twoSum([0, 0, 3, 4], 0))
