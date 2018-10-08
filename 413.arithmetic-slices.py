# ex2tron's blog:
# http://ex2tron.wang

# 做不出来
# class Solution:
#     def numberOfArithmeticSlices(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
        # if len(A)<3:
        #     return 0
        # start ,i= 0 ,0
        # count = 0
        # diff = 0
        # find = False

        # array = []
        # while i <len(A):
        #     if find:
        #         if A[i] == start + diff*count:
        #             count+=1
        #             i+=1
        #         else:
        #             array.append(count)
        #             count = 0
        #             find = False
        #             if len(A)-i<3:
        #                 break

        #     if not find and (A[i]-A[i+1]) == (A[i+1]-A[i+2]) :
        #         start=A[i]
        #         diff = A[i+1]-A[i]
        #         count = 3
        #         find =True

        # array.append(count)

        # return array
        
# 别人的代码：
# class Solution(object):
#     def numberOfArithmeticSlices(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         res, i = 0, 0
#         while i+2 < len(A):
#             start = i
#             while i+2 < len(A) and A[i+2] + A[i] == 2*A[i+1]:
#                 res += i - start + 1
#                 i += 1
#             i += 1

#         return res

# 别人的方法二：
class Solution:
    def numberOfArithmeticSlices(self, arr):
        n = len(arr)
        if n <3:
            return 0
        else:
            num = [0 for i in range(n)]
            num[0] = 0
            num[1] = 0
            for i in range(2,n):
                if arr[i] - arr[i-1] == arr[i-1] - arr[i-2]:
                    num[i] = num[i-1] + 1
            return sum(num)


print(Solution().numberOfArithmeticSlices([1, 2,3,4,5]))