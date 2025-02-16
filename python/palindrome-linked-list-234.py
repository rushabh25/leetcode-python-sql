from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverse(self, head: Optional[ListNode]) ->  Optional[ListNode]:
        return None

    def palindrome(self, head: Optional[ListNode]) -> bool:
        dummy = head
        stack = []
        while head is not None:
            stack.append(head.val)

        while dummy is not None:
            if stack.pop() != dummy.val:
                return False
        return True


