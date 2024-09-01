# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = fake = ListNode()
        sign = 0
        while l1 or l2 or sign:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            num = num1 + num2 + sign
            head.next = ListNode(num % 10)
            head = head.next
            sign = num // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if sign:
            head.next = ListNode(sign)
        return fake.next
