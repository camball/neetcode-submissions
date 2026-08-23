class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_locations = {value: index for index, value in enumerate(nums)}

        for index, num in enumerate(nums):
            if (diff := target - num) in nums_locations and index != nums_locations[diff]:
                return [index, nums_locations[diff]]