# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode(0)
        carry = 0

        while l1 is not None or l2 is not None:
            sum = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + carry
            carry = sum // 10
            rem = sum % 10

            new_node = ListNode(rem)
            curr.next = new_node
            curr = curr.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if carry == 1:
            new_node = ListNode(1)
            curr.next = new_node
            curr = curr.next
        return dummy.next
