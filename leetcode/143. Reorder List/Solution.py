# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Split list at the middle of the list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        first, second = head, slow.next
        slow.next = None
        
        # Reserve the second list
        second = self.reserve(second)
        
        # Insert second list into first one
        while second:
            temp = second.next
            second.next = first.next
            first.next = second
            first = first.next.next
            second = temp
        
    def reserve(self, head):
        result, p, q = None, head, head.next
        while p:
            p.next = result
            result = p
            p = q
            q = None if not q else q.next
        return result
