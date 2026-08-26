class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

        """
        Index: prefix sum
            0: nums[0]
            1: nums[0] + nums[1]
               ...
            n: nums[0] + nums[1] + ... + nums[n]
        """

        # Build prefix sum array
        self.prefix_sums = []
        total = 0
        for num in nums:
            total += num
            self.prefix_sums.append(total)


    def sumRange(self, left: int, right: int) -> int:
        sum_l = 0 if left - 1 < 0 else self.prefix_sums[left - 1]
        return self.prefix_sums[right] - sum_l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
