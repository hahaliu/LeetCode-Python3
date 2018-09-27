
#　没做出来，需要参考
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         m, n = len(nums1), len(nums2)
#         median_index = (m+n)//2 if (m+n) % 2 != 0 else []
#         index1, index2 = 0, 0
#         ret = []
#         while index1 < m or index2 < n:
#             val = 0
#             if index1 < m:
#                 val = nums1[index1]
#                 index1 += 1
#                 index2 -= 1 if index2 != 0 else index2
#             if index2 < n:
#                 if nums2[index2] < val:
#                     val = nums2[index2]
#                     index1 = index1-1 if index1 != 0 else index1
#                     index2 += 1

#             ret.append(val)
#             print(ret)
#             if len(ret) >= (m+n)//2+1:
#                 return ret[-1] if (m+n) % 2 else ret[-1]+ret[-2]


print(Solution().findMedianSortedArrays([1, 2, 3], [4, 5, 6]))
