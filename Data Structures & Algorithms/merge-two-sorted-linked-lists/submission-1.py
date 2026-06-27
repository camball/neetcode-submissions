# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pseudo_head = node = ListNode()
        
        # Continually "pop" a node from the start of one of the two
        # lists, whichever is smaller, and append to the merged list
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            
            # Advance our merged list
            node = node.next

        # Append the rest of whichever list wasn't exhausted first
        # above. One of these two will be empty at this time.
        node.next = list1 or list2

        return pseudo_head.next