# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow is fast):
                return True
        return False
