class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 1. Our first goal is to return `k`, the number
        #    of items that ≠ `val`.
        # 2. Our second goal is to modify `nums` itself
        #    such that all the non-`val` items are moved
        #    to the start of the array, in any order.
        #
        # Since the number of items in `nums` and the
        # order of the items doesn't matter, we'll loop
        # through `nums` and anytime we see `val`, we'll
        # perform a swap with the last non-`val` item in
        # the array. By the end, this will have, in-place,
        # pushed all `val` items to the end.

        k = 0

        last_non_val_element_index = -1

        for i in range(len(nums)):
            if nums[i] == val:
                # Traverse nums backwards to find next `last_non_val_element_index`
                while nums[last_non_val_element_index] == val:
                    last_non_val_element_index -= 1

                    # Handle edge case where all items in `nums` are `val`
                    if abs(last_non_val_element_index) > len(nums):
                        break

                # Stop condition
                #
                # At the end, we effectively have two parts to the array: the
                # part we already swapped non-`val` numbers into, and the part
                # we swapped all the `val` numbers into.
                #
                # We are done when we would be looking for those non-`val` numbers
                # where we've already correctly swapped non-`val` numbers into.
                if len(nums) + last_non_val_element_index <= i:
                    break

                # Swap
                nums[i] = nums[last_non_val_element_index]
                nums[last_non_val_element_index] = val

            # Only increment `k` if we didn't already break
            k += 1
        
        return k