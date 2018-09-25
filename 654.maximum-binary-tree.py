
# 我的思路：先求max，然后分成左右，最后左右分别递归
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        num_max = max(nums)
        max_index = nums.index(num_max)

        left, right = nums[:max_index], nums[max_index+1:]

        tree = TreeNode(num_max)
        tree.left = self.constructMaximumBinaryTree(left)
        tree.right = self.constructMaximumBinaryTree(right)

        return tree


#　别人的思路：遍历不递归，效率更好，但相比之下不好理解

# class Solution:
#     def constructMaximumBinaryTree(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: TreeNode
#         """
#         node_stack = []
#         for num in nums:
#             node = TreeNode(num)
#             while node_stack and num > node_stack[-1].val:
#                 node.left = node_stack.pop()
#             if node_stack:
#                 node_stack[-1].right = node
#             node_stack.append(node)

#         return node_stack[0]


print(Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))
