# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 我的代码：先求长度，再取半
# class Solution:
#     def middleNode(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         head_length = self.getLength(head)
#         mid = head_length//2
#         ret = ListNode(0)
#         count = 0
#         while head:
#             if count == mid:
#                 ret.next = head
#             head = head.next
#             count += 1

#         return ret.next

#     def getLength(self, node):
#         count = 0
#         while node:
#             count += 1
#             node = node.next
#         return count


# 别人的代码：
# 快的是慢的两倍
class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow


l = ListNode(0)
l.next = ListNode(1)
l.next.next = ListNode(2)

print(Solution().middleNode(l).next.val)
