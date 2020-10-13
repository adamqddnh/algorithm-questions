# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l1
        while l1 and l1.next and l2 and l2.next:
            l1.val += l2.val
            l1 = l1.next
            l2 = l2.next
        l1.val += l2.val
        l1.next = l2.next if l2.next else l1.next

        result = head
        i = 0
        preHead = ListNode(0)
        preHead.next = head
        while head:
            temp = head.val + i
            i = temp / 10
            head.val = temp % 10
            head = head.next
            preHead = preHead.next
        if i > 0:
            preHead.next = ListNode(i)

        return result
        
