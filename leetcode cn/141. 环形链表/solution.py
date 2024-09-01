# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slow, fast = head, head.next
        while fast != None and fast.next != None and slow != fast:
            slow = slow.next
            fast = fast.next.next

        return not (fast is None or fast.next is None)
        
