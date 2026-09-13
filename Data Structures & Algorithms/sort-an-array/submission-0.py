from random import randint

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Quicksort.
        """

        # Base cases
        if len(nums) < 2:
            return nums

        if len(nums) == 2:
            if nums[0] < nums[1]:
                return nums
            else:
                return [nums[1], nums[0]]

        # Recursive case
        pivot_index = randint(0, len(nums) - 1)

        nums_smaller_than_pivot = [num for idx, num in enumerate(nums) if num <= nums[pivot_index] and idx != pivot_index]
        nums_greater_than_pivot = [num for idx, num in enumerate(nums) if num > nums[pivot_index] and idx != pivot_index]

        lhs = self.sortArray(nums_smaller_than_pivot)
        rhs = self.sortArray(nums_greater_than_pivot)
        
        return lhs + [nums[pivot_index]] + rhs