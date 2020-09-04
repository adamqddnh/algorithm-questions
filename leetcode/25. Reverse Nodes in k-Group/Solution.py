# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tempNode = ListNode(0)
        result = tempNode
        while head:
            last = self.slice(head, k)
            if last:
                tempHead = last.next
                last.next = None
                temp, first = self.reverse(head)
                head = tempHead
                tempNode.next = temp
                tempNode = first
            else:
                tempNode.next = head
                head = None
            
        return result.next
        
    def slice(self, head, k):
        i = 1
        current = head
        while current and i < k:
            i += 1
            current = current.next
        return current
    
    def reverse(self, head):
        result = None
        first = head
        while head:
            temp = head.next
            head.next = result
            result = head
            head = temp
        return result, first
