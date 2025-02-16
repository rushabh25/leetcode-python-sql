# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB

        while currA != currB:
            if currA is not None:
                currA = currA.next
            else:
                currA = headB
            if currB is not None:
                currB = currB.next
            else:
                currB = headA
        return currA
