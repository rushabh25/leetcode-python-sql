###
# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
###

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                new_node = ListNode(list1.val)
                curr.next = new_node
                curr = curr.next
                list1 = list1.next
            else:
                new_node = ListNode(list2.val)
                curr.next = new_node
                curr = curr.next
                list2 = list2.next
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        else:
            curr.next = None

        return dummy.next
