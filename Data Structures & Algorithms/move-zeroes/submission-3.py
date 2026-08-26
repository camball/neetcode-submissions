class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0

        # Perform a max of `len(nums)` iterations
        for f in range(len(nums)):
            # Swap when we see a non-zero value
            if nums[f] != 0:
                nums[s], nums[f] = nums[f], nums[s]
                
                # No matter where we advance `f` to,
                # we always need to swap into the very
                # next `s` spot to preserve a gap-free
                # relative ordering.
                s += 1