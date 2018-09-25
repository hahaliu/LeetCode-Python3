# 我的解法：先翻转，再求和，最后再翻转
# 解法没问题，能通过，稍显繁琐

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         dummy1, dummy2 = ListNode('-inf'), ListNode('-inf')
#         while l1:
#             dummy1.next, l1.next, l1 = l1, dummy1.next, l1.next
#         while l2:
#             dummy2.next, l2.next, l2 = l2, dummy2.next, l2.next

#         dummy = ListNode('-inf')
#         current = dummy
#         dummy1, dummy2 = dummy1.next, dummy2.next

#         carry, add = 0, 0
#         while dummy1 or dummy2:
#             add = carry
#             if dummy1:
#                 add += dummy1.val
#                 dummy1 = dummy1.next
#             if dummy2:
#                 add += dummy2.val
#                 dummy2 = dummy2.next

#             carry, add = divmod(add, 10)
#             current.next = ListNode(add)
#             current = current.next

#         if carry == 1:
#             current.next = ListNode(1)

#         dummy = dummy.next
#         result = ListNode('-inf')
#         while dummy:
#             result.next, dummy.next, dummy, = dummy, result.next, dummy.next

#         return result.next


# 别人的代码：转换成数字求和，再转成列表
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = 0, 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        num = num1 + num2
        head = ListNode(0)
        cur = head
        for st in str(num):
            temp = ListNode(int(st))
            cur.next = temp
            cur = temp
        return head.next


l = ListNode(4)
# l.next = ListNode(2)
# l.next.next = ListNode(6)

l2 = ListNode(8)
# l2.next = ListNode(3)
# l2.next.next = ListNode(4)

print(Solution().addTwoNumbers(l, l2))
