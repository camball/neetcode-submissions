# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        O(n) solution by only iterating through nodes at most once.
        
        In-place linked-list modification gives O(1) space.
        """
        head = head.next

        to_resume = head

        while to_resume.next.next is not None:
            current = to_resume
            tmp_sum = 0

            while current.val != 0:
                tmp_sum += current.val
                current = current.next

            to_resume.val = tmp_sum

            if current.next is None:
                # Account for scenario where suffix is, e.g., (14) -> (9) -> (0)
                to_resume.next = None
                break
            else:
                to_resume.next = current.next
                to_resume = to_resume.next  # Advance onward

        # Account for scenario where suffix is, e.g., (14) -> (0)
        if to_resume.next and to_resume.next.val == 0:
            to_resume.next = None

        return head
