class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Compute a prefix sum array in O(n) time
        prefix_sums = [0] * len(nums)

        count = 0
        for idx, num in enumerate(nums):
            count += num
            prefix_sums[idx] = count

        # Use prefix array to compute each side's sum in O(n) time
        for i in range(len(nums)):
            to_left = 0 if i == 0 else prefix_sums[i - 1]
            to_right = prefix_sums[len(nums) - 1] - prefix_sums[i]
            if to_left == to_right:
                return i

        return -1