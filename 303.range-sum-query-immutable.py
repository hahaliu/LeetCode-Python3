
# 我的方法一：使用python语法
# class NumArray:
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums
        

#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         return sum(self.nums[i:j+1])
        

# 方法二：使用动态规划
# 使用已经求过的解来节省时间
# 前j+1的和-前i个的和
# 自顶而下的备忘录法
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.accumulate = [0]
        for num in nums:
            self.accumulate.append(num+self.accumulate[-1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accumulate[j+1]-self.accumulate[i]
        
