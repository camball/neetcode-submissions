from functools import reduce

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # O(n) calculation of sum of entire `nums`
        full_sum = reduce(lambda prev, curr: prev + curr, nums)
        
        # O(n) single pass over array
        left = 0
        for idx, num in enumerate(nums):
            right = full_sum - num - left
            if right == left: return idx
            left += num

        return -1