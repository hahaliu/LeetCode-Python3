# https://leetcode-cn.com/problems/add-two-numbers/description/

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """

#         dummy = ListNode(0)
#         current, carry = dummy, 0

#         while l1 or l2:
#             val = carry
#             if l1:
#                 val += l1.val
#                 l1 = l1.next
#             if l2:
#                 val += l2.val
#                 l2 = l2.next
#             carry, val = divmod(val, 10)
#             current.next = ListNode(val)
#             current = current.next

#         if carry == 1:
#             current.next = ListNode(1)

#         return dummy.next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        val, carry = 0, 0
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)
        return dummy.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
lr = Solution().addTwoNumbers(l1, l2)
print(lr)
