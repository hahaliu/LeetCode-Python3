# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 我的解法：有问题

# class Solution:
#     def isPalindrome(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         length = self.getLength(head)
#         if length == 1:
#             return True

#         right_order = []
#         slow, fast = head, head
#         while fast and fast.next:
#             right_order.append(slow.val)
#             slow, fast = slow.next, fast.next.next

#         right_order = right_order[::-1]
#         count = 0
#         while slow:
#             if slow.val != right_order[count]:
#                 return False
#             slow, count = slow.next, count+1

#         return True

#     def getLength(self, node):
#         count = 0
#         while node:
#             count += 1
#             node = node.next
#         return count


# 别人的代码：
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reverse, fast = None, head
        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next

        tail = head.next if fast else head

        is_palindrome = True
        while reverse:
            is_palindrome = is_palindrome and reverse.val == tail.val
            reverse.next, head, reverse = head, reverse, reverse.next
            tail = tail.next

        return is_palindrome


l = ListNode(1)
l.next = ListNode(0)
l.next.next = ListNode(1)
# l.next.next.next = ListNode(0)

print(Solution().isPalindrome(l))
