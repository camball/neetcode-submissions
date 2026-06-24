class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        running_counter = 0
        for num in nums:
            if num == 1:
                running_counter += 1
                if running_counter > max_consecutive:
                    max_consecutive = running_counter
            else:
                running_counter = 0

        return max_consecutive