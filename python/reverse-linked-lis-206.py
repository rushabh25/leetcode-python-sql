# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseList = None
        while head is not None:
            new_node = ListNode(head.val)
            new_node.next = reverseList
            reverseList = new_node
            head = head.next
        return reverseList
