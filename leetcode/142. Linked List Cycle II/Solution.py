# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        hasCycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                hasCycle = True
                break
        if not hasCycle:
            return None

        first = head
        while first is not slow:
            first = first.next
            slow = slow.next

        return slow
