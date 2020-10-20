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
        head1, head2 = self.devideList(head)
        head2 = self.reverse(head2)
        self.merge(head1, head2)

    def devideList(self, head):
        fast, slow = head, head
        pre = TreeNode(0)
        pre.next = slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            pre = pre.next
        pre.next = None
        return head, slow

    def reverse(self, head):
        result = None
        while head:
            first = head
            second = head.next
            first.next = result
            result = first
            head = second
        return result

    def merge(self, head1, head2):
        while head1 and head2:
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            if temp1:
                head2.next = temp1
            head1 = temp1
            head2 = temp2
