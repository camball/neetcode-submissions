class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s, f = 0, 0

        while s < len(nums) or f < len(nums):
            # Found the next zero value
            while s < len(nums) and nums[s] != 0:
                s += 1

            # Find the next non-zero value after the zero
            f = s
            while f < len(nums) and nums[f] == 0:
                f += 1

            # Don't swap if our fast pointer already reached the end
            if f == len(nums):
                break

            nums[s], nums[f] = nums[f], nums[s]