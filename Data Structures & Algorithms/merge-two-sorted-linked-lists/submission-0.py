# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # If either list is completely empty, there is nothing to merge
        if not list1:
            return list2
        if not list2:
            return list1

        main_current = list1 if list1.val <= list2.val else list2
        donor_current = list1 if list1.val > list2.val else list2

        head = main_current  # Save for final return value

        while main_current or donor_current:
            # On every iteration, we want to prioritise the smallest value on the main array
            if donor_current.val <= main_current.val:
                # Merge donor node into main
                main_val = main_current.val        # To swap with donor's val
                main_next = main_current.next      # Save for setting donor's next
                main_current.next = donor_current  # Point main's current to the donor

                donor_val = donor_current.val      # To swap with main's val
                donor_next = donor_current.next    # Save for advancing donor later
                donor_current.next = main_next     # Point the donor to the next node

                # Swap values
                main_current.val = donor_val
                donor_current.val = main_val

                # Advance the donor to the next node
                donor_current = donor_next
            else:
                if not main_current.next and donor_current:
                    # Perform one final pointer swap, effectively concatenating
                    # the rest of the donor to main
                    main_current.next = donor_current
                    return head

                # Main's current value is the smaller value, so simply move on
                main_current = main_current.next

            if not donor_current and main_current:
                return head  # Donor has been fully merged, so we are done

        return head