# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        result = ListNode(0)
        lastSorted = head
        result.next = lastSorted
        current = head.next
        
        while current:
            if lastSorted.val <= current.val:
                lastSorted = lastSorted.next
                current = current.next
            else:
                currentHead = result
                while currentHead.next.val < current.val:
                    currentHead = currentHead.next
                lastSorted.next = current.next
                current.next = currentHead.next
                currentHead.next = current
                current = lastSorted.next

        return result.next
