# ex2tron's blog:
# http://ex2tron.wang

# 没做出来，思路不对
# class Solution:
#     def minPathSum(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         m ,n= len(grid),len(grid[0])
#         if m==1 and n==1:
#             return grid[0][0]
#         if (m==1 and n>1) :
#             return sum(grid[0])
#         if (m>1 and n==1):
#             return sum(zip(*grid)[0])
        
#         minV = []
#         # minV[0][0] = grid[0][0]
#         # minV[0][1] = grid[0][1]
#         # minV[1][0] = grid[1][0]
#         print(minV)

#         for i in range(m):
#             minV.append([0])
#             for j in range(n):
#                 if i-1<0 and j-1<0:
#                     minV[i][0] = grid[0][0]
#                 elif i-1<0:
#                     minV[i].append(minV[i][j-1]+grid[i][j-1] )
#                 elif j -1 <0:
#                     minV[i].append(minV[i-1][j]+grid[i-1][j] )
#                 else:
#                     minV[i].append(min( minV[i-1][j]+grid[i-1][j],minV[i][j-1]+grid[i][j-1] ))
#                 print(minV)
#         return minV

# 别人的代码：
class Solution:
    def minPathSum(self, grid):
        sum = list(grid[0])
        for j in range(1, len(grid[0])):
            sum[j] = sum[j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            sum[0] += grid[i][0]
            # print(sum)
            for j in range(1, len(grid[0])):
                sum[j] = min(sum[j - 1], sum[j]) + grid[i][j]

        return sum[-1]

print(Solution().minPathSum([[1,3,4],[2,5,1]]))