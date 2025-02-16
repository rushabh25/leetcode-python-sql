# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyOdd = oddList = ListNode()
        dummyEven = evenList = ListNode()
        i = 1
        while head is not None:
            newNode = ListNode(head.val)
            if i % 2 != 0:
                oddList.next = newNode
                oddList = oddList.next
            else:
                evenList.next = newNode
                evenList = evenList.next
            head = head.next
            i += 1
        oddList.next = dummyEven.next
        return dummyOdd.next
